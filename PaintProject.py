#Julio Costa
#PaintProject
from pygame import*
from random import*
from math import*
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
root=tkinter.Tk()
root.withdraw()
screen=display.set_mode((1200,800))

#---------------------------------------------------Background Pic---------------------------------------------------
spiderPic=image.load("image/rsz_1spider-man-4k-wallpaper-3.jpg")
screen.blit(spiderPic,(0,0))

#---------------------------------------------------Tool Pics---------------------------------------------------
pencil=image.load("image/pencil.png")
pencil=transform.smoothscale(pencil,(50,50))
eraser=image.load("image/eraser.png")
eraser=transform.smoothscale(eraser,(50,50))
bucket=image.load("image/bucket_fill.png")
bucket=transform.smoothscale(bucket,(50,50))
paint=image.load("image/Paint-Brush-with-Dye-13-2016033035.png")
paint=transform.smoothscale(paint,(50,50))
spray=image.load("image/spray.png")
spray=transform.smoothscale(spray,(50,50))
dropper=image.load("image/eyedropper.png")
dropper=transform.smoothscale(dropper,(50,50))
square=image.load("image/1200px-Square_-_black_simple.svg.png")
square=transform.smoothscale(square,(50,50))
squareFill=image.load("image/squareFill.png")
squareFill=transform.smoothscale(squareFill,(50,50))
circle=image.load("image/1024px-Circle_-_black_simple.svg.png")
circle=transform.smoothscale(circle,(50,50))
circleFill=image.load("image/Disk_pack1.svg.png")
circleFill=transform.smoothscale(circleFill,(50,50))
undo=image.load("image/undo.png")
undo=transform.smoothscale(undo,(50,50))
redo=image.load("image/Arrows-Redo-icon.png")
redo=transform.smoothscale(redo,(50,50))
load=image.load("image/load-md.png")
load=transform.smoothscale(load,(50,50))
save=image.load("image/Save-Button-PNG-Transparent-File.png")
save=transform.smoothscale(save,(50,50))
clear=image.load("image/Notice-of-right-to-cancel.png")
clear=transform.smoothscale(clear,(50,50))
line=image.load("image/line.png")
line=transform.smoothscale(line,(50,50))

#---------------------------------------------------Stamps Pics---------------------------------------------------
spiderO=image.load("image/vjwiejyz83q01.png")
spider=transform.smoothscale(spiderO,(170,170))
spiderS=transform.smoothscale(spiderO,(370,370))

rhinoO=image.load("image/Rhino_from_MSM_render.png")
rhino=transform.smoothscale(rhinoO,(125,125))
rhinoS=transform.smoothscale(rhinoO,(325,325))

electroO=image.load("image/Electro_from_MSM_render.png")
electro=transform.smoothscale(electroO,(115,115))
electroS=transform.smoothscale(electroO,(315,315))

scorpionO=image.load("image/Scorpion_from_MSM_render.png")
scorpion=transform.smoothscale(scorpionO,(115,115))
scorpionS=transform.smoothscale(scorpionO,(315,315))

vultureO=image.load("image/Vulture_from_MSM_render.png")
vulture=transform.smoothscale(vultureO,(125,125))
vultureS=transform.smoothscale(vultureO,(325,325))

negetiveO=image.load("image/Mister_Negative_from_MSM_render.png")
negetive=transform.smoothscale(negetiveO,(115,115))
negetiveS=transform.smoothscale(negetiveO,(315,315))

colorPic=image.load("image/color-wheel-vector-clipart.png")
colorPic=transform.smoothscale(colorPic,(225,225))

