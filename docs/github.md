# Deploy with GitHub and GitHub Pages

This project can be deployed with GitHub Actions to GitHub Pages. The steps below cover both user/organization pages and project pages.

## 1) Enable GitHub Pages

1. Push this repository to GitHub.
2. In GitHub, go to Settings -> Pages.
3. Under Build and deployment, set Source to GitHub Actions.

## 2) Add the GitHub Actions workflow

Create .github/workflows/deploy.yml with the following content:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    runs-on: ubuntu-latest
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## 3) Configure Astro for GitHub Pages

If you are deploying a project page (https://username.github.io/repo-name), set a base path. Update [astro.config.mjs](../astro.config.mjs) like this:

```js
export default defineConfig({
  site: "https://username.github.io/repo-name",
  base: "/repo-name",
  integrations: [mdx(), sitemap(), tailwind()],
});
```

If you are deploying a user or organization page (https://username.github.io), keep base unset and set site to the root URL.

## 4) Custom domain (optional)

If you use a custom domain, add a CNAME file in public/CNAME with your domain:

```
example.com
```

Then set site to the custom domain in [astro.config.mjs](../astro.config.mjs).

## 5) First deployment

Push to main. GitHub Actions will build and deploy the site. The Pages URL will appear in the Actions summary and in Settings -> Pages.
