Sistema para controle de Folha de Ponto
======================

Sistema web feito para auxiliar o controle de folha de ponto.

## Instalação
Recomendamos utilizar virtualenv para isolar o ambiente de desenvolvimento. Use pip para instalar as dependências

## Ambientes utilizados

 - Python 2.7.8
 - Virtualenv 1.8.4
 - Django 1.7.1
 - SQLite 3.8.5
 - PostgreSQL 9.3

* Para instalar e executar a aplicação localmente devemos clonar o repositório (ou baixar e descompactar o arquivo zip).

```bash
git clone git@github.com:wsilva/folha-de-ponto-ach2077.git folha-de-ponto-ach2077
```

* Instalar as dependências

```bash
cd folha-de-ponto-ach2077/
pip install -r requirements.txt.
```

* Copiar o arquivo de configuração base para o dentro do arquivo de configuração para ambiente de desenvolvimento

```bash
cp src/fdp/settings/base.py src/fdp/settings/dev.py
```

* Sincronizar o banco

```bash
cd src/
python manage.py syncdb
```

* Executar o servidor

```bash
python manage.py runserver
```

* E acessar pelo endereço http://0.0.0.0:8000 ou http://127.0.0.1:8000