#---------------------------------------------------background pic---------------------------------------------------
webSpiderO=image.load("image/01-1536805622502_1280w.jpg")
webSpider=transform.smoothscale(webSpiderO,(90,40))
webSpiderS=transform.smoothscale(webSpiderO,(810,550))
posSpiderO=image.load("image/thumb-1920-844967.jpg")
posSpider=transform.smoothscale(posSpiderO,(90,40))
posSpiderS=transform.smoothscale(posSpiderO,(810,550))
logSpiderO=image.load("image/PS4Wallpapers.com_59d66b9b9c361_spiderman-4k-logo-background-4k.jpg")
logSpider=transform.smoothscale(logSpiderO,(90,40))
logSpiderS=transform.smoothscale(logSpiderO,(810,550))

#---------------------------------------------------Title Pic on the right hand corner---------------------------------------------------
title=image.load("image/Marvel_Spider-Man_Logo.png")
title=transform.smoothscale(title,(300,150))

#---------------------------------------------------Tool Rect---------------------------------------------------
pencilRect=Rect(25,5,50,50)
eraserRect=Rect(25,65,50,50)
bucketRect=Rect(115,5,50,50)
paintRect=Rect(115,65,50,50)
sprayRect=Rect(205,5,50,50)
dropperRect=Rect(205,65,50,50)
squareRect=Rect(295,5,50,50)
squareFillRect=Rect(295,65,50,50)
circleRect=Rect(385,5,50,50)
circleFillRect=Rect(385,65,50,50)
undoRect=Rect(475,5,50,50)
redoRect=Rect(565,5,50,50)
loadRect=Rect(475,65,50,50)
saveRect=Rect(565,65,50,50)
clearRect=Rect(645,65,50,50)
lineRect=Rect(645,5,50,50)

#---------------------------------------------------Size Rect---------------------------------------------------
sizeRect=Rect(700,0,260,50)

#---------------------------------------------------Stamps Rect---------------------------------------------------
spiderRect=screen.blit(spider,(0,630))
rhinoRect=screen.blit(rhino,(160,670))
electroRect=screen.blit(electro,(305,675))
scorpionRect=screen.blit(scorpion,(445,675))
vultureRect=screen.blit(vulture,(583,670))
negetiveRect=screen.blit(negetive,(720,675))

#---------------------------------------------------Stamps Rect Outlines---------------------------------------------------
spiderOut=Rect(25,675,115,115)
rhinoOut=Rect(165,675,115,115)
electroOut=Rect(305,675,115,115)
scorpionOut=Rect(445,675,115,115)
vultureOut=Rect(583,675,115,115)
negetiveOut=Rect(720,675,115,115)

#---------------------------------------------------canvas rect backgrounds---------------------------------------------------
webSpiderRect=screen.blit(webSpider,(850,120))
posSpiderRect=screen.blit(posSpider,(850,180))
logSpiderRect=screen.blit(logSpider,(850,240))

#---------------------------------------------------canvas rect backgrounds outlines
webSpiderRect=Rect(850,120,90,40)
posSpiderRect=Rect(850,180,90,40)
logSpiderRect=Rect(850,240,90,40)

#---------------------------------------------------Canvas Rectangle and the outline too---------------------------------------------------
canvisRect=Rect(25,120,810,550)
screenRect=Rect(25,120,810,550)

#---------------------------------------------------Draws the Canvis---------------------------------------------------
draw.rect(screen,(255,255,255),canvisRect)
draw.rect(screen,(255,0,0),screenRect,2)

#---------------------------------------------------Title Rectangle---------------------------------------------------
titleRect=screen.blit(title,(855,650))


click=False
running=True

tool="pencil"
drawColor=(0,0,0)
size=5

#---------------------------------------------------undo and redo lists---------------------------------------------------
undoL=[screen.copy()]
redoL=[]

