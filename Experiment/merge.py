from PIL import Image
import sys

# 사용법: python merge_3x512.py a.png b.png c.png out.png
a, b, c, out_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
imgs = [Image.open(p).convert("RGBA").resize((512, 512)) for p in (a, b, c)]
canvas = Image.new("RGBA", (512*3, 512), (0, 0, 0, 0))
for i, im in enumerate(imgs):
    canvas.paste(im, (512*i, 0))
canvas.save(out_path)
print("Saved:", out_path)
