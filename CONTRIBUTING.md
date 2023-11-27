# Primeiros passos

Verifique os _issues_ existentes e veja se o que você quer fazer já está sendo discutido. Se estiver, participe da discussão e dê suas sugestões. Do contrário, sinta-se à vontade para criar um novo _issue_ e começar sua discussão.

Caso prefira, apenas faça diretamente um _pull request_, mas lembre de descrever bem o que você pretende adicionar ou criar.

# Preparação do ambiente

1. Certifique-se de ter o _Python_ instalado em sua máquina. Recomenda-se usar a versão 3.12.0 (versão inicial do projeto) ou superior. Você pode baixar o _Python_ em https://www.python.org/.

2. Clone o repositório:

```
git clone https://github.com/claudioavgo/triphelper.git
```
3. Crie o ambiente virtual:

```
cd triphelper
```
```
python -m venv venv
```
4. Ative o ambiente virtual:
- No _Windows_:

```
venv\Scripts\activate
```
- No _MacOS/Linux_:

```
source venv/bin/activate
```
5. Instale as dependências:

```
pip install -r requirements.txt
```

6. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

# Cuidados com o código</h2>
Antes de fazer um _pull request_ certifique-se de que o seu código está limpo e organizado. Além disso, o código deve ser o mais direto e curto possível para facilitar o entendimento.

# Enviando uma contribuição
- Faça um _fork_ do projeto.
- Crie uma _branch_ com as suas modificações `git checkout -b exemplo`.
- Faça _commit_ das suas alterações `git commit -m 'Implementação do exemplo`
- Faça um _push_ na sua _branch_ `git push origin exemplo`.
- Faça um _pull request_ com suas alterações.

