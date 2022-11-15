#####################################################################
# Download and install these 2 softwares,(1) Python, (2) PIL        #
#   Python  http://www.python.org/ftp/python/2.3.4/Python-2.3.4.exe #
#   PIL     http://effbot.org/downloads/PIL-1.1.4.win32-py2.3.exe   #
#                                                                   #
# If above link is broken, try this, or do google search            #
# http://www.pythonware.com/products/pil/index.htm                  #
# http://www.python.org/download/                                   #
#                                                                   #
# Author homepage                                                   #
# http://anyway.sina.com.tw/bookmark/myfile_show.asp?myid=81143     #
#                                                                   #
# ver 0.4 (handle only jpg, gif, bmp, tif, tiff, ouput jpg)         #
# ver 0.5 (handle size)                                             #
# ver 0.6 (handle GIF )                                             #
#####################################################################

import os, string, sys, Image;

image_size=1920;

file_size=1024*1024;

def mangleFiles():
  for c in os.listdir( "." ):
    if os.path.isfile(c): # if it is a file, i.e., not a directory
      ### JPEG, BMMP, TIF, TIFF
      if os.path.splitext(c)[1]==".png" or os.path.splitext(c)[1]==".PNG" or os.path.splitext(c)[1]==".jpg" or os.path.splitext(c)[1]==".JPG" or os.path.splitext(c)[1]==".jpeg" or os.path.splitext(c)[1]==".JPEG" or os.path.splitext(c)[1]==".bmp" or os.path.splitext(c)[1]==".BMP" or os.path.splitext(c)[1]==".tif" or os.path.splitext(c)[1]==".TIF" or os.path.splitext(c)[1]==".tiff" or os.path.splitext(c)[1]==".TIFF":
        newfn = "new_" + os.path.splitext(c)[0] + ".jpg";
        print newfn;

        image1 = Image.open(c);
        width, height = image1.size;

        if width > height:
          s = float(height) / float(width);
          image2 = image1.resize((image_size, int(image_size*s)), Image.ANTIALIAS);
        else:
          s = float(width) / float(height);
          image2 = image1.resize((int(image_size*s),image_size));

        q = 100;
        image2.save(newfn, "JPEG", quality=q);
        info = os.stat(newfn)[6]

        while (info > file_size and q>1):
          q = q - 5;
          print q;	
          image2.save(newfn, "JPEG", quality=q);
          info = os.stat(newfn)[6]

      ### GIF
      elif os.path.splitext(c)[1]==".gif" or os.path.splitext(c)[1]==".GIF":
        newfn = "new_" + os.path.splitext(c)[0] + ".jpg";
        print newfn;

        image1 = Image.open(c).convert('RGB');
        width, height = image1.size;

        if width > height:
          s = float(height) / float(width);
          image2 = image1.resize((image_size, int(image_size*s)), Image.ANTIALIAS);
        else:
          s = float(width) / float(height);
          image2 = image1.resize((int(image_size*s),image_size));

        q = 100;
        image2.save(newfn, "JPEG", quality=q);
        info = os.stat(newfn)[6]

        while info > file_size:
          q = q - 1;		
          image2.save(newfn, "JPEG", quality=q);
          info = os.stat(newfn)[6]


mangleFiles();

raw_input("Program completed. Press enter.");