# Image Processing Package 🖼️

Este projeto implementa um pacote para processamento de imagens.

## ✨ Funcionalidades Principais

### 📁 **Manipulação de Arquivos**
- Leitura de imagens em diversos formatos (JPEG, PNG, TIFF, etc.)
- Salvamento com controle de qualidade
- Suporte a imagens coloridas e em escala de cinza

### 🎨 **Visualização Avançada**
- Plotagem de imagens individuais e comparações lado a lado
- Geração de histogramas para análise de distribuição de cores
- Interface intuitiva baseada em matplotlib

### 🔧 **Transformações Geométricas**
- Redimensionamento inteligente com preservação de qualidade
- Rotação com controle preciso de ângulo e centro
- Recorte, espelhamento e outras operações fundamentais

### 🔬 **Análise de Similaridade**
- Cálculo de Similaridade Estrutural (SSIM)
- Erro Quadrático Médio (MSE) 
- Transferência de características de histograma
- Combinação e mesclagem de imagens

## 🚀 Instalação

### Instalação para Desenvolvimento
```bash
git clone https://github.com/renoalencar/dio-logbook.git
cd image-processing-package
pip install -e .
```

1. **Clone o repositório**:
```bash
git clone https://github.com/renoalencar/dio-logbook.git
```

2. **Navegue até o diretório**:
```bash
cd dio-logbook/desafios/python/image-processing-package
```

3. **Instale o pacote**:
```bash
pip install -e .
```

### Dependências
- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.21.0  
- scikit-image >= 0.19.0

## 📖 Guia de Uso Rápido

### Exemplo Básico: Carregando e Visualizando
```python
import image_processing as img_proc
from skimage.data import camera  # Imagem de exemplo

# Carregar uma imagem
image = img_proc.read_image("minha_foto.jpg")

# Ou usar uma imagem de exemplo
image = camera()

# Visualizar a imagem
img_proc.plot_image(image, title="Minha Imagem")
```

### Redimensionamento Inteligente
```python
# Redimensionar para 50% do tamanho original
small_image = img_proc.resize_image(image, proportion=0.5)

# Ou especificar um tamanho exato
custom_image = img_proc.resize_image(image, output_shape=(300, 400))

# Comparar os resultados
img_proc.plot_result(
    image, small_image, custom_image,
    titles=['Original', '50% do tamanho', 'Tamanho customizado']
)
```

### Análise de Similaridade
```python
from image_processing.processing import find_structural_similarity

# Comparar duas imagens
score, diff_image = find_structural_similarity(image1, image2)

# Visualizar a diferença
img_proc.plot_result(
    image1, image2, diff_image,
    titles=['Imagem 1', 'Imagem 2', 'Mapa de Diferenças']
)

print(f"Similaridade: {score:.3f} (1.0 = idênticas)")
```

### Transferência de Características
```python
from image_processing.processing import transfer_histogram

# "Ensinar" uma imagem a ter as características de cor de outra
matched_image = transfer_histogram(dark_image, bright_image)

# Visualizar o resultado
img_proc.plot_result(
    dark_image, bright_image, matched_image,
    titles=['Imagem Escura', 'Imagem Clara', 'Resultado']
)
```

### Transformações Avançadas
```python
from image_processing.processing import rotate_image, flip_image, blend_images

# Rotacionar 45 graus
rotated = rotate_image(image, 45)

# Espelhar horizontalmente
flipped = flip_image(image, 'horizontal')

# Misturar duas imagens (50%-50%)
blended = blend_images(image1, image2, alpha=0.5)
```

### Análise de Histograma
```python
# Para imagens coloridas (RGB)
img_proc.plot_histogram(color_image, title="Distribuição de Cores")

# Para imagens em escala de cinza
from image_processing.utils import plot_grayscale_histogram
plot_grayscale_histogram(gray_image)
```

## 🏗️ Estrutura do Projeto

```
image-processing-package/
├── image_processing/              # Pacote principal
│   ├── __init__.py               # Imports e configurações principais  
│   ├── utils/                    # Utilitários
│   │   ├── __init__.py
│   │   ├── io.py                 # Entrada/saída de arquivos
│   │   └── plot.py               # Visualização e plotagem
│   └── processing/               # Algoritmos de processamento
│       ├── __init__.py
│       ├── transformation.py     # Transformações geométricas
│       └── combination.py        # Análise e combinação
├── README.md                     # Este arquivo
├── requirements.txt              # Dependências
├── setup.py                      # Configuração de instalação
└── LICENSE                       # Licença MIT
```

## 🧪 Executando Testes

```bash
# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Executar testes
pytest tests/

# Verificar cobertura
pytest --cov=image_processing tests/
```

## 📈 Casos de Uso Reais

### Processamento de Lote
```python
import os
import image_processing as img_proc

def process_folder(input_folder, output_folder, scale=0.5):
    """Redimensiona todas as imagens de uma pasta"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Carregar imagem
            image_path = os.path.join(input_folder, filename)
            image = img_proc.read_image(image_path)
            
            # Redimensionar
            resized = img_proc.resize_image(image, proportion=scale)
            
            # Salvar
            output_path = os.path.join(output_folder, f"resized_{filename}")
            img_proc.save_image(resized, output_path)
            
    print(f"Processamento concluído! Imagens salvas em {output_folder}")

# Usar a função
process_folder("fotos_originais/", "fotos_pequenas/", scale=0.3)
```

### Detecção de Mudanças
```python
def detect_changes(image_before, image_after, threshold=0.9):
    """Detecta se houve mudanças significativas entre duas imagens"""
    
    # Calcular similaridade
    similarity_score = img_proc.find_structural_similarity(
        image_before, image_after, return_difference=False
    )
    
    # Determinar se houve mudança significativa
    if similarity_score < threshold:
        print(f"⚠️ Mudança detectada! Similaridade: {similarity_score:.3f}")
        return True
    else:
        print(f"✅ Sem mudanças significativas. Similaridade: {similarity_score:.3f}")
        return False

# Exemplo de uso para monitoramento
has_changed = detect_changes(frame_anterior, frame_atual)
```

## 👨‍💻 Autor

Desenvolvido como parte do desafio de programação da Digital Innovation One.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](/LICENSE) para mais detalhes.

---

**💡 Observação**: Este sistema foi desenvolvido como proposta de desafio na plataforma DIO.