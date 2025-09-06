# image_processing/__init__.py
"""
Image Processing Package

Um pacote Python moderno e modular para processamento e análise de imagens,
construído sobre scikit-image, numpy e matplotlib.

Principais funcionalidades:
- Entrada/saída de imagens
- Visualização e plotagem
- Transformações geométricas
- Análise de similaridade
- Combinação e transferência de características

Exemplo de uso básico:
    -> import image_processing as img_proc
    -> from image_processing.utils import read_image, plot_image
    -> from image_processing.processing import resize_image
     
    -> # Carregar e redimensionar uma imagem
    -> image = read_image("minha_imagem.jpg")
    -> small_image = resize_image(image, proportion=0.5)
    -> plot_image(small_image)

Estrutura do pacote:
    - image_processing.utils: Utilitários para I/O e visualização
    - image_processing.processing: Algoritmos de processamento e análise
"""

__version__ = "1.0.0"
__author__ = "Reno Alencar"
__email__ = "reno.alencar@proton.me"
__license__ = "MIT"

# Imports principais para facilitar o uso
from . import processing, utils
from .processing.combination import find_structural_similarity
from .processing.transformation import resize_image

# Fazer com que as funções mais comuns estejam disponíveis no nível superior
from .utils.io import read_image, save_image
from .utils.plot import plot_image, plot_result

# Lista de símbolos exportados quando usar "from image_processing import *"
__all__ = [
    'utils',
    'processing', 
    'read_image',
    'save_image',
    'plot_image',
    'plot_result',
    'resize_image',
    'find_structural_similarity'
]