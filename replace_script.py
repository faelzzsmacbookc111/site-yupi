import re

with open('c:/Users/rafas/OneDrive/Área de Trabalho/Sites/Site Yupi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Title
content = content.replace(
    'Os Melhores<br>Salgados Assados para<br>o seu Negócio</h1>',
    'Os Melhores<br>Salgados Assados para<br>a sua Lanchonete</h1>'
)

# 2. Logistics Image
content = content.replace(
    '<img src="images/bg-how-it-works.png" alt="Produção Yupi"',
    '<img src="images/logistica.png" alt="Logística Yupi"'
)

# 3. Products Grid
new_products_grid = """            <div class="products-grid">
                <!-- Empadas -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Frango com Requeijão.jpeg" alt="Empada de Frango com Requeijão" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Frango com Requeijão</h3>
                        <p class="product-desc">Super cremosa, com aquele toque caseiro de tempero que todo mundo ama.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Frango com Azeitona.jpeg" alt="Empada de Frango com Azeitona" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Frango com Azeitona</h3>
                        <p class="product-desc">A receita tradicional com massa que desmancha, trazendo sabor de nostalgia.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Frango com Bacon.jpeg" alt="Empada de Frango com Bacon" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Frango com Bacon</h3>
                        <p class="product-desc">Crocância e sabor defumado que elevam o tradicional frango a outro nível.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Carne Seca com Requeijão.jpeg" alt="Empada de Carne Seca com Requeijão" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Carne Seca com Requeijão</h3>
                        <p class="product-desc">Um clássico brasileiro irresistível, bem recheado e com tempero no ponto.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Abacaxi com Provolone.jpeg" alt="Empada de Abacaxi com Provolone" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Abacaxi com Provolone</h3>
                        <p class="product-desc">O equilíbrio perfeito entre o doce do abacaxi e o toque marcante do provolone.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Alho Poró.jpeg" alt="Empada de Alho Poró" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Alho Poró</h3>
                        <p class="product-desc">Sabor sofisticado com recheio cremoso que derrete na boca a cada mordida.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Empada Milho com Requeijão.jpeg" alt="Empada de Milho com Requeijão" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Empada de Milho com Requeijão</h3>
                        <p class="product-desc">Textura macia, recheios maravilhosos, sabor marcante.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <!-- Tortinhas -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Tortinha Frango com Bacon.jpeg" alt="Tortinha de Frango com Bacon" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Tortinha de Frango com Bacon</h3>
                        <p class="product-desc">Formato especial com massa quebradiça e recheio generoso de dar água na boca.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Tortinha Frango com Bacon.jpeg" alt="Tortinha de Sabor 2" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Tortinha de [Sabor 2]</h3>
                        <p class="product-desc">Formato especial com massa quebradiça e recheio maravilhoso.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Tortinha Frango com Bacon.jpeg" alt="Tortinha de Sabor 3" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Tortinha de [Sabor 3]</h3>
                        <p class="product-desc">Formato especial com massa quebradiça e recheio maravilhoso.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <!-- Esfirras -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Esfirra Carne Tradicional.jpeg" alt="Esfirra de Carne Tradicional" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Esfirra de Carne Tradicional</h3>
                        <p class="product-desc">Recheio suculento, tempero árabe clássico e massa super fofinha assada na hora.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Esfirra Frango Tradicional.jpeg" alt="Esfirra de Frango Tradicional" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Esfirra de Frango Tradicional</h3>
                        <p class="product-desc">Delicada, com recheio de frango desfiado bem temperadinho e aroma inconfundível.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Esfirra Frango com Bacon.jpeg" alt="Esfirra de Frango com Bacon" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Esfirra de Frango com Bacon</h3>
                        <p class="product-desc">Para quem gosta de um sabor extra e marcante acompanhado de massa leve.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <!-- Enrolados -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Enrolado Queijo e Presunto.jpeg" alt="Enrolado de Queijo e Presunto" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Enrolado de Queijo e Presunto</h3>
                        <p class="product-desc">A combinação infalível abraçada por uma massa leve, dourada e macia.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Enrolado Salsicha Especial.jpeg" alt="Enrolado de Salsicha Especial" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Enrolado de Salsicha Especial</h3>
                        <p class="product-desc">O lanche favorito, com salsicha de primeira linha e textura surpreendente.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>
                
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Enrolado Queijo e Presunto.jpeg" alt="Enrolado de Sabor 3" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Enrolado de [Sabor 3]</h3>
                        <p class="product-desc">O lanche favorito de muitos, com um recheio delicioso.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <!-- Outros -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Pastel Frango Tradicional.jpeg" alt="Pastel de Frango Tradicional" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Pastel de Frango Tradicional</h3>
                        <p class="product-desc">Assado com perfeição, guardando um recheio úmido e muito saboroso.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Pastel Frango com Requeijão.jpeg" alt="Pastel de Frango com Requeijão" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Pastel de Frango com Requeijão</h3>
                        <p class="product-desc">A cremosidade ideal do requeijão envolta em uma massa leve e douradinha.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/Vegetariano.jpeg" alt="Salgado Vegetariano" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">Salgado Vegetariano <span style="color: inherit;">*</span></h3>
                        <p class="product-desc">Sabor natural e ingredientes frescos para uma opção leve e muito saudável.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>

                <div class="product-card">
                    <div class="product-image">
                        <img src="images/X-Yupi.jpeg" alt="X-Yupi" loading="lazy">
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">X-Yupi</h3>
                        <p class="product-desc">Nossa grande estrela! Uma explosão de sabores exclusivos que você precisa provar.</p>
                        <button class="btn btn-green">Ver Detalhes</button>
                    </div>
                </div>
            </div>"""

content = re.sub(r'            <div class="products-grid">.*?            </div>', new_products_grid, content, flags=re.DOTALL)

with open('c:/Users/rafas/OneDrive/Área de Trabalho/Sites/Site Yupi/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
