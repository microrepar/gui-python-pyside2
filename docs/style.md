# Alterando o estilo do aplicativo

Para exibir estilos disponíveis em uma plataforma:

```python
styles = QStyleFactory.keys()
print('Estilos disponíveis:', styles)
```

## QML

- https://doc.qt.io/qt-5/qtquickcontrols2-universal.html
- https://doc.qt.io/qt-5/qtquickcontrols2-styles.html

### Via Variáveis de ambiente

Utilizando um estilo pré definido:

```python
from os import environ

os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Default'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Fusion'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Imagine'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Universal'
os.environ['QT_QUICK_CONTROLS_STYLE'] = 'org.kde.desktop'
```

Alterando variáveis de ambiente especificas:

```python
from os import environ

environ['QT_QUICK_CONTROLS_UNIVERSAL_THEME'] = 'Dark'
environ['QT_QUICK_CONTROLS_UNIVERSAL_ACCENT'] = 'Violet'
environ['QT_QUICK_CONTROLS_UNIVERSAL_FOREGROUND'] = 'Brown'
environ['QT_QUICK_CONTROLS_UNIVERSAL_BACKGROUND'] = 'Steel'
```

Para que `QT_QUICK_CONTROLS_UNIVERSAL_xxx` funcione, a variável de ambiente `QT_QUICK_CONTROLS_STYLE` **deve** estar definida como `Universal`.

## Temas pré definidos:

- `Light`.
- `Dark`.
- `System`.

### Cores pré definidas

- Universal.Lime: #A4C400
- Universal.Green: #60A917
- Universal.Emerald: #008A00
- Universal.Teal: #00ABA9
- Universal.Cyan: #1BA1E2
- Universal.Cobalt: #3E65FF (default accent)
- Universal.Indigo: #6A00FF
- Universal.Violet: #AA00FF
- Universal.Pink: #F472D0
- Universal.Magenta: #D80073
- Universal.Crimson: #A20025
- Universal.Red: #E51400
- Universal.Orange: #FA6800
- Universal.Amber: #F0A30A
- Universal.Yellow: #E3C800
- Universal.Brown: #825A2C
- Universal.Olive: #6D8764
- Universal.Steel: #647687
- Universal.Mauve: #76608A
- Universal.Taupe: #87794E 

## XML

Para aplicar um estilo pré defindo em aplicativos `QMainWindow`, `QWidget` e `xml` pode-se utilizar:

```python
import sys

sys.argv += ['--style', 'Default']
sys.argv += ['--style', 'Fusion']
sys.argv += ['--style', 'Imagine']
sys.argv += ['--style', 'Material']
sys.argv += ['--style', 'Universal']
sys.argv += ['--style', 'Windows']
sys.argv += ['--style', 'windowsvista']
sys.argv += ['--style', 'org.kde.desktop']
```

> **OBS**: Nem todos os estilo funcionam em todas as plataformas, seja um aplicativo QML ou XML.