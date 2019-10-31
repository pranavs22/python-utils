#! usr_/bin/env

#Imports
from PIL import Image, ImageFont, ImageDraw
import os
import argparse

def get_args():
    ''' This function creates arguments to be passed to the program'''
    parser=argparse.ArgumentParser(description="Please provide path to your folder as well the desired text")
    parser.add_argument("-t","--TEXT",help="Text to be written",required=True,type =str)
    parser.add_argument("-p","--PATH",help="Path of directory containing images",required=True,type =str)

    return parser.parse_args()
#Variables
args=get_args()
prefix=args.PATH
text=args.TEXT
#prefix='C:/test/'
def add_numbers(prefix,text="image"):
    '''
    This function takes a path containing images and adds numbers to it 
    as per the userp preference. Modified images are in the 'modified' 
    folder created newly
    
    '''
    
    out_path=prefix + 'modified/'
    
    files=os.listdir(prefix)
    counter=0
    
    try:
        
        for i in files:
            counter+=1
            if i.endswith(".jpg"):        
                file=prefix+i
#                print(file)
                img=Image.open(file,'r').convert('RGB')
                print("Image opened Successfully!")
                font=ImageFont.truetype('arial.ttf',15)
                (x,y) = (50,50)
                text= "Image " + str(counter)
                color='rgb(0,0,0)'
                draw=ImageDraw.Draw(img, 'RGB')        
                draw.text((x,y), text,fill=color,	 font=font)
                
                out=out_path + i
                if os.path.exists(out_path):
                    img.save(out)
                else:
                    os.mkdir(out_path)
                    img.save(out)
        
                print("File" , out ,"Saved Successfully!")
    except IOError:
    	print("File does not exist!")
    return

if __name__=="__main__":
    add_numbers(prefix,text)