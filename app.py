
# AUTOMATED  CERTIFICATE GENERATOR

from PIL import Image,ImageDraw,ImageFont
import pyfastcopy
import shutil
import os

if os.path.isdir("Output"):
	os.remove

if not os.path.isdir("Output"):
	os.makedirs("Output")

i=101

print("GENERATING CERTIFICATES.........")

log=open('log.csv','w')
file = open("files/in.csv","r")
for x in file:
	base=Image.open("files/BASE.jpg")
	W,H=base.size
	putText=ImageDraw.Draw(base)
	font=ImageFont.truetype("files/tahoma.ttf",40)
	font2=ImageFont.truetype("files/tahoma.ttf",10	)
	text=x;
	w,h = putText.textsize(text, font=font)
	putText.text(((W-w)/2,(H-h)/2), text, fill="black",font=font)
	putText.text(((W-W)/2,(H-20)),("CERTIFICATION ID : CERT_%s"%i) , fill="#eea94c",font=font2)
	base.save("TEMPORARY_FILE.png",'PNG')
	newName=("%s"%text[0:5])
	shutil.copy("TEMPORARY_FILE.png","Output/"+(((str)(i))[-1:])+newName[0:3]+".png")
	log.write("CSEWR%s"%i+","+text+"\n")
	i+=2
    
os.remove("TEMPORARY_FILE.png")
