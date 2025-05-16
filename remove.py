from rembg import remove
from PIL import Image
from io import BytesIO

def remover(path1, path2):
    # input_path = r'D:\epic\project1\hello\hall.jpg'#
    # output_path = r'D:\epic\project1\hello\ball.png'

    input = Image.open(path1)
    output = remove(input)

    output.save(path2, 'PNG')
    print("removed sucessfully")


# here if you want to remove the back ground then first you need to uplode the picture in the hello named folder then 
# you can remove the back ground of the image and save it in the same folder with the name of car.png or any name and any file type you can change in that save line
#here yo need to make virtual environment and then install rembg and onnxrun time to that env an then run the given code using python remove.py