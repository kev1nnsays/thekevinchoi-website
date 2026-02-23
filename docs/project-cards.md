# Project cards with graphics

## Overview
Project cards are rendered for the Projects page and other lists. Each project can define a static image graphic that shows on the card.

## Data model
Projects are content entries in [src/content/projects](../src/content/projects). The schema includes an optional `image` field:
- Schema: [src/content/config.ts](../src/content/config.ts)
- Example frontmatter: [src/content/projects/project-1/index.md](../src/content/projects/project-1/index.md)

Frontmatter example:
```
image: "/images/projects/placeholder.svg"
```

Images should be placed in [public/images/projects](../public/images/projects) so they can be referenced by URL.

## Rendering
Cards use the shared component:
- Card component: [src/components/ArrowCard.tsx](../src/components/ArrowCard.tsx)

When `image` is set on a project, the card renders a thumbnail next to the text. If `image` is missing, the card stays text-only.

## Updating a project image
1. Add your image to [public/images/projects](../public/images/projects).
2. Add or update the `image` field in the project frontmatter.
3. The Projects page will reflect the update automatically.
