---
name: image-gen
description: Generate and edit images via Nano Banana MCP and Gemini, with brand-aware prompting for JEDS and Savage Investments visual identities. Includes quality anchors for different use cases.
allowed-tools: Read, Write, Grep, Glob, Bash
argument-hint: "[use-case] [subject] — e.g. 'site rendering Shakes Run aerial view', 'social media JEDS project highlight', 'investor materials Savage portfolio overview'"
---

# Image-Gen — Brand-Aware Image Generation

## Trigger Phrases
- "generate an image"
- "create a graphic"
- "image-gen"
- "make a rendering"
- "create a visual"
- "design a graphic for"

## Purpose

Image-Gen produces brand-consistent images for JEDS Engineering Solutions and Savage Investments using AI image generation (Nano Banana MCP + Gemini). It loads brand context, builds optimized prompts, and applies quality standards appropriate to the use case. Every image it generates aligns with the correct brand identity and meets the quality bar for its intended audience.

## Prerequisites

- **Nano Banana MCP** must be configured and accessible
- If Nano Banana MCP is not available, this skill will:
  1. Generate the detailed prompt for manual use with any image generation tool
  2. Specify the exact parameters (size, style, quality settings)
  3. Provide the brand color palette for reference

## Execution Phases

### Phase 1: Brand Context Loading

Determine which brand identity applies:

#### JEDS Engineering Solutions Brand
| Element | Value |
|---------|-------|
| **Primary Color** | Gold #D4AF37 |
| **Secondary Color** | Dark Green #2D5016 |
| **Accent Color** | Cream #F5F0E1 |
| **Text on Dark** | White #FFFFFF |
| **Typography Feel** | Professional, engineering, precise |
| **Visual Style** | Clean, technical, authoritative, grounded |
| **Logo Elements** | JEDS wordmark, clean geometric forms |
| **Photography Style** | Aerial site photos, construction progress, finished infrastructure |
| **Avoid** | Cartoonish, overly artistic, abstract, clip art |

#### Savage Investments Brand
| Element | Value |
|---------|-------|
| **Primary Color** | Beige/Warm Neutral #C8B89A |
| **Secondary Color** | Metallic Gold #B8960F |
| **Accent Color** | Deep Charcoal #2C2C2C |
| **Text on Dark** | Warm White #F5F0E1 |
| **Typography Feel** | Sophisticated, luxury, investment-grade |
| **Visual Style** | Premium, refined, high-contrast, editorial |
| **Logo Elements** | SI monogram, serif typography |
| **Photography Style** | Real estate portfolio, aerial property views, luxury finishes |
| **Avoid** | Casual, playful, overly technical, engineering-focused |

**Brand Selection Logic:**
1. If the subject involves real estate, investment, portfolio, or property development --> Savage Investments
2. If the subject involves engineering, civil design, construction, or agency submittals --> JEDS
3. If ambiguous, ask the user
4. If neither brand applies, use a neutral professional style

### Phase 2: Prompt Engineering

Build the image generation prompt with these components:

1. **Subject Description** — what is depicted, with specific details
2. **Composition** — camera angle, framing, focal point
3. **Style Directives** — rendering style, level of realism
4. **Color Palette** — brand colors integrated naturally
5. **Mood/Atmosphere** — lighting, time of day, weather, feeling
6. **Technical Specs** — aspect ratio, resolution tier
7. **Negative Prompts** — what to exclude

**Prompt Template:**
```
[Subject with specific details]. [Composition and camera angle].
[Style: photorealistic/architectural rendering/infographic/etc.].
Color palette featuring [brand colors described naturally, not as hex codes].
[Mood: lighting, atmosphere]. [Aspect ratio and quality].
Avoid: [negative prompts, brand-specific exclusions].
```

### Phase 3: Quality Anchors

Apply the appropriate quality standard based on use case:

