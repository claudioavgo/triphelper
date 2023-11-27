<h1>Primeiros passos</h1>
<p>Verifique os issues existentes e veja se o que você quer fazer já está sendo discutido. Se estiver, participe da discussão e dê suas sugestões. Do contrário, sinta-se à vontade para criar um novo issue e começar sua discussão.</p>
<p>Caso prefira, apenas faça diretamente um pull request, mas lembre de descrever bem o que você pretende adicionar ou criar.</p>

<h1>Preparação do ambiente</h1>
<p>1. Certifique-se de ter o Python instalado em sua máquina. Recomenda-se usar a versão 3.12.0 (versão inicial do projeto) ou superior. Você pode baixar o Python em <a href="https://www.python.org/">python.org</a></p>
<p>2. Clone o repositório:</p>

```
git clone https://github.com/claudioavgo/triphelper.git
```
<p>3. Crie o ambiente virtual:</p>

```
cd triphelper
```
```
python -m venv venv
```
<p>4. Ative o ambiente virtual:</p>
<p>- No Windows:</p>

```
venv\Scripts\activate
```
<p>- No MacOS/Linux:</p>

```
source venv/bin/activate
```
<p>5. Instale as dependências:</p>

```
pip install -r requirements.txt
```

<p>6. Inicie o servidor de desenvolvimento:</p>

```
python manage.py runserver
```