while running:
    for e in event.get():
        if e.type == QUIT:
            running=False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                back = screen.copy()
                click=True
            #size
            if e.button == 4:
                size+=1
            if e.button == 5:
                size-=1

        if e.type == MOUSEBUTTONUP:
            click=True
            pic=screen.copy() #Copies the screen when mouse button is up
            if click and canvisRect.collidepoint(mx,my):
                undoL.append(pic)#Appends the copy of the screen to the undo list
            if undoRect.collidepoint(mx,my):
                if len(undoL)>1: #Checks if the list length is bigger than 1
                    undopic=undoL[-1]
                    undoL=undoL[:-1]
                    redoL.append(undopic) #Takes the last copy after blitting and appends it to redo list
                screen.blit(undoL[-1],(0,0)) #Takes the last copy and blits it on the screen
            if redoRect.collidepoint(mx,my):
                if len(redoL)>0:
                    redoCopy=redoL.pop() #Gives the last value of redoList
                    undoL.append(redoCopy) #Appends the last value to undoList
                    screen.blit(redoCopy,(0,0)) #Blits the last value of redoList

    if size<1:
        size=1#make it so size dosen't go under 1
#----------------------------------------------------
    if key.get_pressed()[K_ESCAPE]:
        break
    #Mouse
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

#---------------------------------------------------Draw Tool Rect---------------------------------------------------
    draw.rect(screen,(255,0,0),pencilRect)
    draw.rect(screen,(255,0,0),eraserRect)
    draw.rect(screen,(255,0,0),bucketRect)
    draw.rect(screen,(255,0,0),paintRect)
    draw.rect(screen,(255,0,0),sprayRect)
    draw.rect(screen,(255,0,0),dropperRect)
    draw.rect(screen,(255,0,0),squareRect)
    draw.rect(screen,(255,0,0),squareFillRect)
    draw.rect(screen,(255,0,0),circleRect)
    draw.rect(screen,(255,0,0),circleFillRect)
    draw.rect(screen,(255,0,0),undoRect)
    draw.rect(screen,(255,0,0),redoRect)
    draw.rect(screen,(255,0,0),loadRect)
    draw.rect(screen,(255,0,0),saveRect)
    draw.rect(screen,(255,0,0),clearRect)
    draw.rect(screen,(255,0,0),lineRect)

#---------------------------------------------------Draw background rect---------------------------------------------------
    draw.rect(screen,(255,0,0),webSpiderRect,2)
    draw.rect(screen,(255,0,0),posSpiderRect,2)
    draw.rect(screen,(255,0,0),logSpiderRect,2)

#---------------------------------------------------Stamps Outlines---------------------------------------------------
    draw.rect(screen,(0),spiderOut,2)
    draw.rect(screen,(0),rhinoOut,2)
    draw.rect(screen,(0),electroOut,2)
    draw.rect(screen,(0),scorpionOut,2)
    draw.rect(screen,(0),vultureOut,2)
    draw.rect(screen,(0),negetiveOut,2)

#---------------------------------------------------Color Circle---------------------------------------------------
    draw.circle(screen,0,(1080,122),118)
    draw.rect(screen,drawColor,(1050,100,50,50))
    colorPicRect=screen.blit(colorPic,(968,10))


    #draw.rect(screen,(0,0,255),sizeRect)

#---------------------------------------------------tools---------------------------------------------------
    if colorPicRect.collidepoint(mx,my):
        if mb[0]==1:
            drawColor=screen.get_at((mx,my))

    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),pencilRect)
        if mb[0]==1:
            tool = "pencil"
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),eraserRect)
        if mb[0]==1:
            tool = "eraser"
    if bucketRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),bucketRect)
        if mb[0]==1:
            tool = "bucket"
    if paintRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),paintRect)
        if mb[0]==1:
            tool = "brush"
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),sprayRect)
        if mb[0]==1:
            tool = "spray"
    if dropperRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),dropperRect)
        if mb[0]==1:
            tool = "dropper"
    if squareRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),squareRect)
        if mb[0]==1:
            tool = "square"
    if squareFillRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),squareFillRect)
        if mb[0]==1:
            tool = "squareFill"
    if circleRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),circleRect)
        if mb[0]==1:
            tool = "circle"
    if circleFillRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),circleFillRect)
        if mb[0]==1:
            tool = "circleFill"
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),undoRect)
        if mb[0]==1:
            tool = "undo"
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),redoRect)
        if mb[0]==1:
            tool = "redo"
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),loadRect)
        if mb[0]==1:
            tool = "load"
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),saveRect)
        if mb[0]==1:
            tool = "save"
    if clearRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),clearRect)
        if mb[0]==1:
            tool = "clear"
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),lineRect)
        if mb[0]==1:
            tool = "line"

