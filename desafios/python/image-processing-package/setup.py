# setup.py
"""
Configuração para distribuição do pacote image_processing.

Este arquivo define todos os metadados necessários para criar um pacote
Python distribuível através do PyPI ou TestPyPI.
"""

import pathlib

from setuptools import find_packages, setup

# O diretório onde este setup.py está localizado
HERE = pathlib.Path(__file__).parent

# Lendo o README para a descrição longa
README = (HERE / "README.md").read_text(encoding='utf-8')

# Lendo o arquivo de requisitos
def read_requirements():
    """Lê as dependências do arquivo requirements.txt"""
    requirements_path = HERE / "requirements.txt"
    if requirements_path.exists():
        with open(requirements_path, encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    # Metadados básicos do pacote
    name="image-processing-package",
    version="1.0.0",
    author="Reno Costa Alencar",
    author_email="reno.alencar@proton.me",
    
    # Descrições
    description="Um pacote Python moderno para processamento e análise de imagens",
    long_description=README,
    long_description_content_type="text/markdown",
    
    # URLs importantes
    url="https://github.com/renoalencar/dio-logbook/desafios/python/image-processing-package",
    
    # Classificadores que descrevem seu projeto
    classifiers=[
        # Estágio de desenvolvimento
        "Development Status :: 4 - Beta",
        
        # Público-alvo
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        
        # Tópicos relacionados
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        
        # Licença (deve corresponder ao arquivo LICENSE)
        "License :: OSI Approved :: MIT License",
        
        # Versões do Python suportadas
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Sistema operacional
        "Operating System :: OS Independent",
    ],
    
    # Palavras-chave para facilitar a busca no PyPI
    keywords="image processing, computer vision, scikit-image, matplotlib, numpy, image analysis",
    
    # Configuração dos pacotes
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    
    # Versão mínima do Python
    python_requires=">=3.8",
    
    # Dependências do projeto
    install_requires=read_requirements(),
    
    # Dependências extras opcionais
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
        "examples": [
            "jupyter>=1.0",
            "ipython>=7.0",
        ],
    },
    
    # Arquivos de dados incluídos no pacote
    include_package_data=True,
    
    # Especificar arquivos adicionais via MANIFEST.in se necessário
    # zip_safe=False,  # Descomente se houver problemas com imports
    
    # Entry points (comandos de linha de comando, se houver)
    # entry_points={
    #     "console_scripts": [
    #         "image-process=image_processing.cli:main",
    #     ],
    # },
)