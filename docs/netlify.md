# Deploy to Netlify

## Option A: Deploy from Git (recommended)

1. Push this repository to GitHub, GitLab, or Bitbucket.
2. In Netlify, click New site from Git and select your repository.
3. Configure the build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. Click Deploy site.

## Option B: Drag-and-drop deploy

1. Build the site locally:
   - `npm install`
   - `npm run build`
2. In Netlify, go to Sites and drag the `dist` folder into the deploy area.

## Optional settings

- If you use a custom domain, add it under Domain management.
- If you use environment variables later, add them under Site settings → Environment variables.
