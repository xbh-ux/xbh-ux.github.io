# DESIGN.md

> 让内容像 Apple 的产品页面一样安静、清晰、精确，但始终服务于中文长文阅读。

## 1. Visual Theme & Atmosphere

**Style**: Apple-inspired editorial minimalism
**Keywords**: 克制、留白、精确、灰阶、轻盈、易读、响应式
**Tone**: 现代且安静，不做营销式夸张，不模仿 Apple 商标或产品素材。
**Feel**: 像在一块校准良好的浅灰屏幕上阅读排版精良的个人笔记。

**Interaction Tier**: L1 精致静态
**Dependencies**: CSS only

## 2. Color Palette & Roles

```css
:root {
  --apple-bg: #f5f5f7;
  --apple-surface: #ffffff;
  --apple-surface-alt: #fbfbfd;
  --apple-surface-hover: #f0f0f2;
  --apple-border: #d2d2d7;
  --apple-border-hover: #a1a1a6;
  --apple-text: #1d1d1f;
  --apple-text-secondary: #515154;
  --apple-text-tertiary: #86868b;
  --apple-accent: #0066cc;
  --apple-accent-hover: #004f9e;
  --apple-bg-rgb: 245, 245, 247;
  --apple-surface-rgb: 255, 255, 255;
  --apple-text-rgb: 29, 29, 31;
  --apple-accent-rgb: 0, 102, 204;
  --apple-success: #248a3d;
  --apple-error: #d70015;
  --apple-warning: #b25000;
}

:root[data-scheme="dark"] {
  --apple-bg: #000000;
  --apple-surface: #1c1c1e;
  --apple-surface-alt: #2c2c2e;
  --apple-surface-hover: #3a3a3c;
  --apple-border: #38383a;
  --apple-border-hover: #636366;
  --apple-text: #f5f5f7;
  --apple-text-secondary: #d2d2d7;
  --apple-text-tertiary: #98989d;
  --apple-accent: #2997ff;
  --apple-accent-hover: #64b5ff;
  --apple-bg-rgb: 0, 0, 0;
  --apple-surface-rgb: 28, 28, 30;
  --apple-text-rgb: 245, 245, 247;
  --apple-accent-rgb: 41, 151, 255;
}
```

Color rules: all custom colors use variables; blue is reserved for links, focus and active states; cards use surface contrast before shadows; dark mode retains neutral grays.

## 3. Typography Rules

No external font request. Use the operating system's Apple-compatible font stack.

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|---|---|---:|---:|---:|---:|
| Page H1 | SF Pro Display / PingFang SC / system | 40px | 600 | 1.2 | 0 |
| Article H1 | SF Pro Display / PingFang SC / system | 36px | 600 | 1.25 | 0 |
| H2 | SF Pro Display / PingFang SC / system | 28px | 600 | 1.25 | 0 |
| H3 | SF Pro Text / PingFang SC / system | 22px | 600 | 1.35 | 0 |
| Body | SF Pro Text / PingFang SC / system | 17px | 400 | 1.75 | 0 |
| Label | SF Pro Text / PingFang SC / system | 14px | 500 | 1.5 | 0 |
| Code | SFMono-Regular / monospace | 14px | 400 | 1.7 | 0 |

Use `-apple-system`, `BlinkMacSystemFont`, `PingFang SC`, `Segoe UI`, and `Microsoft YaHei` as local fallbacks. Never use decorative script, condensed display faces, negative letter spacing, or weights above 700. Headings and body text have no gradient or text shadow.

## 4. Component Stylings

