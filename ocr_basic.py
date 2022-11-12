from PIL import Image
import pyocr

# tools = pyocr.get_available_tools()
# print(tools)

# パソコンにはいっている部品をとってくる（tesseract)
# tools = pyocr.get_available_tools()
# tool = tools[0]
# print(tool)
# print(tool.get_name())

# 日本語の画像を撮ってきたが英語が読み込めないのでlangを日本語に変える
# tools = pyocr.get_available_tools()
# tool = tools[0]
# img = Image.open("tesseract_jpn.png")
# txt = tool.image_to_string(img, lang="eng", builder=pyocr.builders.TextBuilder())
# print(txt)


tools = pyocr.get_available_tools()
tool = tools[0]
# print(tool)
# print(tool.get_name())
img = Image.open("tesseract_jpn.png")
# img.show()
txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

print(txt)