#---------------------------------------------------Stamps tools---------------------------------------------------
    if spiderRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "spider"
    if rhinoRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "rhino"
    if electroRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "electro"
    if scorpionRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "scorpion"
    if vultureRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "vulture"
    if negetiveRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "negetive"

#---------------------------------------------------backgrounds tools---------------------------------------------------
    if webSpiderRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "web"
    if posSpiderRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "pos"
    if logSpiderRect.collidepoint(mx,my):
        if mb[0]==1:
            tool = "log"

#---------------------------------------------------Tool Image---------------------------------------------------
    screen.blit(pencil,(25,5))
    screen.blit(eraser,(25,65))
    screen.blit(bucket,(115,5))
    screen.blit(paint,(115,65))
    screen.blit(spray,(205,5))
    screen.blit(dropper,(205,65))
    screen.blit(square,(295,5))
    screen.blit(squareFill,(295,65))
    screen.blit(circle,(385,5))
    screen.blit(circleFill,(385,65))
    screen.blit(undo,(475,5))
    screen.blit(redo,(565,5))
    screen.blit(load,(475,65))
    screen.blit(save,(565,65))
    screen.blit(clear,(645,65))
    screen.blit(line,(645,5))

    #higlights the tool
##    if tool=="pencil":
##        draw.rect(screen,(0,0,255),pencilRect,2)
##    elif tool=="eraser":
##        draw.rect(screen,(0,0,255),eraserRect,2)
##    elif tool=="bucket":
##        draw.rect(screen,(0,0,255),bucketRect,2)
##    elif tool=="brush":
##        draw.rect(screen,(0,0,255),brushRect,2)
##    elif tool=="spray":
##        draw.rect(screen,(0,0,255),sprayRect,2)
##    elif tool=="droper":
##        draw.rect(screen,(0,0,255),droperRect,2)
##    elif tool=="rect":
##        draw.rect(screen,(0,0,255),rectRect,2)
##    elif tool=="rectFill":
##        draw.rect(screen,(0,0,255),rectFillRect,2)
##    elif tool=="cirle":
##        draw.rect(screen,(0,0,255),circleRect,2)
##    elif tool=="circleFIll":
##        draw.rect(screen,(0,0,255),circleFillRect,2)
##    elif tool=="clear":
##        draw.rect(screen,(0,0,255),clearRect,2)
##    elif tool=="load":
##        draw.rect(screen,(0,0,255),loadRect,2)
##    elif tool=="save":
##        draw.rect(screen,(0,0,255),saveRect,2)
##    elif tool=="undo":
##        draw.rect(screen,(0,0,255),undoRect,2)
##    elif tool=="redo":
##        draw.rect(screen,(0,0,255),redoRect,2)

