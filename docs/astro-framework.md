# Astro framework

## Overview
This site is built with AstroSphere as a static Astro theme. Astro renders pages at build time and only ships client-side JavaScript where explicitly requested (islands).

## Key locations
- Site config: [astro.config.mjs](../astro.config.mjs)
- Global metadata and nav: [src/consts.ts](../src/consts.ts)
- Pages: [src/pages](../src/pages)
- Layouts: [src/layouts](../src/layouts)
- Components: [src/components](../src/components)
- Content collections: [src/content](../src/content)

## Content workflow
Content is managed with Astro content collections, defined in [src/content/config.ts](../src/content/config.ts). Blog posts and projects live under [src/content/blog](../src/content/blog) and [src/content/projects](../src/content/projects).

## Static build
Astro builds a fully static site by default for deployment to Netlify. Client-side JavaScript is only included where you use directives like `client:load` in components.

## Local development
Use the package scripts in [package.json](../package.json) to run dev server and build. See the README for the exact commands.