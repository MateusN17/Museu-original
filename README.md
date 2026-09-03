<p align="center">
  <img src="assets/museu-logo.svg" alt="Símbolo do Museu de Ciências Nucleares" width="230">
</p>

<h1 align="center">Aplicativo Museu</h1>

<p align="center">
  Uma experiência interativa para explorar a história da radiação, da física atômica e da energia nuclear.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Licença-MIT-green.svg" alt="Licença MIT">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10 ou superior">
  <img src="https://img.shields.io/badge/Interface-Flet-00B4AB.svg" alt="Interface Flet">
  <img src="https://img.shields.io/badge/Web-HTML%20%7C%20CSS%20%7C%20JavaScript-F7DF1E.svg?logo=javascript&logoColor=black" alt="HTML, CSS e JavaScript">
</p>

<p align="center">
  <a href="#recursos">Recursos</a> •
  <a href="#início-rápido">Início rápido</a> •
  <a href="#versão-web">Versão web</a> •
  <a href="#estrutura-do-projeto">Estrutura</a>
</p>

## Sobre o projeto

O Museu da Radiação é um projeto educacional que transforma a evolução da ciência nuclear em uma linha do tempo interativa. A aplicação apresenta descobertas, cientistas, modelos atômicos, aplicações tecnológicas e acidentes radiológicos em ordem cronológica.

O conteúdo cobre eventos desde a teoria atômica de Dalton, em 1803, até acontecimentos contemporâneos relacionados à energia nuclear no Brasil e no mundo.

## Recursos

Área | Capacidades
--- | ---
Linha do tempo | Navegação cronológica dividida entre descobertas iniciais e era nuclear moderna
Conteúdo histórico | Textos explicativos sobre cientistas, experimentos, descobertas e acontecimentos
Galeria | Uma ou mais imagens associadas a cada evento histórico
Detalhes | Abertura de uma tela com o registro completo de cada evento
Interface Flet | Aplicação desktop com fundo animado, menu visual e navegação entre telas
Interface web | Página HTML responsiva com linha do tempo horizontal, cartões interativos e modal de detalhes
Identidade visual | Logo oficial do Museu em SVG, imagens temáticas e animações

## Início rápido

### Requisitos

- Python 3.10 ou superior;
- Windows, Linux ou macOS para executar a aplicação Python;
- navegador moderno para a versão web.

### Instalação

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

No Linux ou macOS, ative o ambiente virtual com:

```bash
source .venv/bin/activate
```

### Executar a aplicação Flet

```bash
python main.py
```

O aplicativo abre o menu principal do Museu e permite acessar a linha do tempo, navegar pelas eras e abrir os detalhes de cada evento.

## Versão web

Para executar `index.html` localmente, inicie um servidor HTTP na raiz do projeto:

```bash
python -m http.server 8000
```

Depois, abra [http://localhost:8000](http://localhost:8000) no navegador.

A versão web oferece navegação horizontal pela linha do tempo, cartões com interação por mouse ou teclado, galerias de imagens, modal de detalhes, progresso da jornada e animação da marca do Museu.

## Gerar APK

O projeto contém um workflow em `.github/workflows/main.yml` para gerar um APK com Flet quando houver um `push` na branch `main`.

Para gerar localmente, com o ambiente de build do Flet configurado:

```bash
flet build apk --yes --product "Museu da Radiação"
```

## Estrutura do projeto

```text
.
├── assets/
│   ├── museu-logo.svg              logo oficial do Museu
│   ├── fundo_animado_loop.mp4      fundo animado da aplicação Flet
│   ├── Historia da Radiacao (2).png imagem de apoio da interface
│   ├── menu_otimizado.webp         menu visual da aplicação Flet
│   └── ...                         imagens dos eventos históricos
├── .github/
│   └── workflows/main.yml          automação de build do APK
├── .vscode/                        configurações locais do editor
├── index.html                      versão web completa
├── main.py                         ponto de entrada da aplicação Flet
├── requirements.txt                dependências Python
├── settings.json                   configurações do projeto
└── .gitignore                      arquivos locais e gerados ignorados pelo Git
```

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).

## Observações

- Os arquivos de mídia da pasta `assets/` fazem parte da experiência e devem permanecer junto do projeto.
- O conteúdo tem finalidade educacional e pode ser ampliado com novos eventos, imagens e fontes históricas.
- O símbolo usado neste README foi obtido do SVG original do Museu e mantido sem o texto inferior.
