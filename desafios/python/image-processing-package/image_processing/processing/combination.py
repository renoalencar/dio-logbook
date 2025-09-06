# image_processing/processing/combination.py
"""
Módulo responsável por operações de combinação e análise de similaridade.

Este módulo implementa algoritmos avançados para comparar imagens,
transferir características e calcular métricas de similaridade.
"""

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import mean_squared_error, structural_similarity
from skimage.util import img_as_float


def transfer_histogram(image1, image2, multichannel=True):
    """
    Transfere as características de histograma da image2 para a image1.
    
    Esta função é como "ensinar" uma imagem a ter as mesmas características
    de iluminação e cor de outra imagem, útil para padronização de conjuntos
    de imagens ou correção de iluminação.
    
    Parameters:
    -----------
    image1 : numpy.ndarray
        Imagem que receberá as características (imagem de referência)
    image2 : numpy.ndarray  
        Imagem fonte das características (imagem modelo)
    multichannel : bool, optional
        Se True, processa imagens coloridas. Se False, trata como escala de cinza
    
    Returns:
    --------
    numpy.ndarray
        Imagem1 com histograma ajustado para se parecer com image2
        
    Examples:
    ---------
    -> # Transferir características de iluminação
    -> matched_image = transfer_histogram(dark_image, bright_image)
    
    -> # Para imagens em escala de cinza
    -> matched_gray = transfer_histogram(img1_gray, img2_gray, multichannel=False)
    """
    # Converter para float para melhor precisão nos cálculos
    img1_float = img_as_float(image1)
    img2_float = img_as_float(image2)
    
    # Aplicar o algoritmo de correspondência de histograma
    matched_image = match_histograms(
        img1_float, 
        img2_float, 
        multichannel=multichannel
    )
    
    return matched_image


def find_structural_similarity(image1, image2, return_difference=True):
    """
    Calcula a Similaridade Estrutural (SSIM) entre duas imagens.
    
    SSIM é uma métrica que avalia a similaridade entre imagens considerando
    luminância, contraste e estrutura - mais próxima da percepção humana
    que métricas simples como diferença pixel a pixel.
    
    Parameters:
    -----------
    image1 : numpy.ndarray
        Primeira imagem para comparação
    image2 : numpy.ndarray
        Segunda imagem para comparação
    return_difference : bool, optional
        Se True, retorna também a imagem de diferença (default: True)
    
    Returns:
    --------
    float or tuple
        Se return_difference=False: apenas o score SSIM (0-1, onde 1 = idênticas)
        Se return_difference=True: (score, difference_image)
        
    Raises:
    -------
    ValueError
        Se as imagens não tiverem o mesmo formato
        
    Examples:
    ---------
    -> # Apenas o score de similaridade
    -> similarity_score = find_structural_similarity(img1, img2, return_difference=False)
    
    -> # Score e imagem de diferença
    -> score, diff_img = find_structural_similarity(img1, img2)
    -> print(f"Similaridade: {score:.3f}")
    """
    if image1.shape != image2.shape:
        raise ValueError(
            f"As imagens devem ter o mesmo formato. "
            f"Imagem1: {image1.shape}, Imagem2: {image2.shape}"
        )
    
    # Converter para escala de cinza se necessário
    if len(image1.shape) == 3:
        gray_image1 = rgb2gray(image1)
        gray_image2 = rgb2gray(image2)
    else:
        gray_image1 = image1
        gray_image2 = image2
    
    # Calcular SSIM
    if return_difference:
        score, difference_image = structural_similarity(
            gray_image1, 
            gray_image2, 
            full=True,
            data_range=gray_image1.max() - gray_image1.min()
        )
        
        # Normalizar a imagem de diferença para melhor visualização
        # Converter para o intervalo [0, 255] para facilitar a visualização
        difference_image = ((1 - difference_image) * 255).astype(np.uint8)
        
        print(f"Similaridade Estrutural (SSIM): {score:.4f}")
        print(f"Interpretação: {_interpret_ssim_score(score)}")
        
        return score, difference_image
    else:
        score = structural_similarity(
            gray_image1, 
            gray_image2,
            data_range=gray_image1.max() - gray_image1.min()
        )
        
        print(f"Similaridade Estrutural (SSIM): {score:.4f}")
        print(f"Interpretação: {_interpret_ssim_score(score)}")
        
        return score


def calculate_mse(image1, image2):
    """
    Calcula o Erro Quadrático Médio (MSE) entre duas imagens.
    
    MSE mede a diferença média quadrática entre pixels correspondentes.
    Valores menores indicam maior similaridade (0 = imagens idênticas).
    
    Parameters:
    -----------
    image1 : numpy.ndarray
        Primeira imagem
    image2 : numpy.ndarray
        Segunda imagem
    
    Returns:
    --------
    float
        Valor MSE (menor = mais similar)
        
    Examples:
    ---------
    -> mse_value = calculate_mse(original_image, processed_image)
    -> print(f"MSE: {mse_value:.2f}")
    """
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter o mesmo formato")
    
    # Converter para escala de cinza se necessário
    if len(image1.shape) == 3:
        gray_image1 = rgb2gray(image1)
        gray_image2 = rgb2gray(image2)
    else:
        gray_image1 = image1
        gray_image2 = image2
    
    mse_value = mean_squared_error(gray_image1, gray_image2)
    
    print(f"Erro Quadrático Médio (MSE): {mse_value:.6f}")
    print(f"Interpretação: {_interpret_mse_score(mse_value)}")
    
    return mse_value


def blend_images(image1, image2, alpha=0.5):
    """
    Mistura duas imagens usando interpolação linear (alpha blending).
    
    Resultado = alpha * image1 + (1 - alpha) * image2
    
    Parameters:
    -----------
    image1 : numpy.ndarray
        Primeira imagem
    image2 : numpy.ndarray
        Segunda imagem
    alpha : float, optional
        Peso da primeira imagem (0.0 a 1.0, default: 0.5)
        alpha=1.0 resulta apenas na image1
        alpha=0.0 resulta apenas na image2
        alpha=0.5 mistura igualmente as duas
    
    Returns:
    --------
    numpy.ndarray
        Imagem resultante da mistura
        
    Examples:
    ---------
    -> # Mistura igual (50%-50%)
    -> blended = blend_images(img1, img2)
    
    -> # 70% da primeira imagem, 30% da segunda
    -> blended = blend_images(img1, img2, alpha=0.7)
    """
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter o mesmo formato")
    
    if not (0.0 <= alpha <= 1.0):
        raise ValueError("Alpha deve estar entre 0.0 and 1.0")
    
    # Converter para float para evitar overflow
    img1_float = img_as_float(image1)
    img2_float = img_as_float(image2)
    
    # Realizar a mistura
    blended = alpha * img1_float + (1 - alpha) * img2_float
    
    return blended


def _interpret_ssim_score(score):
    """Interpreta o score SSIM em linguagem natural."""
    if score >= 0.95:
        return "Praticamente idênticas"
    elif score >= 0.85:
        return "Muito similares"
    elif score >= 0.70:
        return "Moderadamente similares"
    elif score >= 0.50:
        return "Pouco similares"
    else:
        return "Muito diferentes"


def _interpret_mse_score(mse):
    """Interpreta o score MSE em linguagem natural."""
    if mse < 0.001:
        return "Praticamente idênticas"
    elif mse < 0.01:
        return "Muito similares"
    elif mse < 0.05:
        return "Moderadamente similares"
    elif mse < 0.1:
        return "Pouco similares"
    else:
        return "Muito diferentes"