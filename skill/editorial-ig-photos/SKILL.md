---
name: editorial-ig-photos
description: Generate aesthetically pleasing, IG-ready photorealistic photos (people, pets, hands holding objects, places) with Midjourney-level quality from Nano Banana, without the AI-slop look. Bright, glamorous lifestyle sets (party, city, ocean, travel) written per post as one story, the same cast kept across a post, and a vignette + grain finish done in code. Use when making photos for Instagram/TikTok posts, reels, carousels, story templates, app marketing or seeded content, or whenever generated photos "look like AI slop", "look fake", "aren't IG-ready". Not for candid iPhone/flash UGC (use last-summer-ugc-slides) or video (ugc-dance-video).
---

# Editorial IG photos

The approved look: glamorous, sunlit, aspirational photos that could run on a top lifestyle photographer's Instagram, each set telling one story. The user's verdict on the first batch made this way was "love the quality".

## Why it works

Midjourney's "quality" is a built-in house style: dramatic single-source light, shallow focus, a graded palette and deliberate framing. Nano Banana leaves all of that out by default and renders clean, evenly lit stock realism, which reads as AI slop. So you have to **write the house style out** in every prompt. Darkness also hides the backgrounds and props, which is where AI usually breaks.

These looks were rejected, so never use them:
- **Busy scenes:** clutter, messy tables, flea markets, many props.
- **Gritty "real":** grey flat light, mess, mud, lo-fi. The user's verdict: "aesthetically pleasing images not dirt shit photos".
- **Clean but flat editorial:** soft even daylight, white sheets, creamy but shadowless. It still reads as slop.
- **Glossy retouched "magazine" faces,** and the same AI woman repeated across posts.

## 1. Write each prompt in this order

**Default look: bright, glamorous, aspirational.** The photos showcase whatever they're for (a template, an app, a brand), so each post's set is one IG-worthy story: lifestyle, parties, the city centre, the ocean, travel, adventure. They're sunlit or golden hour by default, and night only for parties and city scenes, using flash and glowing city lights.

```
A photograph for a beautiful, aspirational Instagram feed, shot by a top lifestyle and fashion photographer.
<NAMED SUBJECT, age, 2–4 fixed details: hair, outfit, jewellery> <one glamorous action> in <a specific beautiful place>, <natural gaze: laughing with friends, looking out at the view, mid-step>.
<LIGHT: bright midday sun and blue sky | warm golden-hour sun from the side | direct on-camera flash with city lights glowing behind>.
<35mm for scenes, 50mm for people>, <framing>.
Vivid but natural colour, Kodak Portra 400, crisp, glamorous, effortless. Natural skin texture, not glossy, not posed at the lens.
Adults only. No text, no logos, no watermark, no borders.
```

Rules:
- **One location and one cast per post,** so the set reads as a story. Use the same named person or friends in every shot of the post (repeat the description word for word), and a different cast in every post.
- **Pick each shot for what it showcases.** A party template gets the party, a magazine template gets a cover-worthy portrait, a travel template gets the ocean.
- The **"one visible light source + dark falloff"** look (the d02c candle shots) is a variant for candle or night-intimate moments only. **Never apply it to a whole batch.** In 2026-11 it turned 400 photos gloomy and grungy, and they were rejected and wasted.
- Don't ask for grain or "film look" in the prompt. That's handled in step 3.
- **Never bulk-wrap someone's old briefs in a style block.** Write each post's set yourself, and show a 2-post pilot before any run over ~20 images.

## People: faces and eyes (the hardest part)

AI eyes are the number-one giveaway. What was learned on 2026-11-22, after many rejected rounds:

