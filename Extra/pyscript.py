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