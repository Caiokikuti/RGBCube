import cv2
import numpy as np

facesDoCubo = [([255, 0, 0], [255, 255, 0], [255, 0, 255], [255, 255, 255]),
				([0, 255, 0], [0, 0, 0], [0, 0, 255], [0, 255, 255]),
				([0, 0, 0], [255, 0, 0], [0, 0, 255], [255, 0, 255]),
				([255, 255, 0], [0, 255, 0], [255, 255, 255], [0, 255, 255]),
				([255, 0, 255], [255, 255, 255], [0, 0, 255], [0, 255, 255]),
				([0, 0, 0], [0, 255, 0], [255, 0, 0], [255, 255, 0])]

axis = [0, 0, 1, 1, 2, 2]

def mudarPagina(linha, face, page):
    for x in linha:
        if x[axis[face]] == 255:
            x[axis[face]] = 255 - page
        else:
            x[axis[face]] = page



def emptyFunction(x):
    pass


def main():
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'Livro RGB'
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    
    cv2.createTrackbar('FACE', windowName, 0, 5, emptyFunction)
    cv2.createTrackbar('PAGE', windowName, 0, 255, emptyFunction)

    while(True):
        cv2.imshow(windowName, img1.astype(np.uint8))
        
        if cv2.waitKey(1) == 27:
            break
        face1 = cv2.getTrackbarPos('FACE', windowName)
        page = cv2.getTrackbarPos('PAGE', windowName)
             
        face = [facesDoCubo[face1][0].copy(), facesDoCubo[face1][1].copy(), facesDoCubo[face1][2].copy(), facesDoCubo[face1][3].copy()] 

        mudarPagina(face[:2], face1, page)
        mudarPagina(face[2:], face1, page)
     
        tracoInferior = np.linspace(face[:2][0], face[:2][1], 255)
        tracoSuperior = np.linspace(face[2:][0], face[2:][1], 255)
    
        img1 = np.linspace(tracoInferior, tracoSuperior, 255).astype(np.uint8)
        

    cv2.destroyAllWindows()



if __name__== "__main__":
    main()