#---------------------------------------------------using the tools in the canvis---------------------------------------------------
    if mb[0]==1 and canvisRect.collidepoint(mx,my):
        screen.set_clip(canvisRect)
        if tool=="pencil":
            draw.line(screen,drawColor,(omx,omy),(mx,my))
        if tool=="eraser":
            tx=mx-omx
            ty=my-omy
            dis=hypot(tx,ty)
            for i in range(int(dis)):
                disx=int(omx+i/dis*tx)
                disy=int(omy+i/dis*ty)
                draw.circle(screen,(255,255,255),(disx,disy),size)
        if tool=="bucket":
            draw.rect(screen,(drawColor),canvisRect)
        if tool=="brush":
            tx=mx-omx
            ty=my-omy
            dis=hypot(tx,ty)
            for i in range(int(dis)):
                disx=int(omx+i/dis*tx)
                disy=int(omy+i/dis*ty)
                draw.circle(screen,drawColor,(disx,disy),size)
        if tool=="spray":
            for x in range(6):
                x=randint(-size,size)
                y=randint(-size,size)
                xx=mx-x
                yy=my-y
                if hypot(mx-xx,my-yy)<size:
                    draw.circle(screen,drawColor,(xx,yy),0)
        if tool=="dropper":
            drawColor=screen.get_at((mx,my))
        if tool=="square":
            if click:
                dotx=mx
                doty=my
                click=False
            screen.blit(back,(0,0))
            draw.rect(screen,drawColor,(dotx,doty,mx-dotx,my-doty),1)
        if tool=="squareFill":
            if click:
                dotx=mx
                doty=my
                click=False
            screen.blit(back,(0,0))
            draw.rect(screen,drawColor,(dotx,doty,mx-dotx,my-doty))
        if tool=="circle":
            if click:
                dotx=mx
                doty=my
                click=False
            screen.blit(back,(0,0))
            circleR=Rect(dotx,doty,mx-dotx,my-doty)
            circleR.normalize()
            if circleR.width<2 or circleR.height<2:
                draw.ellipse(screen,drawColor,circleR)
            else:
                draw.ellipse(screen,drawColor,circleR,1)
        if tool=="circleFill":
            if click:
                dotx=mx
                doty=my
                click=False
            screen.blit(back,(0,0))
            circleR=Rect(dotx,doty,mx-dotx,my-doty)
            circleR.normalize()
            draw.ellipse(screen,drawColor,circleR)
        if tool=="clear":
            draw.rect(screen,(255,255,255),canvisRect)
        if tool=="load":
            fileName=tkinter.filedialog.askopenfilename(filetypes=[("Picture files","*.png;*.bmp;*.jpg;*.jpeg")])
            if fileName!="":
                img=image.load(fileName)
                img=transform.smoothscale(img,(810,550))
                screen.blit(img,canvisRect)
            tool="pencil"
        if tool=="save":
            fileName=tkinter.filedialog.asksaveasfilename(filetypes=[("Picture files","*.png;*.bmp;*.jpg;*.jpeg")],defaultextension=".png")
            if fileName!="":
                image.save(screen.subsurface(canvisRect),fileName)
            tool = "pencil"
        if tool=="line":
            if click:
                linex=mx
                liney=my
                click=False
            screen.blit(back,(0,0))
            draw.line(screen,drawColor,(linex,liney),(mx,my))


#---------------------------------------------------Stamps on the canvas---------------------------------------------------
        if tool=="spider":
            screen.blit(back,(0,0))
            screen.blit(spiderS,(mx-185,my-185))
        if tool=="rhino":
            screen.blit(back,(0,0))
            screen.blit(rhinoS,(mx-162.5,my-162.5))
        if tool=="electro":
            screen.blit(back,(0,0))
            screen.blit(electroS,(mx-155.75,my-155.75))
        if tool=="scorpion":
            screen.blit(back,(0,0))
            screen.blit(scorpionS,(mx-155.75,my-155.75))
        if tool=="vulture":
            screen.blit(back,(0,0))
            screen.blit(vultureS,(mx-155.75,my-155.75))
        if tool=="negetive":
            screen.blit(back,(0,0))
            screen.blit(negetiveS,(mx-155.75,my-155.75))

#---------------------------------------------------Backgrounds on the canvas---------------------------------------------------
        if tool=="web":
            screen.blit(webSpiderS,(25,120))
        if tool=="pos":
            screen.blit(posSpiderS,(25,120))
        if tool=="log":
            screen.blit(logSpiderS,(25,120))

        screen.set_clip(None)
    omx,omy=mx,my


    print(tool)
#----------------------------------------------------
    display.flip()
quit()
