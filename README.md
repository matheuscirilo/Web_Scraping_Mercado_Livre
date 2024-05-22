# Web scraping no site do MercadoLivre

Dentro da pasta SRC os seguintes comandos:

Para rodar o web scraping (EXTRAT)->

> scrapy crawl mercadolivre -o ../../data/data.jsonl

Para rodar o PANDAS (TRANSFORM e LOAD)->

> python transformacao/main.py


Para rodar o Streamlit (BI)->

> streamlit run dashboard/app.py 


Aplicação de um pipeline ETL com dashboard, feita para fazero web scraping (Extrat) no site do Mercado usando o Scrapy, tranformação com Pandas e Load no SQLite. além disso, conta com um dashboard feito em Streamlit. Foi utilizado conceito de Git para versioanemnto e o Software Dbeaver para análise do banco de dados relacioanl.
Aplicação 100% open suarce e funcional.