- **The cause is small faces.** A group of 4–5 people at mid-distance gives each face a few dozen pixels, and every model (NB 2.1, NB Pro, GPT Image 2.6, Soul) draws glassy, cloned eyes at that size. No eye wording fixes it: "squinting, laugh lines, little makeup" was rejected, sunglasses were rejected ("glasses doesn't solve the eye problem"), and GPT Image 2.6's look was rejected as slop.
- **What passed:** **one person, face large in frame, on `google/nano-banana-pro`**, with **one named key light at ~45°** that casts a soft shadow under the brow and eyes, natural catchlights from that light, realistic eye reflections, detailed irises, slightly uneven lids mid-laugh, gaze past the camera, real skin (pores, peach fuzz, a few freckles, light natural makeup), 85mm at f/2, and focus on the eyes. Call her "a real girl, not a model".
- **Cast: women in their early 20s** (21–23), with girlfriends and not mixed groups or older people. Give every person her own hair, skin tone, outfit and jewellery, and a name. Avoid the name "Maya".
- **Two people at most with visible faces per photo.** Group moments (toasts, dinners, dance floors) become close shots of hands and props: write the prompt about the hands, glasses and table only, and don't describe the people at all. NB Pro ignores "crop at the lips" and draws full, cloned faces if you describe the women.
- Products in hand pick up brand logos ("Aperol Spritz" appeared on a glass). Say "an unbranded glass" and check every shot for text.

## 2. Generate (Sume MCP)

- Model: `google/nano-banana-pro` for any shot with a visible face; `google/nano-banana-2.1` for places, food, hands and objects. Both take `aspect_ratio: "2:3"` (or `"4:5"` for a feed post), `resolution: "2K"`, `output_format: "jpeg"`. NB 2.1 is about $0.06 per image; check Pro's price with `estimate_image_cost`.
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

- **Woman, glam portrait (NB Pro, the eye fix):** "A real photograph for an aspirational Instagram feed, shot by a professional lifestyle photographer. Sienna, 22, a real girl not a model: long dark-blonde beach waves with flyaways, a few freckles across her nose, light natural makeup, thin gold necklace, black slip dress, leaning on the glass railing of a rooftop bar at sunset with an unbranded spritz in her hand, laughing at something a friend just said off to the side, her eyes looking past the camera. The low sun is the key light, about 45 degrees to her left: warm light across her face, a soft natural shadow under her brow and eyes, small natural catchlights from the sun, realistic eye reflections, detailed irises, slightly uneven lids from the laugh. A glittering city skyline softly out of focus behind her. 85mm lens at f/2, head and shoulders, sharp focus on her eyes. Real skin texture with visible pores, peach fuzz on her cheek, natural hair texture. Kodak Portra 400 colour. No text, no logos, no watermark, no borders."

- **Pet, indoors:** "Pip, a small wire-haired terrier, grey and tan coat, one ear up and one ear folded, soft white chest patch, a neat beard, sits on a pale oak floor and tilts his head towards someone just out of frame, eyes catching the light. One low window to his left is the only light: a soft warm shaft falls across him and the floor, and the room behind falls off into deep warm shadow. 50mm lens at f/1.8, at his eye level, placed off-centre with dark negative space above."
- **Pet, golden hour:** "…trots through tall golden grass in a park at sunset, ears bouncing, mouth slightly open and happy, looking off to the side. The low sun behind him is the only light: a glowing golden rim around his fur, the grass backlit, the background melting into soft warm bokeh and darker trees. 85mm lens at f/1.8, at his eye level, the dog off-centre in the lower third."
- **Person:** "Hannah, 24, light brown hair in a loose low ponytail, a beige trench coat, walks alone down a park path carpeted in orange leaves, glancing back over her shoulder, not at the camera. The low autumn sun behind her is the only light: it rims her hair and coat in gold and makes the leaves in the trees glow, while the avenue ahead falls into soft warm shadow. 50mm lens at f/1.8, waist-up, she sits off-centre with the glowing trees as soft bokeh behind."
- **Place:** "A single wooden park bench under a huge yellow ginkgo tree… The late sun breaks through the tree from behind as the only light: the leaves glow like stained glass, a warm shaft falls across the bench, and the rest of the park sinks into deep soft shadow… Nothing else in the frame, no people."
- **Hands and object:** "A young woman's hand, short unpainted nails and a thin silver ring, holds a small silver point-and-shoot film camera up in front of golden autumn trees… The low sun from behind is the only light: it rims her fingers and the camera's edge with gold and a soft flare…"
- **Night, earlier approved pair:** candle-lit cake held in hands, and a woman blowing out candles in profile. "The candles are the only light: a warm glow on the hands and icing that falls off quickly to near black."
