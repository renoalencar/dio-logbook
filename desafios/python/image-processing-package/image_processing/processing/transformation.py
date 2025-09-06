# image_processing/processing/transformation.py
"""
Módulo responsável por transformações geométricas e de tamanho em imagens.

Este módulo implementa operações fundamentais como redimensionamento,
rotação e outras transformações usando scikit-image.
"""

import numpy as np
from skimage.transform import resize, rotate
from skimage.util import img_as_ubyte


def resize_image(image, proportion=None, output_shape=None, preserve_range=True):
    """
    Redimensiona uma imagem mantendo ou não a proporção original.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem original
    proportion : float, optional
        Fator de escala (0 < proportion <= 1) para redimensionamento proporcional
    output_shape : tuple, optional
        Forma específica de saída (height, width) ou (height, width, channels)
    preserve_range : bool, optional
        Se True, preserva o intervalo de valores original (default: True)
    
    Returns:
    --------
    numpy.ndarray
        Imagem redimensionada
        
    Raises:
    -------
    ValueError
        Se nem proportion nem output_shape forem fornecidos
        Se proportion estiver fora do intervalo válido
        
    Examples:
    ---------
    -> # Redimensionar para 50% do tamanho original
    -> smaller_image = resize_image(image, proportion=0.5)
    
    -> # Redimensionar para tamanho específico
    -> resized_image = resize_image(image, output_shape=(300, 400))
    """
    if proportion is None and output_shape is None:
        raise ValueError("Deve ser fornecido either 'proportion' or 'output_shape'")
    
    if proportion is not None:
        if not (0 < proportion <= 1):
            raise ValueError("A proporção deve estar entre 0 (exclusivo) e 1 (inclusivo)")
        
        # Calcular nova forma baseada na proporção
        if len(image.shape) == 3:
            height = round(image.shape[0] * proportion)
            width = round(image.shape[1] * proportion)
            new_shape = (height, width, image.shape[2])
        else:
            height = round(image.shape[0] * proportion)
            width = round(image.shape[1] * proportion)
            new_shape = (height, width)
    else:
        new_shape = output_shape
    
    # Redimensionar com anti-aliasing para melhor qualidade
    resized_image = resize(
        image, 
        new_shape, 
        anti_aliasing=True,
        preserve_range=preserve_range
    )
    
    return resized_image


def rotate_image(image, angle, center=None, preserve_range=True):
    """
    Rotaciona uma imagem por um ângulo especificado.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem original
    angle : float
        Ângulo de rotação em graus (positivo = anti-horário)
    center : tuple, optional
        Centro de rotação (row, col). Se None, usa o centro da imagem
    preserve_range : bool, optional
        Se True, preserva o intervalo de valores original (default: True)
    
    Returns:
    --------
    numpy.ndarray
        Imagem rotacionada
        
    Examples:
    ---------
    -> # Rotacionar 45 graus no sentido anti-horário
    -> rotated = rotate_image(image, 45)
    
    -> # Rotacionar em torno de um ponto específico
    -> rotated = rotate_image(image, 30, center=(100, 150))
    """
    rotated_image = rotate(
        image, 
        angle, 
        center=center,
        preserve_range=preserve_range,
        mode='constant',
        cval=0  # Preencher áreas vazias com preto
    )
    
    return rotated_image


def crop_image(image, top_left, bottom_right):
    """
    Recorta uma região retangular da imagem.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem original
    top_left : tuple
        Coordenadas (row, col) do canto superior esquerdo
    bottom_right : tuple
        Coordenadas (row, col) do canto inferior direito
    
    Returns:
    --------
    numpy.ndarray
        Região recortada da imagem
        
    Raises:
    -------
    ValueError
        Se as coordenadas estiverem fora dos limites da imagem
        
    Examples:
    ---------
    -> # Recortar região central da imagem
    -> cropped = crop_image(image, (100, 100), (400, 500))
    """
    top, left = top_left
    bottom, right = bottom_right
    
    # Validar coordenadas
    if (top < 0 or left < 0 or 
        bottom > image.shape[0] or right > image.shape[1] or
        top >= bottom or left >= right):
        raise ValueError("Coordenadas de recorte inválidas")
    
    # Realizar o recorte
    if len(image.shape) == 3:
        cropped_image = image[top:bottom, left:right, :]
    else:
        cropped_image = image[top:bottom, left:right]
    
    return cropped_image


def flip_image(image, direction='horizontal'):
    """
    Espelha uma imagem horizontal ou verticalmente.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem original
    direction : str
        Direção do espelhamento ('horizontal' ou 'vertical')
    
    Returns:
    --------
    numpy.ndarray
        Imagem espelhada
        
    Raises:
    -------
    ValueError
        Se a direção não for 'horizontal' ou 'vertical'
        
    Examples:
    ---------
    -> # Espelhar horizontalmente
    -> flipped_h = flip_image(image, 'horizontal')
    
    -> # Espelhar verticalmente  
    -> flipped_v = flip_image(image, 'vertical')
    """
    if direction not in ['horizontal', 'vertical']:
        raise ValueError("Direção deve ser 'horizontal' ou 'vertical'")
    
    if direction == 'horizontal':
        # Espelhar ao longo do eixo das colunas (esquerda-direita)
        flipped_image = np.fliplr(image)
    else:  # vertical
        # Espelhar ao longo do eixo das linhas (cima-baixo)
        flipped_image = np.flipud(image)
    
    return flipped_image