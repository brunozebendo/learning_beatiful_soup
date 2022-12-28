"""a intenção do código é ensinar o básico do beatiful soup, usando, para isso, o site que foi criado no
curso de frontend"""

from bs4 import BeautifulSoup
with open ("website.html") as file:

    contents = file.read()
"""os código abaixo são exemplos do que dá pra fazer com o programa, o primeiro imprime o texto do titulo,
o outro imprime o código inteiro, mas de maneira organizada, depois o código imprime o primeiro parágrafo (p)
que encontra"""
soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.pretiffy())
print(soup.p)
"""o código abaixo encontra todas as ocorrências do atributo estabelecido, nesse caso, as tags <a>"""
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)
"""já no exemplo abaixo o for loop vai localizar e separar somente o conteúdo do href, ou seja, o endereço dos sites"""
for tag in all_anchor_tags:
    print(tag.get("href"))
"""já a opção select seleciona o elemento que for passado, podendo ser uma tag específica, uma classe
que tem que ser passada como class_, um id, e por aí vai..."""
name = soup.select(".heading")
print(name)


"""o objetivo do código é analisar o HMTL do site abaixo, que é um site com últimas notícias da
tecnologia, e achar e separar uma determinada informação"""

##############Scraping Hacker News#########
from bs4 import BeautifulSoup
import requests
"""aqui é feito um request para o site e abaixo a informação é guardada em forma de texto, dentro da variável"""
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
"""abaixo são passados os atributos obrigatórios, ou seja, a variável com o texto e o html.parser(interpretador)"""
soup = BeautifulSoup(yc_web_page, "html.parser")
"""aqui são separados os artigos com a tag <a> e a classe storylink, pois dentro dessas classe é que estão os links para as reportagens. Reparar que isso é localizado através da função inspecionar, dentro do navegador"""
articles = soup.find_all(name="a", class_="storylink")
"""aqui são criados dicionários vazios que irão guardar o texto e o link de cada artigo, então é feito um 
for loop que pega o texto do artigo, acima já trabalhado, então acrescenta (append) no dicionário
e faz a mesma coisa para o link"""
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
"""aqui é usado um list comprehension para separar somente o dado necessário do número de votos no artigo,
 traduzindo, vai pegar o texto dentro do nome span, dentro da class_ score, vai fazer um loop, 
 vai pegar o primeiro item [0] usar o espaço como divisor e, por fim, vai transformar essa informação em um int"""
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
"""aqui vai usar a função max do Python para localizar o maior número, como a informação do texto, do link e do número estão na mesma ordem, ou seja, no mesmo índice (index), primeiro se localizou o maior número, depois, usou a função index para achar o indice desse número, e, por fim, o print imprime o artigo e o link que esteja no mesmo indice"""
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])