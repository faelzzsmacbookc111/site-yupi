import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Nav links
content = content.replace(
    '<li><a href="#home" class="active">Home</a></li>\n                    <li><a href="#produtos">Produtos</a></li>',
    '<li><a href="#home" class="active">Início</a></li>'
)
content = content.replace('Catálogo de Produtos', 'Nosso Cardápio')
content = content.replace('href="#catalogo"', 'href="#produtos"')

# 2. Hero Text
content = content.replace(
    'Salgados Assados<br>Artesanais para<br>Lanchonetes e Atacado',
    'A Arte dos<br>Salgados Assados para<br>o seu Negócio'
)

# 3. Section Titles
content = content.replace('Nossos Produtos\n                    <span class="decoration right"></span>', 'Nosso Cardápio\n                    <span class="decoration right"></span>')
content = content.replace('Por que escolher nossa fábrica?', 'Nossos Diferenciais')
content = content.replace('Produção Artesanal', 'Feito à Mão')
content = content.replace('Depoimentos de Nossos Clientes', 'O que Dizem Nossos Parceiros')
content = content.replace('Como Funciona\n                    <span class="decoration right"></span>', 'Faça seu Pedido\n                    <span class="decoration right"></span>')

# 4. Product Descriptions
descriptions = {
    'Empada Abacaxi com Provolone': 'O equilíbrio perfeito entre o doce do abacaxi e o toque marcante do provolone.',
    'Empada Alho Poró': 'Sabor sofisticado com recheio cremoso que derrete na boca a cada mordida.',
    'Empada Carne Seca com Requeijão': 'Um clássico brasileiro irresistível, bem recheado e com tempero no ponto.',
    'Empada Frango com Azeitona': 'A receita tradicional com massa que desmancha, trazendo sabor de nostalgia.',
    'Empada Frango com Bacon': 'Crocância e sabor defumado que elevam o tradicional frango a outro nível.',
    'Empada Frango com Requeijão': 'Super cremosa, com aquele toque caseiro de tempero que todo mundo ama.',
    'Empada Milho com Requeijão': 'O contraste suave do milho com a cremosidade do nosso requeijão autêntico.',
    
    'Enrolado Queijo e Presunto': 'A combinação infalível abraçada por uma massa leve, dourada e macia.',
    'Enrolado Salsicha Especial': 'O lanche favorito, com salsicha de primeira linha e textura surpreendente.',
    
    'Esfirra Carne Tradicional': 'Recheio suculento, tempero árabe clássico e massa super fofinha assada na hora.',
    'Esfirra Frango Tradicional': 'Delicada, com recheio de frango desfiado bem temperadinho e aroma inconfundível.',
    'Esfirra Frango com Bacon': 'Para quem gosta de um sabor extra e marcante acompanhado de massa leve.',
    
    'Pastel Frango Tradicional': 'Assado com perfeição, guardando um recheio úmido e muito saboroso.',
    'Pastel Frango com Requeijão': 'A cremosidade ideal do requeijão envolta em uma massa leve e douradinha.',
    
    'Tortinha Frango com Bacon': 'Formato especial com massa quebradiça e recheio generoso de dar água na boca.',
    
    'Vegetariano': 'Sabor natural e ingredientes frescos para uma opção leve e muito saudável.',
    'X-Yupi': 'Nossa grande estrela! Uma explosão de sabores exclusivos que você precisa provar.'
}

for prod, desc in descriptions.items():
    # Encontrar a div com a classe product-name que contém o nome do produto
    pattern = r'(<h3 class="product-name">' + re.escape(prod) + r'</h3>\s*<p class="product-desc">)[^<]+(</p>)'
    content = re.sub(pattern, r'\g<1>' + desc + r'\g<2>', content)

# 5. About Section
about_old = """    <section id="sobre" class="section about-contact-section">
        <div class="container about-contact-container">
            <div class="about-content">
                <h2 class="about-title">Sobre Nós</h2>
                <p class="about-desc">Mais de 20 anos de tradição em salgados assados de qualidade.</p>

                <div id="contato" class="contact-form-wrapper">
                    <h3 class="form-title">Peça seu Orçamento</h3>"""

about_new = """    <section id="sobre" class="section about-contact-section">
        <div class="container about-contact-container">
            <div class="about-content" style="text-align: left;">
                <h2 class="about-title" style="justify-content: flex-start;">
                    Nossa história
                </h2>
                <p class="about-desc" style="margin-left: 0;">Tradição e amor em cada receita de salgado assado, levando o melhor sabor para o seu negócio.</p>

                <div id="contato" class="contact-form-wrapper">
                    <h3 class="form-title">Faça um Orçamento</h3>"""

content = content.replace(about_old, about_new)

# Add decorative elements closing tags correctly
end_form_str = """                        <button type="submit" class="btn btn-primary btn-block">Enviar</button>
                    </form>
                </div>
            </div>
        </div>
    </section>"""

end_form_new = """                        <button type="submit" class="btn btn-primary btn-block">Enviar</button>
                    </form>
                </div>
            </div>

            <!-- Decorative Elements -->
            <div class="about-decoration" style="display: flex; justify-content: center; align-items: center; position: relative; height: 100%; min-height: 450px;">
                <div class="deco-circle" style="width: 320px; height: 320px; border-radius: 50%; border: 3px dashed var(--primary-color); opacity: 0.2; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"></div>
                <div class="deco-image" style="width: 280px; height: 400px; background-color: var(--dark-green); border-radius: 140px 140px 20px 20px; overflow: hidden; position: relative; z-index: 2; box-shadow: 0 15px 35px rgba(0,0,0,0.15);">
                    <img src="images/bg-how-it-works.png" alt="Produção Yupi" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;">
                </div>
                <div class="deco-dots" style="position: absolute; bottom: 30px; right: 20px; font-size: 2.5rem; color: var(--primary-color); opacity: 0.4; letter-spacing: 5px; line-height: 0.6; z-index: 3;">
                    <i class="fa-solid fa-ellipsis"></i><br>
                    <i class="fa-solid fa-ellipsis"></i><br>
                    <i class="fa-solid fa-ellipsis"></i>
                </div>
            </div>
        </div>
    </section>"""

content = content.replace(end_form_str, end_form_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done index.html")
