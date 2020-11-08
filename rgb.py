import cv2
import numpy as np


facesDoCubo = {
  0: {"RGB": ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]), "axis": 0}, 
  1: {"RGB": ([255, 0, 0], [255, 255, 0], [255, 0, 255], [255, 255, 255]), "axis": 0},
  2: {"RGB": ([0, 0, 0], [255, 0, 0], [0, 0, 255], [255, 0, 255]), "axis": 1},
  3: {"RGB": ([0, 255, 0], [0, 0, 0], [0, 0, 255], [0, 255, 255]), "axis": 0},
  4: {"RGB": ([255, 255, 0], [0, 255, 0], [255, 255, 255], [0, 255, 255]), "axis": 1},
  5: {"RGB": ([255, 0, 255], [255, 255, 255], [0, 0, 255], [0, 255, 255]), "axis": 2},
  6: {"RGB": ([0, 0, 0], [0, 255, 0], [255, 0, 0], [255, 255, 0]), "axis": 2}
  }

def mudarPagina(linha, face,page):
    for x in linha:
        page -= 1
        if x[facesDoCubo[face]["axis"]] == 255:
            x[facesDoCubo[face]["axis"]] = 255 - page
        else:
            x[facesDoCubo[face]["axis"]] = page



def emptyFunction():
    pass


def main():
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'Livro RGB'
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    
    cv2.createTrackbar('FACE', windowName, 1, 6, emptyFunction)
    cv2.createTrackbar('PAGE', windowName, 0, 255, emptyFunction)

    while(True):
        cv2.imshow(windowName, img1.astype(np.uint8))
        
        if cv2.waitKey(1) == 27:
            break
        face1 = cv2.getTrackbarPos('FACE', windowName)
        page = cv2.getTrackbarPos('PAGE', windowName)
             
        linha1 = [facesDoCubo[face1]["RGB"][0], facesDoCubo[face1]["RGB"][1]] 
        linha2 = [facesDoCubo[face1]["RGB"][2], facesDoCubo[face1]["RGB"][3]]

        mudarPagina(linha1, face1, page)
        mudarPagina(linha2, face1, page)
     
        tracoInferior = np.linspace(linha1[0], linha1[1], 255)
        tracoSuperior = np.linspace(linha2[0], linha2[1], 255)
        img1 = np.linspace(tracoSuperior, tracoInferior, 255) 
        

    cv2.destroyAllWindows()



if __name__== "__main__":
    main()