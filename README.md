# Testimonial Generator — Department of Physics, Jagannath University

A lightweight, fully client-side web app for producing **print-ready B.Sc / M.Sc testimonials**. Faculty fill in a short form and download a **true vector PDF** — the text is stamped directly onto the official certificate template (no images, no blur, small file size).

Everything runs in the browser. There is **no backend, no build step, and no internet requirement** once the files are in place — it even works by double-clicking `index.html`.

---

## Features

- **Vector output** — real, selectable text drawn onto the original certificate PDF. Sharp at any zoom; typical file size ~230 KB (vs. ~1 MB for the old image-based version).
- **Two programs** — separate, pixel-tuned layouts for B.Sc and M.Sc.
- **Custom fonts embedded** — student/parent names render in a calligraphy script; all filled-in values are bold.
- **Offline & self-contained** — the templates and font are embedded as base64 in `assets.js`; the PDF libraries are vendored locally. No CDN, no server needed.
- **Keyboard friendly** — `↑` / `↓` / `Enter` move between fields; `Enter` on the last field downloads.
- **Preview or Download** — open the PDF in a new tab, or save it named after the Student ID.

---

## Usage

1. Open **`index.html`**.
2. Choose **Bachelor of Science** or **Master of Science**.
3. Fill in the fields (Sl No, Name, Father's/Mother's Name, Student ID, Registration No, Session, Exam Year, Held In, CGPA, Letter Grade, Date).
4. Click **Download PDF** (saved as `<StudentID>.pdf`) or **Preview** to view first.

Empty fields are simply left blank on the certificate.

---

## Files

**Required to run the site:**

| File | Purpose |
|------|---------|
| `index.html` | Landing page — choose the degree |
| `form.html` | The generator form (reads `?degree=bsc` / `?degree=msc`) |
| `assets.js` | Base64-embedded certificate templates + calligraphy font |
| `pdf-lib.min.js` | PDF creation/editing library (local) |
| `fontkit.umd.min.js` | Custom-font embedding for pdf-lib (local) |
| `logo.png` | University crest shown in the UI |

**Source files (only needed to regenerate `assets.js`):**

- `BSc Certificate.pdf`, `MSc Certificate.pdf` — the certificate templates
- `calligrafy.ttf` — the name font
- other `.ttf`/`.TTF` files — currently unused

---

## Hosting on GitHub Pages

The app is 100% static, so GitHub Pages works out of the box:

1. Upload the files to a repository (**use a repo name without spaces**, e.g. `physics-testimonial`).
2. **Settings → Pages → Build and deployment → Deploy from a branch** → select your branch and `/ (root)`.
3. The site will be available at `https://<username>.github.io/<repo>/`.

> After updating `assets.js`, do a hard refresh (`Ctrl` + `F5`) since browsers cache it.

---

## Updating templates or the font

The templates and font are embedded in `assets.js`. If you change a certificate PDF or the name font, regenerate that file with Python:

```python
import base64

def b64(fn):
    with open(fn, "rb") as f:
        return base64.b64encode(f.read()).decode()

bsc  = b64("BSc Certificate.pdf")
msc  = b64("MSc Certificate.pdf")
font = b64("calligrafy.ttf")

with open("assets.js", "w", encoding="utf-8") as f:
    f.write("window.BSC_TEMPLATE_PDF_B64=" + repr(bsc).replace("'", '"') + ";\n")
    f.write("window.MSC_TEMPLATE_PDF_B64=" + repr(msc).replace("'", '"') + ";\n")
    f.write("window.CALLIG_FONT_B64="      + repr(font).replace("'", '"') + ";\n")
```

### Adjusting text placement

Text positions live in the `CONFIGS` object inside `form.html`, one entry per degree. Coordinates are in **PDF points** on a `792 × 612` page with the origin at the **bottom-left** (`y` is the text baseline):

- `align: 'center'` → `cx` is the horizontal center of the value.
- `align: 'left'` → `x` is the start of the value.
- `font: 'callig'` → calligraphy name font (faux-bolded); `font: 'data'` → Times Bold Italic.

Raise `y` to move a value up, lower it to move down; change `cx`/`x` to shift left/right.

---

## How it works

`form.html` loads the correct base64 template, embeds `calligrafy.ttf` (subset) and the built-in Times Bold Italic via **pdf-lib** + **fontkit**, draws each field at its configured coordinate, and hands back the resulting PDF bytes as a downloadable blob. Because it edits the original vector PDF rather than rasterizing a canvas, the output stays crisp and compact.

---

## License / Credits

Internal tool for the Department of Physics, Jagannath University. Built with [pdf-lib](https://pdf-lib.js.org/) and [fontkit](https://github.com/foliojs/fontkit).
