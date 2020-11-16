import cv2
import numpy as np

# Declaração das 6 faces do cubo
facesDoCubo = [ ([255, 0, 0], [255, 255, 0], [255, 0, 255], [255, 255, 255]),
				([0, 255, 0], [0, 0, 0], [0, 255, 255], [0, 0, 255]),
				([0, 0, 0], [255, 0, 0], [0, 0, 255], [255, 0, 255]),
				([255, 255, 0], [0, 255, 0], [255, 255, 255], [0, 255, 255]),
				([255, 0, 255], [255, 255, 255], [0, 0, 255], [0, 255, 255]),
				([255, 255, 0], [255, 0, 0], [0, 255, 0], [0, 0, 0])]

# Declaração dos eixos do cubo, sendo que cada um dos valores representam
# uma das cores primárias.
axis = [0, 0, 1, 1, 2, 2]

def mudarPagina(linha, face, page):
	# A linha é um array de duas posições e cada posição é uma tripla (R, G, B)
	# A face representa a face atual escolhida pelo usuário. É um valor de 0 a 5
	# A page é a página atual escolhida pelo usuário, indo de 0 a 255
    for x in linha:
        if x[axis[face]] == 0:
            x[axis[face]] = page
        else:
            x[axis[face]] = 255 - page



def emptyFunction(x):
    pass


def main():
	# Criação de um array de 255 linhas, 255 colunas e 3 dimensões
    img1 = np.zeros((255, 255, 3), np.uint8)

	# Criação da interface gráfica para a apresentação do Livro RGB
    windowName = 'Livro RGB'
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    
	# Criação das barras arrastáveis para a escolha das faces e das páginas
    cv2.createTrackbar('FACE', windowName, 0, 5, emptyFunction)
    cv2.createTrackbar('PAGE', windowName, 0, 255, emptyFunction)

    while(True):
		# Mostra a pagina "page" da face "faceAtual" na interface gráfica
        cv2.imshow(windowName, img1.astype(np.uint8))
        
		# Condição para fechar a interface gráfica que mostra o livro RGB
        if cv2.waitKey(1) == 27:
            break

		# Captura a face escolhida pelo usuário a partir da barra arrastável
        faceAtual = cv2.getTrackbarPos('FACE', windowName)
		# Captura a página escolhida pelo usuário a partir da barra arrastável
        page = cv2.getTrackbarPos('PAGE', windowName)
             
		# Declaração de um vetor para o armazenamento de cópias dos quatro 
		# vértices da face escolhida pelo usuário
        face = [facesDoCubo[faceAtual][0].copy(), facesDoCubo[faceAtual][1].copy(),
				facesDoCubo[faceAtual][2].copy(), facesDoCubo[faceAtual][3].copy()] 

		# Chamada da função responsável pela mudança de página
        mudarPagina(face[:2], faceAtual, page)
        mudarPagina(face[2:], faceAtual, page)
     
	 	# Cálculo da aresta inferior da face atual escolhida pelo usuário
        tracoInferior = np.linspace(face[:2][0], face[:2][1], 255)
	 	# Cálculo da aresta superior da face atual escolhida pelo usuário
        tracoSuperior = np.linspace(face[2:][0], face[2:][1], 255)
    
		# Preenchimento da página atual partindo da aresta superior e chegando
		# na inferior, tendo um total de 255 valores neste intervalo
        img1 = np.linspace(tracoInferior, tracoSuperior, 255).astype(np.uint8)
        
	# Fechamento da interface gráfica
    cv2.destroyAllWindows()



if __name__== "__main__":
    main()