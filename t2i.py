from captcha.image import ImageCaptcha
#import cv2
from PIL import Image
#import main
#genS = "Gen Img"
Loc = {
    "images": [
      {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/a02022.png",
            "label": "apple;red",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/b02022.png",
            "label": "ball;white",
            "date": "23-01-2022"
        },
    ]
}
genS ="HelloWorld"
def String2Img():
  img = ImageCaptcha(width = 300, height = 150)
  #gImg = img.generate(genS)
  img.write(genS, (genS+'.png'))
#gImg = img.generate_image(generate())

def ImgOnScreen():
  String2Img()
  IMG = Image.open((genS+'.png'))
  IMG.show()
  print("Image on screen")
  #display(IMG)
ImgOnScreen()
'''
def GenerateImgs():
  #Loc = main.Loc
  for i in range(len(Loc["images"])):
    data = Loc["images"][i]
    ImgOnScreen(label=data['label'],location=("GenImg/"+data["location"]),i=i)
    #cursor.execute(""" INSERT INTO Images(location,label,date) VALUES (?,?,?)""", (data["location"],data["label"],data["date"]))
'''