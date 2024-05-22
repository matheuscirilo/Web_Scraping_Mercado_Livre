# Web scraping no site do MercadoLivre

Para rodar o web scraping ->

'''bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
'''

Para rodar o PANDAS tem que fazer isso dentro da pasta SRC ->

'''bash
python transformacao/main.py
'''

Para rodar o Streamlit tem que fazer isso dentro da pasta SRC ->

'''bash
streamlit run dashboard/app.py 
'''

Aplicação de um pipeline ETL com dashboard, feita para fazero web scraping (Extrat) no site do Mercado usando o Scrapy, tranformação com Pandas e Load no SQLite. além disso, conta com um dashboard feito em Streamlit. Foi utilizado conceito de Git para versioanemnto e o Software Dbeaver para análise do banco de dados relacioanl.
Aplicação 100% open suarce e funcional.
