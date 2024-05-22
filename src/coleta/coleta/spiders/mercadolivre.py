import scrapy

# Para rodar o código basta estar no diretório raiz do projeto e dar o seguinte comando:
# scrapy crawl mercadolivre -o ../data/data.jsonl
class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-masculino"]

    page_count = 1
    max_pages = 20


    def parse(self, response):
        
        # Retorna todo o html do bloco do anúncio, gerando uma lista (54, no caso)
        # comando é testado no scrapy shell antes de vir para cá
        # Lembrar de colocar . quando tiver espaço no texto
        products = response.css('div.ui-search-result__content')
        
        #Pecorre cada caixa de products, retornando o texto solicitado
        for product in products:

            #Cria uma lista com os três campos do HTML refente ao preço na página
            prices = products.css('span.andes-money-amount__fraction::text').getall()
            cents = products.css('span.andes-money-amount__cents::text').getall()

            yield {
                'brand' : product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'name': product.css('h2.ui-search-item__title::text').get(),
                'old_price_reais': prices[0] if len(prices) >0 else None,
                'new_price_reais': prices[1] if len(prices) >0 else None,
                'old_price_centavos': cents[0] if len(prices) >0 else None,
                'new_price_centavos': cents[1] if len(prices) >0 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()                    
            }

        if self.page_count < self.max_pages:
            next_page=response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
            
            
#name -> h2 -> ui-search-item__title
#old price reais -> span -> andes-money-amount__fraction
#old price centavos -> span -> andes-money-amount__cents
#new price reais -> span -> andes-money-amount__fraction
#new price centavos -> span -> andes-money-amount__cents
#reviews_rating-number -> span -> ui-search-reviews__rating-number
#reviews_amount-> span -> ui-search-reviews__amount
        
