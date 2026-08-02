import os
import sys
import json
from datetime import datetime

def generate_blog_post(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    title = data['title']
    filename = data['filename']
    description = data['description']
    content_html = data['content_html']

    base_dir = r"C:\Users\sevii\projects\RI-Projects\ri-dogtraining-site"
    file_path = os.path.join(base_dir, filename)

    # HTML Template for Blog Post
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Rogue Intelligence Dog Training</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="https://ri-dogtraining.com/{filename}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta name="author" content="Rogue Intelligence Dog Training" />
  <meta name="theme-color" content="#0b0a09" />
  <link rel="icon" type="image/png" href="/favicon-32.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&amp;family=Azeret+Mono:wght@400;500&amp;family=Inter:wght@400;500;600;700&amp;display=swap" />
  <link rel="stylesheet" href="/styles.css" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Rogue Intelligence Dog Training" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:url" content="https://ri-dogtraining.com/{filename}" />
  <meta property="og:title" content="{title} | Rogue Intelligence Dog Training" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="https://ri-dogtraining.com/ri-banner.png" />
  <meta name="twitter:card" content="summary_large_image" />
  
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "@id": "https://ri-dogtraining.com/{filename}#webpage",
      "url": "https://ri-dogtraining.com/{filename}",
      "name": "{title}",
      "isPartOf": {{
        "@id": "https://ri-dogtraining.com/#website"
      }},
      "inLanguage": "en-US"
    }},
    {{
      "@type": "Article",
      "@id": "https://ri-dogtraining.com/{filename}#article",
      "headline": "{title}",
      "description": "{description}",
      "author": {{
        "@type": "Organization",
        "name": "Rogue Intelligence Dog Training",
        "@id": "https://ri-dogtraining.com/#business"
      }},
      "publisher": {{
        "@id": "https://ri-dogtraining.com/#business"
      }},
      "isPartOf": {{
        "@id": "https://ri-dogtraining.com/{filename}#webpage"
      }},
      "mainEntityOfPage": {{
        "@id": "https://ri-dogtraining.com/{filename}#webpage"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://ri-dogtraining.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Guides",
          "item": "https://ri-dogtraining.com/guides.html"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{title}",
          "item": "https://ri-dogtraining.com/{filename}"
        }}
      ]
    }}
  ]
}}
  </script>
</head>
<body>
  <a href="#main-content" class="skip-link" style="position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); border:0;">Skip to main content</a>
  <nav>
    <a class="wordmark" href="/" aria-label="Rogue Intelligence Dog Training — home">
      <span class="wordmark-plate" aria-hidden="true"><span>RI</span></span>
      <span class="wordmark-lines">
        <span class="wordmark-name">ROGUE<i>&bull;</i>INTELLIGENCE</span>
        <span class="wordmark-sub">DOG TRAINING &middot; CHANDLER AZ</span>
      </span>
    </a>
    <ul class="nav-links">
      <li><a href="/#board-train">Board &amp; Train</a></li>
      <li><a href="/#lessons">Lessons</a></li>
      <li><a href="/#areas">Areas</a></li>
      <li><a href="/guides.html">Guides</a></li>
      <li><a href="/#faq">FAQ</a></li>
      <li><a href="/#contact">Contact</a></li>
      <li class="nav-login"><a href="https://app.ri-dogtraining.com">Client Login</a></li>
      <li class="nav-mobile-cta"><a href="/#contact">Book Now</a></li>
    </ul>
    <a href="/#contact" class="nav-cta">Book Now</a>
    <button class="nav-toggle" id="nav-toggle" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button>
  </nav>

  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol><li><a href="/">Home</a></li><li><a href="/guides.html">Guides</a></li><li>{title}</li></ol>
  </nav>

  <main id="main-content">
  <header class="page-hero">
    <div class="container">
      <div class="eyebrow"><div class="eyebrow-bar"></div><span>Dog Training Blog &middot; Chandler, AZ</span></div>
      <h1>{title}</h1>
      <p class="lede">{description}</p>
      <div class="hero-actions" style="margin-top:32px;">
        <a href="/#board-train" class="btn btn-primary">See Programs &amp; Pricing</a>
        <a href="/guides.html" class="btn btn-ghost">Back to Guides</a>
      </div>
    </div>
  </header>

  <section class="section" style="padding-top:48px;">
    <div class="container">
      <div class="prose">
{content_html}
      </div>
    </div>
  </section>
  </main>

  <footer>
    <div class="footer-bottom">
      <div class="footer-copy">
        <span itemscope itemtype="https://schema.org/LocalBusiness">
          <strong itemprop="name">Rogue Intelligence Dog Training</strong> —
          <span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"><span itemprop="addressLocality">Chandler</span>, <span itemprop="addressRegion">AZ</span></span> ·
          Veteran-Owned Dog Trainer · Serving the greater Phoenix Valley
        </span><br>&copy; 2026 Rogue Intelligence Dog Training &mdash; All Rights Reserved
      </div>
      <ul class="footer-links">
        <li><a href="mailto:Info@ri-dogtraining.com">Email</a></li>
        <li><a href="tel:4802690530">(480) 269-0530</a></li>
        <li><a href="https://instagram.com/ri_dogtraining" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
    </div>
  </footer>

  <script>
    (function(){{var t=document.getElementById("nav-toggle"),l=document.querySelector(".nav-links");
    if(t&&l){{t.addEventListener("click",function(){{var o=l.classList.toggle("open");t.setAttribute("aria-expanded",o?"true":"false");}});}}}}();
  </script>
</body>
</html>"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template)

    # 2. Update guides.html
    guides_path = os.path.join(base_dir, "guides.html")
    with open(guides_path, "r", encoding="utf-8") as f:
        guides_content = f.read()

    # Find the injection point: <h2>Articles</h2>\n<ul>
    injection_point = "<h2>Articles</h2>\n<ul>\n"
    new_link = f'<li><a href="/{filename}"><strong>{title}</strong></a> &mdash; {description}</li>\n'
    
    if injection_point in guides_content:
        # Don't add if already exists
        if f'href="/{filename}"' not in guides_content:
            guides_content = guides_content.replace(injection_point, injection_point + new_link)
            with open(guides_path, "w", encoding="utf-8") as f:
                f.write(guides_content)
            print(f"Added {filename} to guides.html")
        else:
            print(f"{filename} already exists in guides.html")
    else:
        print("Could not find the injection point in guides.html")

    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_blog_post.py <path_to_json>")
        sys.exit(1)
    generate_blog_post(sys.argv[1])
