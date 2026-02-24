# Deploy to GitHub Pages

## Prerequisites

- A GitHub repository (e.g. `https://github.com/kev1nnsays/thekevinchoi-website`)
- GitHub Pages enabled on the repository
- (Optional) A custom domain (e.g. `www.thekevinchoi.com`)

## How it works

The site is automatically built and deployed via GitHub Actions whenever you push to the `main` branch. The workflow is defined in `.github/workflows/deploy.yml`.

The workflow:
1. Checks out the repo (including Git LFS files)
2. Sets up Node.js 20 with npm cache
3. Installs dependencies with `npm ci`
4. Builds the site with `npm run build` (runs `astro check && astro build`)
5. Uploads the `dist/` directory as a GitHub Pages artifact
6. Deploys to GitHub Pages

## Initial setup on GitHub

1. Go to your repository on GitHub: `https://github.com/kev1nnsays/thekevinchoi-website`
2. Navigate to **Settings → Pages**
3. Under **Build and deployment → Source**, select **GitHub Actions**
4. Push to `main` — the workflow will trigger automatically
5. Your site will be live at `https://kev1nnsays.github.io/thekevinchoi-website/` (without custom domain) or your custom domain

## Custom domain setup (GoDaddy → GitHub Pages)

The site is configured to use `www.thekevinchoi.com` as the custom domain.

### 1. CNAME file

The file `public/CNAME` contains `www.thekevinchoi.com`. This gets copied to the build output automatically and tells GitHub Pages to serve the site on that domain.

### 2. GitHub Pages settings

1. Go to **Settings → Pages** in your GitHub repository
2. Under **Custom domain**, enter `www.thekevinchoi.com`
3. Check **Enforce HTTPS** (once DNS propagates and the certificate is issued)

### 3. GoDaddy DNS configuration

Log in to GoDaddy and go to **DNS Management** for `thekevinchoi.com`. Configure these records:

#### CNAME record (for `www` subdomain)

| Type  | Name | Value                       | TTL    |
|-------|------|-----------------------------|--------|
| CNAME | www  | kev1nnsays.github.io        | 1 Hour |

#### A records (for apex domain `thekevinchoi.com`)

Add these four A records pointing to GitHub Pages IP addresses:

| Type | Name | Value            | TTL    |
|------|------|------------------|--------|
| A    | @    | 185.199.108.153  | 1 Hour |
| A    | @    | 185.199.109.153  | 1 Hour |
| A    | @    | 185.199.110.153  | 1 Hour |
| A    | @    | 185.199.111.153  | 1 Hour |

> The A records ensure that `thekevinchoi.com` (without `www`) also resolves to GitHub Pages. GitHub will redirect it to `www.thekevinchoi.com` automatically.

#### Remove conflicting records

- Delete any existing A records for `@` that don't point to the GitHub IPs above
- Delete any "Parked" or forwarding records that GoDaddy may have set by default

### 4. Verify DNS propagation

After updating DNS records, it can take up to 48 hours to propagate (usually much faster). You can check with:

```bash
dig www.thekevinchoi.com +short
# Should return: kev1nnsays.github.io.

dig thekevinchoi.com +short
# Should return GitHub Pages IPs (185.199.108-111.153)
```

### 5. HTTPS certificate

GitHub Pages automatically provisions a free TLS certificate via Let's Encrypt. After DNS propagates:

1. Go to **Settings → Pages**
2. Check **Enforce HTTPS**
3. If the certificate isn't ready yet, wait a few minutes and try again

## Astro configuration

The `site` field in `astro.config.mjs` must match your custom domain:

```js
export default defineConfig({
  site: "https://www.thekevinchoi.com",
  // ...
});
```

This is used by the sitemap, RSS feed, and canonical URLs. If you're not using a custom domain, set it to `https://kev1nnsays.github.io/thekevinchoi-website`.

## Manual deploy trigger

You can also trigger a deploy manually without pushing code:

1. Go to **Actions** tab in your repository
2. Select **Deploy to GitHub Pages** workflow
3. Click **Run workflow → Run workflow**

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Check the Actions tab for error logs. Common cause: lockfile mismatch — run `npm install` locally and commit the updated `package-lock.json` |
| 404 on site | Ensure **Settings → Pages → Source** is set to **GitHub Actions** (not "Deploy from a branch") |
| Custom domain not working | Verify DNS records with `dig`. Ensure CNAME file contains `www.thekevinchoi.com` |
| HTTPS not available | Wait for DNS to fully propagate, then enable "Enforce HTTPS" in Pages settings |
| Images not loading | Ensure Git LFS is set up and files are pushed. The workflow checks out LFS files automatically |
