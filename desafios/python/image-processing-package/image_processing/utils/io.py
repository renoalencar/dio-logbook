# image_processing/utils/io.py
"""
Módulo responsável pela entrada e saída de imagens.

Este módulo fornece funções simplificadas para carregar e salvar imagens
usando a biblioteca scikit-image como base.
"""

import os

from skimage.io import imread, imsave


def read_image(path, is_gray=False):
    """
    Carrega uma imagem de um caminho especificado.
    
    Parameters:
    -----------
    path : str
        Caminho para o arquivo de imagem
    is_gray : bool, optional
        Se True, carrega a imagem em escala de cinza (default: False)
    
    Returns:
    --------
    numpy.ndarray
        Array representando a imagem carregada
        
    Raises:
    -------
    FileNotFoundError
        Se o arquivo não existir no caminho especificado
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    
    try:
        image = imread(path, as_gray=is_gray)
        return image
    except Exception as e:
        raise ValueError(f"Erro ao carregar imagem: {str(e)}")


def save_image(image, path):
    """
    Salva uma imagem em um caminho especificado.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem a ser salva
    path : str
        Caminho onde a imagem será salva
        
    Raises:
    -------
    ValueError
        Se a imagem não for um array válido
    """
    if image is None or not hasattr(image, 'shape'):
        raise ValueError("Imagem deve ser um array numpy válido")
    
    # Criar diretório se não existir
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        imsave(path, image)
        print(f"Imagem salva com sucesso em: {path}")
    except Exception as e:
        raise ValueError(f"Erro ao salvar imagem: {str(e)}")