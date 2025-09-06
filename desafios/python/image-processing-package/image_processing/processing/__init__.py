# image_processing/processing/__init__.py
"""
Módulo de processamento para o pacote image_processing.

Este sub-pacote contém algoritmos para:
- Transformações geométricas (transformation.py)
- Análise de similaridade e combinação (combination.py)
"""

from .combination import (
    blend_images,
    calculate_mse,
    find_structural_similarity,
    transfer_histogram,
)

# Importar funções dos módulos de processamento
from .transformation import crop_image, flip_image, resize_image, rotate_image

# Exportações do módulo processing
__all__ = [
    # Transformation functions
    'resize_image',
    'rotate_image',
    'crop_image', 
    'flip_image',
    
    # Combination functions
    'transfer_histogram',
    'find_structural_similarity',
    'calculate_mse',
    'blend_images'
]