| Use Case | Aspect Ratio | Style | Quality Bar | Brand |
|----------|-------------|-------|-------------|-------|
| **Site Rendering** | 16:9 landscape | Photorealistic architectural visualization | High — accurate to site conditions, professional grade | JEDS |
| **Presentation Board** | 16:9 or 4:3 | Clean infographic with photo elements | High — polished, consistent with slide deck | JEDS or Savage |
| **Client Proposal** | Various | Professional, understated, confidence-building | High — must not look AI-generated or cheap | JEDS |
| **Social Media** | 1:1 or 4:5 | Eye-catching, branded, shareable | Medium — authentic feel, not stock-photo generic | JEDS or Savage |
| **Investor Materials** | 16:9 or letter | Premium, editorial, luxury feel | Very High — must feel investment-grade | Savage |
| **Concept Sketch** | Various | Hand-drawn or watercolor feel, exploratory | Medium — intentionally informal, ideation stage | JEDS |
| **Construction Documentation** | Various | Technical, clear, annotated | Medium — clarity over aesthetics | JEDS |
| **Marketing Collateral** | Various | On-brand, polished, versatile | High — consistent with other brand materials | Either |

### Phase 4: Generation

1. **Build the final prompt** combining all elements from Phases 1-3.
2. **Set parameters:**
   - Resolution/size appropriate to use case
   - Style/model settings for the target aesthetic
   - Number of variations (default: 2-3 options)
3. **Execute generation** via Nano Banana MCP or prepare the prompt for manual execution.
4. **Review output** against quality anchors.

### Phase 5: Delivery

1. **Present the generated images** with:
   - The prompt used (for reproducibility)
   - Which brand identity was applied
   - Quality anchor assessment
   - Suggested usage context
2. **Offer refinements:**
   - "Want me to adjust the composition?"
   - "Should I try a different style?"
   - "Need a different aspect ratio?"
3. **Save the prompt** if it's reusable (suggest adding to a prompt library).

## Prompt Engineering Best Practices

### Do
- Describe colors by appearance, not hex codes ("warm gold accents," not "#D4AF37")
- Specify camera angle and distance ("aerial view at 45 degrees," "eye-level close-up")
- Include environmental context ("overcast Kentucky sky," "late afternoon golden hour")
- Reference real-world materials and textures ("limestone retaining wall," "fresh asphalt")
- Describe the feeling ("conveys stability and precision," "feels premium and exclusive")

### Avoid
- Vague descriptions ("nice building," "good-looking site")
- Conflicting styles ("photorealistic watercolor")
- Over-specification (too many details crowd out the main subject)
- Text in images (AI-generated text is unreliable — add text in post-processing)
- Copyrighted elements (specific brand logos, trademarked designs, named architects' styles)

## Rules

- **Always load brand context first.** Never generate without determining which brand applies.
- **Never include text in generated images.** AI text rendering is unreliable. Overlay text in post-processing.
- **Always provide the prompt** alongside the image for reproducibility.
- **Quality must match use case.** Don't over-invest in a concept sketch; don't under-invest in investor materials.
- **Disclose AI generation** when appropriate. For client-facing materials, note that renderings are AI-generated concept visualizations if there's any risk of confusion with actual photography.
- **Save successful prompts.** If a prompt produces great results, suggest storing it for reuse.
- **Respect copyright.** Never attempt to replicate a specific artist's style, copy trademarked imagery, or generate images of real identifiable people.

## Output Format

```
## Image Generation: [Subject]

### Brand Context
- **Brand:** [JEDS / Savage Investments / Neutral]
- **Use Case:** [from quality anchors table]
- **Quality Bar:** [from quality anchors table]

### Prompt
```
[The full generation prompt]
```

### Parameters
- **Aspect Ratio:** [ratio]
- **Style:** [style name]
- **Variations:** [number generated]

### Generated Images
[Images or file paths]

### Quality Assessment
- Matches brand identity: [Yes/No + notes]
- Meets quality bar for use case: [Yes/No + notes]
- Composition and subject accuracy: [assessment]

### Refinement Options
- [Suggested adjustments if quality bar not fully met]
```
