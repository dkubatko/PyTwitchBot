from PIL import Image, ImageDraw, ImageFont, ImageChops

import os


offset = 20


def img_equal(im1, im2):
  return ImageChops.difference(im1, im2).getbbox() is None

def outline(draw, text, font, x, y):
   shadowcolor = (10, 10, 10)
   draw.text((x-1, y-1), text, font=font, fill=shadowcolor, align='center')
   draw.text((x+1, y-1), text, font=font, fill=shadowcolor, align='center')
   draw.text((x-1, y+1), text, font=font, fill=shadowcolor, align='center')
   draw.text((x+1, y+1), text, font=font, fill=shadowcolor, align='center')

def new_img(data, wid, pix_raw, color, f_size, b_rgb, b_thick):   
   width = wid
   count = data["answers_count"]
   height = pix_raw
   img = Image.new("RGBA", (width, height * (2 * count + 1)))

   draw = ImageDraw.Draw(img)
   font = ImageFont.truetype("C://Test/text/open.ttf", f_size + 3)
   x = width / 2
   y = height / 2 #+ offset*0.25

   l1 = width / draw.textsize('a', font = font)[0]
   msg = split_text(data['question'], l1)

   draw.rectangle([(0, 0), (width,height*(2*count+1))], fill=b_rgb)
   
   outline(draw, msg, font, convert_xy(msg, x, y, draw, font)[0],
           convert_xy(msg, x, y, draw, font)[1])
             
   draw.text(convert_xy(msg, x, y, draw, font),
             msg, font = font, align = "center")

   
   if (b_thick != 0):
     for i in range(1, 2*(count + 1) + 1, 2):
       draw.line([(0, height*i), (width, height*i)], width = b_thick)
    
   for i in range(2, 2*count + 1, 2):

      font = ImageFont.truetype("C://Test/text/open.ttf", f_size)
      text = data["answers"][(i - 1) / 2]['text'] + " - " + str(data["answers"][(i - 1) / 2]["rate"]) + "%"

      l1 = width / draw.textsize('a', font = font)[0]
      text = split_text(text, l1)
      
      x = offset + (width - offset) / 2.0 - 0.25*offset
      y = (i-1)*height + offset + (height - 2 * offset) / 2.0
      
      outline(draw, text, font, convert_xy(text, x, y, draw, font)[0],
              convert_xy(text, x, y, draw, font)[1])

      draw.text(convert_xy(text, x, y, draw, font), text, font = font,
                align = "center")

      coef = data["answers"][(i - 1) / 2]["rate"] / 100.0
      draw.rectangle([(offset, i*height + 0.5*offset), ((width - 2*offset) * coef + offset,
                     i*height + height - 1.5*offset)],
                     fill = color)
      
   try:
     im = Image.open("out\\VKPolls.png")
   except:
     im = Image.new("RGBA", (100, 100))
     
   if not img_equal(img, im):
      img.save('out\\VKPolls.png', 'PNG')
      print 'Picture updated (/out/VKPolls.png)'
   return

def convert_xy(mes, x, y, draw, font):
   w, h = draw.textsize(mes, font = font)
   return float(x) - w / 2.0, float(y) - h / 2.0

def split_text(s, u):
   new_s = ''
   k = 0
   for i in s:
      k += 1
      if i == ' ' and k >= u - 5:
         new_s += '\n'
         k = 0
      else:
         new_s += i
   return new_s

   