```css
.button {
  min-height: 44px; padding: 0 18px; border: 0; border-radius: 999px;
  color: var(--apple-surface); background: var(--apple-accent);
  transition: background-color .18s ease, transform .18s ease;
}
.button:hover { background: var(--apple-accent-hover); }
.button:active { transform: scale(.98); }
.button:focus-visible { outline: 3px solid rgba(var(--apple-accent-rgb), .35); outline-offset: 2px; }
.button:disabled { opacity: .45; cursor: not-allowed; }

.article-card {
  background: var(--apple-surface); border: 1px solid transparent;
  border-radius: 12px; transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.article-card:hover { transform: translateY(-2px); border-color: var(--apple-border); box-shadow: 0 12px 32px rgba(var(--apple-text-rgb), .07); }
.article-card:focus-within { outline: 3px solid rgba(var(--apple-accent-rgb), .28); outline-offset: 2px; }

.site-nav { background: rgba(var(--apple-surface-rgb), .82); border-bottom: 1px solid var(--apple-border); }
.site-nav a:hover, .site-nav a[aria-current="page"] { color: var(--apple-accent); }
.site-nav a:focus-visible { outline: 3px solid rgba(var(--apple-accent-rgb), .3); outline-offset: 3px; border-radius: 8px; }

a { color: var(--apple-accent); text-underline-offset: .2em; }
a:hover { color: var(--apple-accent-hover); text-decoration-thickness: 2px; }
a:focus-visible { outline: 3px solid rgba(var(--apple-accent-rgb), .3); outline-offset: 3px; border-radius: 4px; }

.tag { padding: 5px 10px; border-radius: 999px; color: var(--apple-text-secondary); background: var(--apple-surface-hover); }
.tag:hover { color: var(--apple-accent); }
```

Search inputs use an 11px radius, visible focus ring, and a 44px minimum height. Code blocks have no surrounding box; a subtle left rule separates them from body text while preserving horizontal scrolling.

## 5. Layout Principles

- Site container: maximum 1180px, horizontal padding 24px desktop and 18px mobile.
- Reading column: maximum 720px; article body remains left aligned.
- Section spacing: 64px desktop, 40px mobile.
- Component gap: 24px desktop, 16px mobile.
- Card padding: 24px desktop, 20px mobile.
- Grid: one primary content column plus optional 280px sidebar; article lists use a single readable column.

```css
.apple-grid { display: grid; grid-template-columns: minmax(0, 1fr) 280px; gap: 32px; }
```

## 6. Depth & Elevation

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow | page bands and article body |
| Subtle | `0 1px 3px rgba(var(--apple-text-rgb), .05)` | static cards |
| Elevated | `0 12px 32px rgba(var(--apple-text-rgb), .07)` | hover and floating search |
| Focus | 3px translucent accent ring | keyboard focus |

Depth comes mainly from gray surface changes. Never nest cards or stack multiple shadows.

## 7. Animation & Interaction

Motion is short, quiet and limited to opacity and transform. No JavaScript animation dependency.

```css
@keyframes apple-fade-in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}
.main-container { animation: apple-fade-in .35s ease-out both; }
a, button, .article-card { transition-duration: .18s; transition-timing-function: ease; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; scroll-behavior: auto !important; transition-duration: .01ms !important; }
}
```

## 8. Do's and Don'ts

### Do

- Prioritize reading width and Chinese line height.
- Use one blue accent only for interaction.
- Use neutral surfaces to establish hierarchy.
- Keep touch targets at least 44px.
- Preserve Stack's accessible navigation and semantic templates.

### Don't

- Do not copy Apple logos, product photography or branded copy.
- Do not use gradients, decorative blobs or glass panels as page backgrounds.
- Do not use negative letter spacing.
- Do not use oversized landing-page typography for article cards.
- Do not place cards inside cards.
- Do not use more than 12px card radius except pills.
- Do not add heavy shadows, parallax or scroll-jacking.
- Do not animate layout properties or ignore reduced-motion preferences.

## 9. Responsive Behavior

| Name | Width | Key Changes |
|---|---:|---|
| Desktop | > 1024px | content plus optional sidebar, 24px gutters |
| Tablet | 601-1024px | reduced sidebar, tighter gaps |
| Mobile | <= 600px | one column, 18px gutters, 44px controls |

Navigation follows Stack's mobile drawer. Cards become full width, metadata wraps, media never exceeds its container, and no element may create horizontal overflow.

```css
@media (max-width: 600px) {
  .apple-grid { grid-template-columns: 1fr; gap: 16px; }
  .main-container { padding-inline: 18px; }
  h1 { font-size: 32px; }
  button, .menu a { min-height: 44px; }
}
```
