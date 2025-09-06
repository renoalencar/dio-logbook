# image_processing/utils/__init__.py
"""
Módulo de utilitários para o pacote image_processing.

Este sub-pacote contém funções auxiliares para:
- Entrada/saída de arquivos de imagem (io.py)
- Visualização e plotagem de imagens (plot.py)
"""

# Importar todas as funções dos módulos
from .io import read_image, save_image
from .plot import plot_grayscale_histogram, plot_histogram, plot_image, plot_result

# Exportações do módulo utils
__all__ = [
    'read_image',
    'save_image',
    'plot_image',
    'plot_result',
    'plot_histogram',
    'plot_grayscale_histogram'
]
