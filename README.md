# Projeto de Web Scraping da Seção de Tênis Masculinos do Mercado Livre

Este projeto tem como objetivo realizar o web scraping da seção de tênis masculinos do site Mercado Livre utilizando o framework Scrapy. A aplicação extrai dados relevantes dos produtos, transforma as informações utilizando a biblioteca Pandas e carrega os dados em um banco de dados SQLite. Além disso, um painel de BI foi desenvolvido usando Streamlit para visualização interativa dos dados coletados.

## Tecnologias Utilizadas

- **Scrapy:** Framework de web scraping usado para extrair dados da seção de tênis masculinos do Mercado Livre.
- **Pandas:** Biblioteca para manipulação e análise de dados, utilizada para transformar e limpar os dados extraídos.
- **SQLite:** Banco de dados relacional leve para armazenamento dos dados extraídos e transformados.
- **Streamlit:** Ferramenta para a criação de aplicações web interativas, utilizada para desenvolver o painel de BI que permite a visualização dos dados.

## Estrutura do Projeto

### Scrapy

A aplicação Scrapy é configurada para acessar a seção de tênis masculinos do Mercado Livre, navegando pelas páginas e extraindo informações relevantes de cada produto, tais como:

- Marca do produto
- Nome do produto
- Preço antigo
- Preço novo
- Número de avaliações
- Avaliação (de 0 a 5)

Os dados são armazenados temporariamente em arquivos JSON.

### Pandas

Os dados extraídos são carregados em um DataFrame do Pandas para processamento adicional. Nesta etapa, são realizadas transformações e limpezas dos dados, tais como:

- Conversão de tipos de dados
- Tratamento nas categorias de preço antigo e preço novo para assegurar consistência e precisão

### SQLite

Após a transformação, os dados são carregados em um banco de dados SQLite. A estrutura do banco de dados inclui uma tabela principal onde todas as informações dos produtos são armazenadas.

### Streamlit

Foi desenvolvido um painel de BI com Streamlit que permite a visualização interativa dos dados. O painel inclui os seguintes indicadores e visualizações:

- Número total de itens
- Número total de marcas
- Preço médio dos tênis
- Marcas mais encontradas
- Preço médio por marca
- Satisfação média por marca (avaliação)
- Desconto médio por marca (razão entre preço antigo e preço novo)

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o scraper na pasta src\coleta:**
   ```bash
   scrapy crawl mercadolivre -o data/data.jsonl
   ```

4. **Execute o script de transformação e carga:**
   ```bash
   python transformacao/main.py
   ````
5. **Inicie a aplicação Streamlit:**
   ```bash
   streamlit run dashboard/app.py
   ````
   

  
