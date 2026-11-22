---
name: editorial-ig-photos
description: Generate aesthetically pleasing, IG-ready photorealistic photos (people, pets, hands holding objects, places) with Midjourney-level quality from Nano Banana, without the AI-slop look. One house-style prompt block (single visible light source, dark falloff, 50mm off-centre, Portra grade), the same subject kept across a post, and a vignette + grain finish done in code. Use when making photos for Instagram/TikTok posts, reels, carousels, story templates, app marketing or seeded content, or whenever generated photos "look like AI slop", "look fake", "aren't IG-ready". Not for candid iPhone/flash UGC (use last-summer-ugc-slides) or video (ugc-dance-video).
---

# Editorial IG photos

The approved look: photos that could run on a photographer's Instagram. Each has one subject, one beautiful visible light source, darkness everywhere else, a warm film grade and a calm off-centre frame. The user's verdict on the first batch made this way was "love the quality".

## Why it works

Midjourney's "quality" is a built-in house style: dramatic single-source light, shallow focus, a graded palette and deliberate framing. Nano Banana leaves all of that out by default and renders clean, evenly lit stock realism, which reads as AI slop. So you have to **write the house style out** in every prompt. Darkness also hides the backgrounds and props, which is where AI usually breaks.

These looks were rejected, so never use them:
- **Busy scenes:** clutter, messy tables, flea markets, many props.
- **Gritty "real":** grey flat light, mess, mud, lo-fi. The user's verdict: "aesthetically pleasing images not dirt shit photos".
- **Clean but flat editorial:** soft even daylight, white sheets, creamy but shadowless. It still reads as slop.
- **Glossy retouched "magazine" faces,** and the same AI woman repeated across posts.

## 1. Write each prompt in this order

```
A photograph for a beautiful Instagram feed, shot by a fine-art <pet|lifestyle|food|travel> photographer.
<SUBJECT with 2–4 fixed identifying details> <one action>, <gaze off the lens: looking to the side / back over the shoulder / eyes closed>.
<ONE visible light source> is the only light: <where it falls on the subject>, and <the rest> falls off into deep (warm) shadow.
50mm lens at f/1.8, <height/angle>, the subject off-centre with dark negative space <above/around>.
Warm highlights, cool deep shadows, Kodak Portra 400 colour, <quiet and cinematic | calm and intimate | gentle lens flare>.
Only the <subject>, nothing else in the frame. Natural <fur|skin> texture<, minimal retouching, not glossy>, a real photograph.
<Adults only.> No text, no logos, no watermark, no borders.
```

Good light sources, each named as "the only light":
- a low window shaft
- a single warm lamp just out of frame
- candles
- low sun behind the subject, giving rim light and backlit leaves or grass
- golden sun through a door's glass panel

Rules:
- **One subject per photo.** Allow at most one supporting prop: a lead, a blanket, a film camera.
- **Faces:** at most one clear face per post. Otherwise use profiles, backs, hands and over-the-shoulder looks. Never have the subject look into the lens.
- Use 85mm for running animals or tight portraits, and 50mm for everything else.
- Don't ask for grain or "film look" in the prompt. That's handled in step 3.

## 2. Generate (Sume MCP)

- Model: `google/nano-banana-2.1`, `aspect_ratio: "2:3"` (or `"4:5"` for a feed post), `resolution: "2K"`, `output_format: "jpeg"`. It costs about $0.06 per image.
- Text-only prompts were enough for the approved batch. Escalate only if a shot fails twice:
  - pass 2–3 already-approved photos as style references in `input_references` on `google/nano-banana-pro`
  - or try `openai/gpt-image-2.6` instead
- Send a whole post (or several posts, up to 12 requests) in one `generate_image_batch` with `max_spend_usd`, then a single `jobs_wait` with `include_results: true`.
- **Same subject across a post** (a pet, a person): repeat the identical identifying description word for word in every prompt. In the approved batch this kept the dog consistent across 4 shots. If it drifts, generate frame 0, then pass its Sume URL as `input_references` for the rest, starting the prompt with "Use the <dog/person> in the reference photo: keep exactly the same …".
- Download with `curl -s -o <name>.jpg <artifact url>`.

## 3. Finish in code, then review

```bash
python3 ~/.agents/skills/editorial-ig-photos/scripts/finish.py v1-*.jpg --inplace --sheet check.jpg
```

This adds a 13% vignette and fine midtone grain, then writes a contact sheet.

Read the contact sheet before showing anyone. Regenerate a shot (with a new idempotency key) if you see any of these:
- warped paws, hands or eyes
- text or a logo
- more than one subject or a cluttered background
- flat light where there should be one source
- a face looking into the lens, or glossy skin

Once the shots pass, show the user the images themselves (SendUserFile with `display: "render"`), not just a path.

## Proven prompts (approved 2026-11-22)

- **Pet, indoors:** "Pip, a small wire-haired terrier, grey and tan coat, one ear up and one ear folded, soft white chest patch, a neat beard, sits on a pale oak floor and tilts his head towards someone just out of frame, eyes catching the light. One low window to his left is the only light: a soft warm shaft falls across him and the floor, and the room behind falls off into deep warm shadow. 50mm lens at f/1.8, at his eye level, placed off-centre with dark negative space above."
- **Pet, golden hour:** "…trots through tall golden grass in a park at sunset, ears bouncing, mouth slightly open and happy, looking off to the side. The low sun behind him is the only light: a glowing golden rim around his fur, the grass backlit, the background melting into soft warm bokeh and darker trees. 85mm lens at f/1.8, at his eye level, the dog off-centre in the lower third."
- **Person:** "Hannah, 24, light brown hair in a loose low ponytail, a beige trench coat, walks alone down a park path carpeted in orange leaves, glancing back over her shoulder, not at the camera. The low autumn sun behind her is the only light: it rims her hair and coat in gold and makes the leaves in the trees glow, while the avenue ahead falls into soft warm shadow. 50mm lens at f/1.8, waist-up, she sits off-centre with the glowing trees as soft bokeh behind."
- **Place:** "A single wooden park bench under a huge yellow ginkgo tree… The late sun breaks through the tree from behind as the only light: the leaves glow like stained glass, a warm shaft falls across the bench, and the rest of the park sinks into deep soft shadow… Nothing else in the frame, no people."
- **Hands and object:** "A young woman's hand, short unpainted nails and a thin silver ring, holds a small silver point-and-shoot film camera up in front of golden autumn trees… The low sun from behind is the only light: it rims her fingers and the camera's edge with gold and a soft flare…"
- **Night, earlier approved pair:** candle-lit cake held in hands, and a woman blowing out candles in profile. "The candles are the only light: a warm glow on the hands and icing that falls off quickly to near black."
