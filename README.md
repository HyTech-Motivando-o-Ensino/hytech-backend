<h1 align="center">Hytech->Backend</h1>

:question: Repositório para núcleo do backend do nosso projeto (Chatbot).

*Sistema Operacionais:*
- [Windows](#para-windows)
- [Linux](#para-linux)
- [Mac](#para-mac)

# Para Windows
>## Instalando o projeto

### 🟤Clone nosso repositório backend usando o git bash
```Python
git clone <https://github.com/HyTech-Motivando-o-Ensino/hytech-backend.git>
```
`OBS: É necessário ter instalado o git, acesse em: https://git-scm.com/downloads`

`OBS: É necessário ter instalado o python 3.8.3, acesse em: https://www.python.org/downloads/`
### 🟤Entrando dentro do repositório crie a venv
```Python
python -m venv venv
```
`OBS: É necessário instalar o ambiente virtual caso ainda não tenha em sua máquina`
```Terminal
pip install pipenv
```
### 🟤Ative a venv
```Python
source venv/Scripts/activate
```
### 🟤Instale o framework fastAPI
```Python
pip install fastapi
```
### 🟤Instale o servidor do fastAPI 
```Python
pip install "uvicorn[standard]"
```
`OBS: É necessário instalar o uvicorn`
### 🟤Instale o requirements.txt
```Python
pip install -r requirements.txt
```
``` json 
 OBS: Caso de erro, ainda irá rodar normalmente
``` 

>## Rodando o projeto novamente

### 🟤Ative a venv
```Python
source venv/Scripts/activate
```
### 🟤Rode o servidor
```Python
uvicorn server:app --reload
```
### 🟤Acesse http://127.0.0.1:8000

# Para Linux
###### (Em breve!)

# Para Mac
###### (Em breve!)
