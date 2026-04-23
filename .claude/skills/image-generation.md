# Image Generation Skill

## Purpose
Guide agents to produce professional, high-quality images using the two Gemini API image generation tools available via MCP.

## Available Tools

- `mcp__gemini-image__generate_image` — Google Imagen 3. Parameters: `prompt` (str), `number_of_images` (1–4), `aspect_ratio` (one of `1:1`, `16:9`, `9:16`, `4:3`, `3:4`). Returns inline images and saved file paths.
- `mcp__gemini-image__generate_image_gemini` — Gemini 2.0 Flash native image generation. Parameter: `prompt` (str) only. Returns a single image.

---

## When to Use Each Model

### Use Imagen 3 (`generate_image`) when:
- Output quality and photorealism are the primary requirement
- The image is a deliverable in its own right (marketing asset, hero banner, product image)
- Aspect ratio control is needed (e.g. banner vs portrait vs square)
- Generating multiple variants to choose from (set `number_of_images` to 3 or 4)
- The prompt is straightforward and descriptive

### Use Gemini 2.0 Flash (`generate_image_gemini`) when:
- The prompt requires world knowledge, reasoning, or multi-step logic
- Accurate text must appear inside the image (labels, signs, diagrams)
- The image accompanies a text explanation and visual/text coherence matters

**Decision rule:** Default to Imagen 3 for any professional/corporate deliverable. Use Gemini 2.0 Flash only when prompt complexity or text-rendering requirements exceed what a descriptive prompt alone can achieve.

---

## Aspect Ratio Selection (Imagen 3 only)

| Ratio | Dimensions (approx) | Use for |
|-------|---------------------|---------|
| `1:1` | 1024 × 1024 | Social media posts, thumbnails, icons |
| `16:9` | 1408 × 768 | Website hero banners, slides, video thumbnails, desktop wallpapers |
| `9:16` | 768 × 1408 | Mobile backgrounds, Stories, Pinterest pins |
| `4:3` | 1280 × 960 | Slide decks, print materials, tablets |
| `3:4` | 960 × 1280 | Printed portraits, magazine covers, posters |

Default to `1:1` if the destination format is unknown.

---

## Crafting Effective Prompts

### Prompt Structure
Follow this order: **Subject → Setting → Style → Lighting → Composition → Mood → Quality**

Example:
> "Professional female architect in her 30s reviewing blueprints at a modern drafting table, contemporary open-plan office with floor-to-ceiling windows, commercial photography style, soft diffused natural light from the left, medium shot with shallow depth of field, confident and focused expression, 8K photorealistic"

### Subject
Be specific. State age range, attire, expression, and relevant props.

- Poor: "a businessperson at a desk"
- Better: "a mid-40s male executive in a charcoal suit reviewing a report at a glass desk in a modern corner office"

### Style Keywords
- **Photorealistic / commercial**: `commercial photography`, `advertising photography`, `photorealistic`, `hyperrealistic`
- **Corporate / clean**: `corporate photography`, `minimalist`, `modern aesthetic`, `clean background`
- **Lifestyle / authentic**: `lifestyle photography`, `candid moment`, `authentic`, `editorial`
- **Cinematic**: `cinematic lighting`, `film photography`, `anamorphic lens`

### Lighting Keywords
- **Safe / flattering**: `soft natural lighting`, `diffused daylight`, `professional headshot lighting`
- **Studio**: `professional studio lighting`, `softbox lighting`, `three-point lighting`
- **Atmospheric**: `golden hour`, `warm window light`, `overcast daylight`
- **Dramatic** (use sparingly for corporate): `Rembrandt lighting`, `high contrast`, `dramatic side lighting`

### Composition Keywords
- **Framing**: `rule of thirds`, `centered composition`, `symmetrical`, `environmental portrait`
- **Shot type**: `wide shot` (context), `medium shot` (professional), `close-up` (detail), `headshot`
- **Depth**: `shallow depth of field`, `bokeh background`, `sharp focus on subject`

### Mood Keywords
- **Professional**: `confident`, `authoritative`, `trustworthy`, `polished`, `purposeful`
- **Approachable**: `warm`, `friendly`, `authentic`, `candid`, `relatable`
- **Aspirational**: `forward-thinking`, `innovative`, `visionary`, `inspiring`
- **Modern/tech**: `sleek`, `contemporary`, `clean`, `minimal`

### Quality Boosters
Append to any prompt:
> `photorealistic, 8K resolution, sharp focus, professional grade, perfect exposure`

---

## Exclusions (fold into prompt text)

The MCP tool does not expose a separate negative prompt parameter. Embed exclusions directly in the prompt:
> `no watermarks, no text overlays, no cluttered background, no harsh shadows, no overexposure, no cartoon or illustration style`

---

## Output Handling

1. The tool returns **saved file paths** alongside the inline image data. Note every returned path.
2. **Copy** the generated file(s) into the task output folder using Bash:
   ```
   cp /path/to/generated/image.png /workspaces/AITeamBlueprint/work/AgentOutbox/[folder]/image.png
   ```
3. Record the final destination path of every image in the output report.

---

## Iteration Strategy

- For Imagen 3, generate 3–4 variants on the first call (`number_of_images: 3` or `4`), then pick the best.
- If all variants miss, adjust one variable at a time: lighting → composition → style.
- Keep core style descriptors identical across a batch for brand consistency.
- For Gemini 2.0 Flash, one image per call; iterate by rephrasing based on what the prior output got wrong.

---

## Common Professional Use Cases

### Website hero banner
> "Diverse team of four professionals collaborating around a bright conference table, modern glass-walled office, natural daylight from large windows, wide shot, warm and energetic atmosphere, editorial photography style, photorealistic, 8K"
- Aspect ratio: `16:9`

### Corporate headshot
> "Professional headshot of a confident woman in her late 30s, navy blazer, neutral grey background, soft studio lighting, slight bokeh, sharp focus on face, commercial photography, 8K"
- Aspect ratio: `3:4` or `1:1`

### Mobile campaign asset
> "Young professional checking her phone while walking through a sunlit urban street, lifestyle photography, golden hour warm tones, shallow depth of field, candid and aspirational mood, photorealistic, 8K"
- Aspect ratio: `9:16`
