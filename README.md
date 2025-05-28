# Guia para Criação e Estruturação de Projetos Python do Zero

Workshop da Jornada de Dados

## Sobre

Este repositório apresenta um guia prático para criar e estruturar projetos Python do zero, seguindo boas práticas de organização, versionamento e colaboração.

## Objetivos

- Ensinar a criar um projeto Python do início
- Demonstrar a estrutura recomendada de diretórios e arquivos
- Integrar controle de versão com Git e GitHub
- Configurar ambiente virtual e dependências

## Estrutura Recomendada

```
projeto-py-full-do-zero/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Passos Iniciais

1. **Clone o repositório:**
    ```bash
    git clone git@github.com:leovnoliveira/projeto-py-full-do-zero.git
    cd projeto-py-full-do-zero
    ```

2. **Configure o ambiente Python:**

    - **Com pyenv (recomendado para gerenciar múltiplas versões do Python):**
        1. Instale o pyenv seguindo as instruções da [documentação oficial](https://github.com/pyenv/pyenv#installation).
        2. Liste as versões disponíveis:
            ```bash
            pyenv install --list
            ```
        3. Instale a versão desejada do Python:
            ```bash
                 pyenv install 3.11
                 ```
             4. Defina a versão local do projeto:
                 ```bash
                 pyenv local 3.11
                 ```

        - **Com Poetry (recomendado para projetos colaborativos):**
            1. Instale o pipx (caso ainda não tenha):
             ```bash
             pip install pipx
             pipx ensurepath
             ```
            2. Instale o Poetry globalmente usando pipx:
             ```bash
             pipx install poetry
             ```
            3. Inicialize o projeto com Poetry:
             ```bash
             poetry init
             ```
            4. Instale as dependências:
             ```bash
             poetry install
             ```
            5. Ative o ambiente virtual do Poetry:
             ```bash
             poetry env activate
             ```
            ```

    - **Com uv (alternativa rápida para projetos pessoais):**
        1. Instale o uv:
            ```bash
            pip install uv
            ```
        2. Crie e ative o ambiente virtual:
            ```bash
            uv venv
            source .venv/bin/activate  # Linux/Mac
            .venv\Scripts\activate     # Windows
            ```
        3. O uv também pode ser usado para instalar dependências e gerenciar versões de pacotes.

3. **Gerencie dependências:**

    - **Com Poetry (recomendado para projetos colaborativos):**
        1. Instale o Poetry:
            ```bash
            pipx install poetry
            ```
        2. Inicialize o projeto com Poetry:
            ```bash
            poetry init
            ```
        3. Instale as dependências:
            ```bash
            poetry install
            ```
        4. Ative o ambiente virtual do Poetry:
            ```bash
            poetry env activate
            ```

    - **Com uv (para projetos rápidos):**
        1. Instale as dependências listadas em requirements.txt:
            ```bash
            uv pip install -r requirements.txt
            ```

4. **(Opcional) Ambiente virtual manual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows
    ```

## Boas Práticas

- Separe código fonte e testes
- Utilize arquivos de configuração (.gitignore, requirements.txt)
- Documente o projeto no README.md
- Faça commits frequentes e descritivos

## Contribuição

Sinta-se à vontade para abrir issues e pull requests!

## Licença

Este projeto está licenciado sob a licença MIT.