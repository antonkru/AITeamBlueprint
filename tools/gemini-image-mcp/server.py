"""
Gemini Image Generation MCP Server
Uses Google's Imagen 3 model via the Gemini API (free tier).
Requires: GEMINI_API_KEY environment variable.
"""

import os
from datetime import datetime
from pathlib import Path

from google import genai
from google.genai import types as genai_types
from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("Gemini Image Generation")

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def _client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    return genai.Client(api_key=api_key)


def _save(image_bytes: bytes, prefix: str, prompt: str) -> str:
    slug = prompt[:40].strip().replace(" ", "_").replace("/", "-")
    path = OUTPUT_DIR / f"{prefix}-{slug}.png"
    path.write_bytes(image_bytes)
    return str(path)


@mcp.tool()
def generate_image(prompt: str, number_of_images: int = 1, aspect_ratio: str = "1:1") -> list:
    """
    Generate images using Google's Imagen 3 model (free tier via Gemini API).

    Args:
        prompt: Text description of the image to generate.
        number_of_images: How many images to generate (1-4).
        aspect_ratio: One of '1:1', '16:9', '9:16', '4:3', '3:4'.

    Returns:
        Inline image(s) plus saved file paths.
    """
    number_of_images = max(1, min(4, number_of_images))
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    response = _client().models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=genai_types.GenerateImagesConfig(
            number_of_images=number_of_images,
            aspect_ratio=aspect_ratio,
        ),
    )

    results = []
    for i, generated in enumerate(response.generated_images):
        image_bytes = generated.image.image_bytes
        results.append(Image(data=image_bytes, format="png"))
        path = _save(image_bytes, f"{timestamp}-{i+1}", prompt)
        results.append(f"Saved: {path}")

    return results


@mcp.tool()
def generate_image_gemini(prompt: str) -> list:
    """
    Generate an image using Gemini 2.0 Flash native image output.
    Good alternative to Imagen 3 for prompts that need Gemini's instruction-following.

    Args:
        prompt: Text description of the image to generate.

    Returns:
        Inline image(s), any accompanying text, and saved file paths.
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    response = _client().models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=genai_types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    results = []
    for i, part in enumerate(response.candidates[0].content.parts):
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            image_bytes = part.inline_data.data
            results.append(Image(data=image_bytes, format="png"))
            path = _save(image_bytes, f"{timestamp}-gemini-{i+1}", prompt)
            results.append(f"Saved: {path}")
        elif part.text:
            results.append(part.text)

    return results


if __name__ == "__main__":
    mcp.run()
