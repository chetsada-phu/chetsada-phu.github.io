"""Generate the portfolio's typography-based social preview image."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
im = Image.new('RGB', (1200, 630), '#edf3fc')
d = ImageDraw.Draw(im)
font_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
bold_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(size, bold=False):
    return ImageFont.truetype(bold_path if bold else font_path, size)
d.rectangle((0, 0, 16, 630), fill='#225bc5')
d.text((75, 61), 'PORTFOLIO  /  CHETSADA-PHU.GITHUB.IO', font=font(20, True), fill='#225bc5')
d.text((70, 135), 'Chetsada', font=font(95, True), fill='#182b43')
d.text((70, 238), 'Phummee.', font=font(95, True), fill='#225bc5')
d.line((76, 379, 1124, 379), fill='#c7d5e7', width=2)
d.text((76, 416), 'Data Science  /  ML Engineering', font=font(34, True), fill='#182b43')
d.text((76, 464), 'Applied AI  /  Data Analytics', font=font(34, True), fill='#182b43')
d.text((76, 555), 'Chulalongkorn University  ·  Economics', font=font(22), fill='#52677b')
im.save(ROOT / 'assets' / 'portfolio-cover-v1.png', optimize=True)
