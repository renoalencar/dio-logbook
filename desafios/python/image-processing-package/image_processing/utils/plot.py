# image_processing/utils/plot.py
"""
Módulo responsável pela visualização de imagens e histogramas.

Este módulo oferece funções para exibir imagens individuais, comparações
lado a lado e análise de histogramas usando matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_image(image, title="Imagem", figsize=(8, 6)):
    """
    Exibe uma única imagem.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem
    title : str, optional
        Título da imagem (default: "Imagem")
    figsize : tuple, optional
        Tamanho da figura (width, height) (default: (8, 6))
    """
    plt.figure(figsize=figsize)
    
    # Determinar se é escala de cinza ou colorida
    if len(image.shape) == 2 or image.shape[2] == 1:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)
    
    plt.title(title, fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def plot_result(*args, titles=None, figsize=(15, 5)):
    """
    Exibe múltiplas imagens lado a lado para comparação.
    
    Parameters:
    -----------
    *args : numpy.ndarray
        Arrays representando as imagens a serem exibidas
    titles : list, optional
        Lista de títulos para cada imagem
    figsize : tuple, optional
        Tamanho da figura (width, height)
    
    Example:
    --------
    -> plot_result(img1, img2, img3, titles=['Original', 'Processada', 'Diferença'])
    """
    number_images = len(args)
    
    if number_images == 0:
        print("Nenhuma imagem fornecida para plotagem")
        return
    
    fig, axes = plt.subplots(nrows=1, ncols=number_images, figsize=figsize)
    
    # Garantir que axes seja sempre uma lista
    if number_images == 1:
        axes = [axes]
    
    # Definir títulos padrão se não fornecidos
    if titles is None:
        titles = [f'Imagem {i+1}' for i in range(number_images)]
    
    for ax, image, title in zip(axes, args, titles):
        # Determinar se é escala de cinza ou colorida
        if len(image.shape) == 2 or (len(image.shape) == 3 and image.shape[2] == 1):
            ax.imshow(image, cmap='gray')
        else:
            ax.imshow(image)
        
        ax.set_title(title, fontsize=12)
        ax.axis('off')
    
    fig.tight_layout()
    plt.show()


def plot_histogram(image, title="Histograma", figsize=(12, 4)):
    """
    Exibe o histograma de uma imagem colorida (RGB).
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem colorida (3 canais)
    title : str, optional
        Título principal do gráfico
    figsize : tuple, optional
        Tamanho da figura (width, height)
        
    Raises:
    -------
    ValueError
        Se a imagem não tiver 3 canais de cor
    """
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("A imagem deve ter 3 canais de cor (RGB)")
    
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=figsize, 
                            sharex=True, sharey=True)
    
    color_list = ['red', 'green', 'blue']
    channel_names = ['Vermelho', 'Verde', 'Azul']
    
    for index, (ax, color, name) in enumerate(zip(axes, color_list, channel_names)):
        ax.set_title(f'Canal {name}', fontsize=12)
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, 
                alpha=0.8, density=True)
        ax.set_xlim([0, 256])
        ax.grid(True, alpha=0.3)
    
    fig.suptitle(title, fontsize=14)
    fig.tight_layout()
    plt.show()


def plot_grayscale_histogram(image, title="Histograma - Escala de Cinza", figsize=(8, 5)):
    """
    Exibe o histograma de uma imagem em escala de cinza.
    
    Parameters:
    -----------
    image : numpy.ndarray
        Array representando a imagem em escala de cinza
    title : str, optional
        Título do gráfico
    figsize : tuple, optional
        Tamanho da figura (width, height)
    """
    plt.figure(figsize=figsize)
    plt.hist(image.ravel(), bins=256, color='gray', alpha=0.8, density=True)
    plt.title(title, fontsize=14)
    plt.xlabel('Intensidade do Pixel', fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()