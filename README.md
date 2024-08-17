# 🛠️ Automação de Cadastro de Produtos com PyAutoGUI

Este projeto é uma automação de processos usando **PyAutoGUI** que simula o preenchimento de formulários em um sistema fictício de cadastro de produtos. A automação lê os dados de um arquivo CSV e preenche os campos necessários em uma interface web.

## 🚀 Funcionalidades

- Abrir o navegador **Google Chrome**
- Acessar um sistema fictício de cadastro de produtos
- Ler os dados de produtos a partir de um arquivo CSV
- Preencher automaticamente o formulário de cadastro no sistema
- Realizar múltiplos cadastros de forma automatizada

## 📋 Pré-requisitos

- **Python 3.12**
- **PyAutoGUI** (Instalação: `pip install pyautogui`)
- **Pandas** (Instalação: `pip install pandas`)

## 🛠️ Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Arisson-Oliveira/Planilha-Automatica.git
    ```

2. Instale as dependências:

    ```bash
    pip install pyautogui pandas
    ```

3. Prepare seu arquivo CSV com os seguintes campos:

    ```csv
    codigo,marca,tipo,categoria,preco_unitario,custo,obs
    001,Marca X,Tipo A,Categoria 1,10.50,8.00,Sem observações
    002,Marca Y,Tipo B,Categoria 2,20.75,15.00,Novo produto
    ...
    ```

## 🖥️ Como executar a automação

1. Verifique se o arquivo `produtos.csv` está no diretório correto.
2. Execute o script:

    ```bash
    python automacao.py
    ```

3. O script abrirá o navegador, acessará o sistema e começará a cadastrar os produtos conforme os dados do CSV.

## ⚠️ Importante

- **Ajuste das coordenadas**: As coordenadas de cliques `x, y` no código foram configuradas para um monitor específico. Você pode precisar ajustá-las para sua tela usando o comando `pyautogui.position()` para identificar as coordenadas corretas.
- **Delays**: O tempo de espera (`sleep`) pode ser ajustado de acordo com a velocidade de carregamento do sistema.

## 🤝 Contribuições

Sinta-se à vontade para enviar pull requests, sugerir melhorias ou reportar problemas.

 
