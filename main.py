import ssl
import flet as ft

ssl._create_default_https_context = ssl._create_unverified_context


def main(page: ft.Page):
    page.assets_dir = "assets"
    
    page.title = "Linha do Tempo - História da Energia Nuclear"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10

    def abrir_tela_detalhes(ano, titulo, imagens, detalhe_completo):
        def voltar(e):
            page.views.pop()
            page.update()
        if isinstance(imagens, str):
            imagens = [imagens]
        galeria_fotos1 = []
        for img_path in imagens:
            caminho_correto = img_path
            if caminho_correto.startswith("assets/"):
                caminho_correto = caminho_correto.replace("assets/", "/", 1)
            if not caminho_correto.startswith("/"):
                caminho_correto = "/" + caminho_correto

            galeria_fotos1.append(
                ft.Container(
                    content=ft.Image(src=caminho_correto, height=220, fit="contain"),
                    padding=5,
                    border_radius=10,
                )
            )
        tela_detalhes = ft.View(
            route=f"/detalhes/{ano}",
            controls=[
                ft.AppBar(
                    title=ft.Text(f"{ano} - {titulo}"),
                    bgcolor="#2a2a2a",
                    leading=ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=voltar,
                    ),
                ),
                ft.ListView(
                    expand=True,
                    padding=20,
                    controls=[
                        ft.Text(
                            ano,
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color="#00adb5",
                        ),
                        ft.Text(
                            titulo,
                            size=18,
                            weight=ft.FontWeight.W_500,
                            color="#ffffff",
                        ),
                        ft.Divider(color="#00adb5", height=20),
                        ft.Text("Galeria / Registros Históricos:", size=14, color="#b3b3b3"),
                        ft.Row(
                            controls=galeria_fotos1,
                            scroll="always",
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                        
                        ft.Divider(height=20, color="transparent"),
                        ft.Text(
                            "Detalhes do Evento Histórico:",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="#00adb5",
                        ),
                        ft.Text(
                            detalhe_completo,
                            size=16,
                            color="#e0e0e0",
                            selectable=True,
                        ),
                    ],
                ),
            ],
        )

        page.views.append(tela_detalhes)
        page.update()

    def criar_no_timeline(ano, titulo, imagens, detalhe_completo):
        foto_capa = imagens[0] if isinstance(imagens, list) else imagens
        caminho_capa_correto = foto_capa
        if caminho_capa_correto.startswith("assets/"):
            caminho_capa_correto = caminho_capa_correto.replace("assets/", "/", 1)
        if not caminho_capa_correto.startswith("/"):
            caminho_capa_correto = "/" + caminho_capa_correto

        return ft.GestureDetector(
            on_tap=lambda e: abrir_tela_detalhes(
                ano, titulo, imagens, detalhe_completo
            ),
            content=ft.Container(
                width=140,
                height=180,
                padding=10,
                bgcolor="#2a2a2a",
                border_radius=12,
                border=ft.Border.all(1, "#00adb5"),
                shadow=ft.BoxShadow(blur_radius=5, color="#000000"),
                alignment=ft.Alignment.CENTER,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                    controls=[
                        ft.Container(
                            width=75,
                            height=75,
                            border_radius = 16,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            alignment=ft.Alignment.CENTER,
                            content=ft.Image(src=caminho_capa_correto, fit="cover"),
                        ),
                        ft.Text(
                            ano,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color="#00adb5",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            titulo,
                            size=11,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ],
                ),
            ),
        )

    # Tela 1
    eventos_painel_1 = [
        (
            "1803",
            "Teoria Atômica",
            ["assets/John Dalton.jpg",'assets/ModeloDalton.jpg'],
            "John Dalton propôs o primeiro modelo atômico com bases científicas concretas. Sua teoria revolucionária afirmava que toda a matéria é constituída de átomos, que ele descrevia como esferas maciças, indivisíveis e indestrutíveis — uma ideia que ficou popularmente conhecida como o modelo da bola de bilhar. Dalton foi crucial para a ciência ao estabelecer que átomos de um mesmo elemento são idênticos em massa e propriedades. Essa teoria não apenas explicou leis químicas fundamentais, mas também lançou as bases para todo o estudo moderno da química e da estrutura da matéria.",
        ),
        (
            '1875',
            'Ampola de Crookes',
            ["assets/WilliamCrookes.jpg", "assets/AmpolaC.jpg"],
            'Inventada pelo físico inglês William Crookes, a Ampola de Crookes é um tubo de vidro selado sob vácuo parcial contendo eletrodos. Quando submetida a uma alta voltagem, a ampola emitia raios invisíveis (raios catódicos) que faziam o vidro brilhar. Este dispositivo tornou-se a ferramenta mais importante da física do final do século XIX.\nFoi utilizando e modificando a Ampola de Crookes que Wilhelm Röntgen descobriu os Raios-X (1895) e J.J. Thomson descobriu o Elétron (1897). Por ser o instrumento que revelou a existência das partículas subatômicas e das radiações, a ampola é considerada o marco inicial que deu origem à física atômica e nuclear moderna.',
        ),
        (
            "1895",
            "Raios-X",[
                "assets/Wilhelm Röntgen.jpg", 
                "assets/mãoesposa.jpg",
                "assets/röntgeneesposa.jpg"
            ],
            "Durante os seus experimentos com o Tubo de Crookes, Wilhelm Röntgen cobriu o tubo com um papelão escuro/preto para ver se a luz visível ainda seria capaz de sair daquela proteção. Contudo aquela contenção, blindou totalmente a luz emitida pelos raios catódicos, mas não era esta a sua maior surpresa naquele dia.\nUma placa de platinocianeto de bário próxima começou a brilhar, mesmo sem nenhuma luz interferindo naquela direção. Röntgen não sabia o que era, mas sabia que raios estavam atravessando a blindagem e acertando a placa, como não sabia sua origem os chamou de: Raios-X.\nApós a descoberta, ele realizou diversos testes, incluindo a famosa primeira radiografia da história: a mão esquerda de sua esposa, Anna Bertha. Ao ver a imagem revelada, exibindo seus ossos e o anel de casamento, ela exclamou que havia visto a própria morte.",
        ),
        (
            "1896",
            "Radioatividade",
            "assets/Becquerel.jpg",
            "Antoine Henri Becquerel descobre a radioatividade testando a descoberta de Wilhelm Röntgen. Ele tinha a teoria de que o que Röntgen havia descoberto tinha interferência da luz solar, então tentou simular o mesmo experimento.\nContudo, em Paris, no momento em que Becquerel buscava refutar a teoria de seu colega, o céu estava nublado. Conformado que seus experimentos ficariam para depois, guardou uranita com um filme por três dias.\nSua surpresa ao abrir a gaveta foi ter o filme e a chapa fotográfica completamente bombardeados e modificados pela emissão de algo que só poderiam vir da pedra de Urânio. Sendo assim, os chamou de: Raios Urânicos. Mais adiante, receberam como homenagem o nome de 'Raios de Becquerel'.\nSendo nada mais, nada menos, que as nossas radiações Alfa (α), Beta (β) e Gamma (γ).",
        ),
        (
            "1897",
            "O Elétron",
            ["assets/J.J. Thomson.jpg",'assets/ModeloThomson.jpg'],
            "J.J. Thomson foi mais um grande cientista a revolucionar a física usando a Ampola de Crookes. Para realizar seus testes sem interferências, ele evacuou quase todo o ar de dentro do tubo, criando um vácuo extremamente elevado. Ao aplicar campos elétricos e magnéticos no tubo, Thomson percebeu algo impressionante: o feixe de raios catódicos era atraído pela placa elétrica positiva e repelido pela negativa. Isso provou que os raios não eram ondas, mas sim um fluxo de partículas com carga elétrica negativa.\nEssa descoberta provou que o átomo não era indivisível (derrubando o modelo de Dalton) e revelou a existência da primeira partícula subatômica: o elétron. Para explicar sua descoberta, Thomson criou um novo modelo atômico, apelidado de 'Pudim de Passas', no qual os elétrons ficavam incrustados em uma 'massa' ou esfera de carga positiva.",
        ),
        (
            "1898",
            "Polônio e Radium",
            "assets/Pierre e Marie.webp",
            "Inspirada pela recente descoberta de Becquerel sobre o urânio, Marie Curie — ao lado de seu marido, Pierre Curie — decidiu investigar se outros elementos também emitiam essa radiação misteriosa. Trabalhando em condições precárias em um galpão improvisado em Paris, o casal analisou toneladas do minério pitchblenda (pechblenda).\nEm julho de 1898, após um exaustivo trabalho de separação química, eles isolaram um novo elemento radioativo, cerca de 400 vezes mais ativo que o urânio. Em homenagem à pátria de Marie, o elemento foi batizado de Polônio.\nContudo, ao notar que os resíduos restantes continuavam extremamente radioativos, o casal continuou os experimentos. Em dezembro do mesmo ano, descobriram o Rádio, um elemento impressionantes mil vezes mais radioativo que o urânio e que brilhava no escuro.\nEssas descobertas não apenas confirmaram que a radioatividade era uma propriedade atômica do próprio elemento, mas também renderam ao casal o Prêmio Nobel de Física de 1903 e abriram as portas para a medicina nuclear e o tratamento do câncer.",
        ),
        (
            '1899',
            "Descoberta das radiações Alfa (α) e Beta (β)",
            "assets/Rutherford.jpg",
            "Investigando a radiação emitida pelo urânio, Ernest Rutherford descobriu que ela não era homogênea. Ao colocar finas folhas de alumínio no caminho das emissões, ele percebeu que havia dois tipos distintos de radiação.A primeira, de baixo poder de penetração e facilmente bloqueada pela folha de papel ou alumínio, ele chamou de Radiação Alfa (α). A segunda, mais penetrante e capaz de atravessar camadas mais espessas de metal, batizou de Radiação Beta (β). Essa classificação foi o primeiro passo para mapear os componentes e os perigos do comportamento radioativo.",
        ),
        (
            "1900",
            "Descoberta dos Raios Gamma",
            "assets/paul.jpg",
            "Enquanto estudava as radiações emitidas pelos sais de rádio descobertos pelo casal Curie, o químico e físico francês Paul Villard observou um tipo de radiação surpreendentemente potente.Ao contrário das radiações alfa e beta, essa nova emissão não sofria desvio por campos magnéticos e conseguia atravessar blindagens espessas de chumbo. Mais tarde, Ernest Rutherford reconheceu a relevância dessa descoberta e a batizou de Radiação Gama (γ), identificando-a como uma onda eletromagnética de altíssima energia e alto poder de penetração."
        ),
        (
            "1902-1903",
            "Descoberta Transmutação Natural",
            ["assets/soddy.webp","assets/Rutherford.jpg"],
            "Trabalhando juntos na Universidade McGill, Ernest Rutherford e Frederick Soddy chocaram o mundo científico ao provar que a radioatividade era acompanhada pela transformação espontânea de um elemento químico em outro.\nAo analisarem o tório, eles perceberam que o elemento emitia radiação e se 'desintegrava', transformando-se em um elemento completamente novo com propriedades químicas diferentes. Essa descoberta derrubou o dogma de séculos de que os átomos eram imutáveis e eternos, provando que a matéria estava em constante transformação no nível subatômico."
        ),
        (
            "1905",
            "Relatividade",
            "assets/Einstein.jpg",
            "Em seu 'Ano Miraculoso' de 1905, Albert Einstein publicou a equação mais famosa da história da ciência: E = mc². Ela demonstrou que massa e energia são equivalentes e que uma quantidade minúscula de matéria pode se transformar em uma quantidade colossal de energia.\nEssa teoria resolveu o maior mistério da época: de onde vinha a energia inesgotável emitida pelos elementos radioativos descobertos pelo casal Curie. A física teórica de Einstein forneceu a base matemática necessária para entender a fissão nuclear e a liberação de energia do núcleo do átomo, alterando para sempre o rumo da humanidade.",
        ),
        (
            "1911",
            "Núcleo Atômico",
            ["assets/rutherford2.jpg",'assets/ModeloRutherford.jpg'],
            "Ao bombardear uma finíssima folha de ouro com partículas alfa, Ernest Rutherford e seus assistentes (Geiger e Marsden) observaram que a maioria das partículas atravessava a folha sem desvio, mas algumas poucas ricocheteavam em ângulos impressionantes. Rutherford comparou o fenômeno a atirar um projétil de 15 polegadas contra uma folha de papel de seda e vê-lo voltar contra você.\n\nEsse experimento revolucionário provou que o átomo é, na verdade, um grande espaço vazio com um centro extremamente denso, pequeno e de carga positiva: o Núcleo Atômico. Com essa descoberta, o modelo de 'Pudim de Passas' de Thomson foi superado, nascendo o Modelo Atômico Planetário de Rutherford.",
        ),
        (
            "1913",
            "Modelo Atômico de Bohr",
            ["assets/Bohr.jpg","assets/ModeloBohr.png"],
            "Para resolver o problema do modelo de Rutherford — onde os elétrons deveriam perder energia e colapsar no núcleo —, Niels Bohr aplicou a recente Teoria Quântica ao átomo. Ele propôs que os elétrons orbitam o núcleo em camadas ou níveis de energia bem definidos, sem emitir radiação enquanto estão em sua órbita 'permitida'.\n\nAlém disso, Bohr explicou que quando um elétron salta de um nível de maior energia para um menor, ele emite energia na forma de um fóton de luz. Esse modelo não apenas salvou a estrutura do átomo, mas explicou com precisão o espectro de luz do hidrogênio, dando início à física atômica moderna.",
        ),
        (
            "1913",
            "A Descoberta dos Isótopos",
            "assets/soddy.webp",
            "Enquanto estudava as cadeias de desintegração radioativa, o químico inglês Frederick Soddy percebeu algo intrigante: existiam elementos com massas atômicas diferentes, mas que possuíam exatamente as mesmas propriedades químicas e ocupavam o mesmo lugar na Tabela Periódica.\n\nSoddy os batizou de 'Isótopos' (do grego 'no mesmo lugar'). Essa descoberta provou que a identidade química de um elemento não depende da sua massa total. O conceito de isótopos tornou-se a espinha dorsal de toda a tecnologia nuclear moderna, sendo fundamental para o enriquecimento de urânio e para a medicina nuclear.",
        ),
        (
            "1913",
            "Lei de Moseley e o Número Atômico",
            "assets/Moseley.jpg",
            "Utilizando a recente técnica de difração de Raios-X, o jovem físico Henry Moseley analisou os raios emitidos por diversos metais e descobriu uma relação matemática perfeita entre a frequência desses raios e a carga elétrica do núcleo atômico.\n\nMoseley provou que o que define as propriedades de um elemento na Tabela Periódica não é a sua massa atômica (como Dmitri Mendeleev achava), mas sim o número de prótons em seu núcleo — surgindo assim o conceito oficial de Número Atômico (Z). Essa descoberta reorganizou a Tabela Periódica de forma definitiva.",
        ),
        (
            "1919",
            "Primeira Transmutação Artificial",
            "assets/rutherford3.jpg",
            "Pela primeira vez na história, o ser humano conseguiu realizar o antigo sonho dos alquimistas: transformar um elemento químico em outro. Ernest Rutherford bombardeou átomos do gás Nitrogênio com partículas alfa (núcleos de hélio) e observou que a colisão transformou o Nitrogênio em um isótopo de Oxigênio, liberando um núcleo de hidrogênio no processo.\n\nCom esse experimento, Rutherford não apenas realizou a primeira transmutação artificial da história, mas também identificou formalmente a partícula responsável por essa carga positiva emitida: o Próton. Foi o marco inicial da física nuclear de reação.",
        ),
        (
            "1930",
            "O Cíclotron",
            ["assets/Lawrence.jpg","assets/Ciclotron.jpg"],
            "De início, Ernest Lawrence teve a ideia teórica inicial no começo de 1929, após ler um artigo do físico holandês Rolf Widerøe sobre um acelerador linear.\nE então, Lawrence e seu estudante, Niels Edlefsen, construíram o primeiríssimo modelo experimental \n(feito de vidro e latão) na Universidade da Califórnia em Berkeley, que funcionou de forma muito rudimentar no outono de 1930.",
        ),
        (
            "1932",
            "Chadwick descobre o Nêutron",
            "assets/Chadwick.jpg",
            "Chadwick descobre o Nêutron utilizando-se do Polônio, ótimo emissor de partículas alfa. Com isso, ele lançou essas partículas alfa na direção de uma placa de Berílio que emitia por sua vez algo tão pesado, mas sem carga, que conseguia empurrar os prótons do anteparo que era parafina.\nTambém solucionou com isso o mistério de termos um átomo de Hélio+Berílio resultado em Carbono 12 e algo faltando com massa 1 e carga 0, chamado assim de Nêutron, mais que uma partícula, uma radiação corpuscular."
        ),
        (
            "1933",
            "Anderson descobre o Pósitron",
            "assets/Anderson.jpg",
            "Enquanto analisava fotografias de raios cósmicos em uma câmara de nuvem imersa em um forte campo magnético, o físico americano Carl Anderson observou o rastro de uma partícula intrigante. A trajetória tinha a mesma massa de um elétron, mas curvava no sentido oposto ao campo magnético, provando que possuía carga elétrica positiva.\n\nAnderson batizou a nova partícula de 'Pósitron' (o anti-elétron). Essa foi a primeira confirmação experimental da existência da antimatéria, que havia sido prevista teoricamente por Paul Dirac em 1928, abrindo um campo completamente novo na física de partículas e na medicina diagnóstica (como no moderno exame PET-Scan)."
        ),
        (
            "1935",
            "Yukawa prediz a existência do Méson",
            "assets/Yukawa.jpg",
            "Para resolver um dos maiores enigmas da física — como os prótons (que têm cargas positivas e se repelem fortemente) conseguem permanecer juntos e estáveis dentro do núcleo atômico —, o físico teórico japonês Hideki Yukawa propôs a existência de uma nova força: a Força Nuclear Forte.\n\nYukawa teorizou matematicamente que essa força era mediada pelo 'intercâmbio' de uma partícula ainda desconhecida, cuja massa seria intermediária entre a do elétron e a do próton. Ele a chamou de 'Méson' (do grego *mesos*, que significa 'meio'). Anos mais tarde, os mésons foram detectados experimentalmente (inclusive com a famosa participação do brasileiro César Lattes em 1947), e Yukawa tornou-se o primeiro japonês a receber o Prêmio Nobel de Física em 1949, por sua previsão."
        ),
        (
            "1938",
            "Hahn e Strassman/Meitner Frisch descobrem a Fissão Nuclear",
            [
            "assets/LiseMeitner_OttoHahn.jpg",
            "Hahn-Strassman.jpg",
            "assets/LiseFrischSeaborg.jpg",
            ],
            "Em Berlim, Otto Hahn e Fritz Strassmann bombardearam átomos de Urânio com nêutrons e, para surpresa de todos, encontraram o elemento Bário entre os produtos da reação — um elemento com quase metade da massa do urânio. Sem saber como explicar o resultado, Hahn escreveu para sua colega de longa data, a física Lise Meitner, que havia fugido da Alemanha nazista para a Suécia meses antes devido à sua origem judaica.\n\nAo lado do seu sobrinho, o físico Otto Frisch, Meitner decifrou o enigma durante uma caminhada na neve: o núcleo de urânio não havia apenas emitido partículas, ele havia se partido ao meio! Eles batizaram o processo de 'Fissão Nuclear' e usaram a equação de Einstein ($E = mc^2$) para provar que a fissão libertava uma quantidade colossal de energia, abrindo as portas para a era da energia e das armas nucleares.",
        ),
        (
            "1942",
            "Primeira Reação Nuclear controlada",
            "assets/Fermi.jpg",
            "Sob as arquibancadas do estádio Stagg Field, na Universidade de Chicago, uma equipe liderada pelo físico italiano Enrico Fermi construiu a Chicago Pile-1 (CP-1) — o primeiro reator nuclear artificial do mundo. O reator era uma estrutura monumental feita de blocos de grafite (usado como moderador) e urânio.\n\nEm 2 de dezembro de 1942, ao retirar cuidadosamente as barras de controle de cádmio, Fermi e sua equipe alcançaram a primeira reação em cadeia autossustentada e controlada da história. Esse experimento provou na prática que a energia nuclear poderia ser dominada e liberada de forma contínua, abrindo caminho para a criação dos reatores nucleares e marcando o início prático do Projeto Manhattan."
        ),
        (
            "1943",
            "Seaborg descobre o Plutônio",
            "assets/Seaborg.jpg",
            "Em meio à Segunda Guerra Mundial, Glenn Seaborg e a sua equipa na Universidade da Califórnia, Berkeley, isolaram e caracterizaram o elemento transurânico Plutónio (especificamente o isótopo Plutônio-239). O plutónio foi sintetizado ao bombardear o Urânio-238 com deutérios no Cíclotron.\n\nSeaborg demonstrou que o Plutônio-239 era altamente fissionável por nêutrons lentos, assim como o Urânio-235, mas com uma vantagem crucial: por ser um elemento químico diferente, podia ser separado do urânio por processos químicos industriais em vez do complexo enriquecimento isotópico. Essa descoberta levou à criação do Reator de BNL/Hanford e forneceu o combustível para o primeiro teste nuclear da história (Trinity) e para a bomba Fat Man."
        ),
        (
            "1945",
            "Primeira Bomba Atômica",[
            "assets/Oppenheimer.webp",
            "assets/BombaAtômica.jpg"
            ],
            "Sob a direção científica de J. Robert Oppenheimer e liderança militar do General Leslie Groves, o Projeto Manhattan culminou no Teste Trinity em 16 de julho de 1945, no deserto do Novo México — a primeira explosão nuclear da história humana, utilizando uma bomba de plutônio.\n\nPoucos semanas depois, em agosto de 1945, os Estados Unidos lançaram as bombas 'Little Boy' (de Urânio-235) sobre Hiroshima e 'Fat Man' (de Plutônio-239) sobre Nagasaki. Os ataques causaram uma destruição sem precedentes e forçaram o fim da Segunda Guerra Mundial, revelando ao mundo o poder aterrorizante do núcleo atômico e dando início à Guerra Fria e à era do desarmamento nuclear.",
        ),
    ]

    # Tela 2
    eventos_painel_2 = [
        (
            "1947",
            "Detecção dos Mésons",
            ["assets/LattesOcchialiniPowell.jpg","assets/CLattes.jpg", "assets/LatOccPow.jpg"],
            "O físico brasileiro César Lattes revolucionou a ciência mundial ao lado de Cecil Powell e Giuseppe Occhialini ao detectar o méson pi — a partícula que funciona como a 'cola' do núcleo atômico. Usando placas fotográficas especiais no topo do Monte Chacaltaya, na Bolívia, a equipe liderada por Powell, Lattes e Occhialini registrou os rastros dos raios cósmicos e colocou o Brasil na elite da física de partículas.",
        ),
        (
            "1948",
            "Méson Artificial",
            ["assets/Lattes-Gardner.jpg", "assets/LatYuk.jpg"],
            "Após detectar o méson pi na natureza, César Lattes e o físico norte-americano Eugene Gardner fizeram história novamente ao produzir os primeiros mésons de forma artificial. Utilizando o poderoso sincrociclótron da Universidade de Califórnia em Berkeley, a dupla provou que a humanidade era capaz de criar e controlar partículas subatômicas em laboratório, abrindo as portas para a física moderna de aceleradores.",
        ),
        (
            "1951",
            "Reator Rápido",
            ["assets/EBR-1.jpg", "assets/EBR-I.jpg", "assets/EBR-I(2).jpg"],
            "Em 20 de dezembro de 1951, o Reator Regenerador Rápido I (EBR-I), projetado pelo físico Walter Zinn nos EUA, fez história ao acender quatro lâmpadas com eletricidade gerada por reação nuclear. Pela primeira vez no planeta, provou-se que a energia do núcleo atômico podia ser convertida em energia elétrica útil para a humanidade, inaugurando a era da energia nuclear.",
        ),
        (
            "1954",
            "Castle Bravo e a Era das Armas Termonucleares",
            ["assets/BombaH.jpg", "assets/BombH.jpg", "assets/CastleBravo.jpg"],
            "Em 1º de março de 1954, os Estados Unidos realizaram no Atol de Bikini o teste Castle Bravo, a maior e mais destrutiva explosão termonuclear da história norte-americana (15 megatons). Ao contrário das bombas anteriores, essa utilizou combustível sólido (fusão de hidrogênio), provando a viabilidade de armas termonucleares operacionais e inaugurando a fase mais perigosa e assustadora da Guerra Fria.",
        ),
        (
            '1954',
            'Submarino Nuclear - Nautilus',
            ['assets/USS-Nautilus.jpg', 'assets/Naut.jpg', 'assets/Nau.jpg'],
            'Em 1954, os Estados Unidos lançaram ao mar o USS Nautilus, o primeiro submarino movido a energia nuclear do planeta. Criado sob a liderança do almirante Hyman Rickover, o Nautilus revolucionou a engenharia naval e a estratégia militar ao conseguir navegar por semanas totalmente submerso e sem precisar de reabastecimento — feito comprovado ao realizar a histórica travessia sob o gelo do Polo Norte..',
        ),
        (
            '1954',
            'Primeira Central Nuclelétrica Russa',
            ['assets/Obninsk.jpg', 'assets/Obs.jpg', 'assets/Obsi.jpg'],
            'Em 27 de junho de 1954, a União Soviética inaugurou a Usina Nuclear de Obninsk (APS-1), liderada pelo físico Igor Kurchatov. Conectada diretamente à rede elétrica pública, ela tornou-se a primeira central nucleoeletrica a fornecer energia para residências e indústrias na história, marcando o início do uso civil e comercial da tecnologia nuclear.',
        ),
        (
            '1956',
            '☢️ Calder Hall',
            ['assets/Calder Hall.jpg', "assets/Chsll.jpg", "assets/CalHall.jpg"],
            'Em 17 de outubro de 1956, o Reino Unido inaugurou Calder Hall, a primeira usina nuclear do mundo a gerar eletricidade em escala industrial e comercial contínua. Operando com reatores do tipo Magnox, a central forneceu energia para a rede elétrica britânica por quase 50 anos, tornando-se o grande marco da transição da energia nuclear para o consumo de massa.'
        ),
        (
            '1957',
            'Primeira Usina Americana Shippingport',
            ['assets/Shippingport.jpg', "assets/ship.jpg", "assets/shipp.jpg" ],
            'Em 18 de dezembro de 1957, entrava em operação a Shippingport Atomic Power Station, na Pensilvânia — a primeira usina nuclear de grande porte construída nos EUA exclusivamente para fins civis. Projetada sob a liderança do almirante Hyman Rickover usando um Reator de Água Pressurizada (PWR), a usina tornou-se o modelo padrão para a maioria dos reatores comerciais em operação no mundo até hoje.'
        ),
        (
            '1957',
            '☢️ O Desastre de Kyshtym',
            ["assets/Kyshtym.jpg", "assets/ky.jpg"],
            'Em 29 de setembro de 1957, uma falha no sistema de refrigeração de um tanque de resíduos radioativos causou uma explosão química devastadora na usina nuclear de Mayak, perto de Kyshtym, na União Soviética. A explosão lançou uma nuvem tóxica sobre uma área de centenas de quilômetros quadrados (a chamada Pegada Radioativa do Ural Leste), contaminando mais de 270.000 pessoas. O desastre foi mantido em segredo absoluto pelo governo soviético por mais de três décadas, sendo hoje classificado como o terceiro pior acidente nuclear da história, atrás apenas de Chernobyl e Fukushima.'
        ),
        (
            '1957',
            '☢️ Acidente em Windscale',
            ['assets/Windscale.jpg', 'assets/Windscale_Bombeiros.jpg', "assets/ws.jpg", "assets/wis.jpg"],
            'Em 10 de outubro de 1957, o Reino Unido enfrentou o pior acidente nuclear de sua história quando um incêndio atingiu o reator de Windscale (hoje Sellafield). O fogo queimou durante dias e liberou uma nuvem radioativa que se espalhou pelo Reino Unido e Europa, levando ao descarte de milhões de litros de leite contaminado e revelando ao mundo os riscos da energia atômica sem protocolos de segurança adequados.\nA usina foi renomeada para Sellafields após o acidente'
        ),  
        (
            '1958',
            'Navio Savannah',
            ['assets/NS Savannah.jpg', "assets/sav.jpg", "assets/sava.jpg"],
            'Lançado pelos Estados Unidos sob o programa Atoms for Peace do presidente Eisenhower, o NS Savannah fez história como o primeiro navio cargueiro e de passageiros movido a energia nuclear. Com seu design futurista e reator PWR, o navio viajou pelos oceanos provando que a energia atômica podia ser usada com segurança para o comércio e o transporte marítimo global de paz.'
        ),
        (
            '1959',
            'Quebra-Gelos - Lênin',
            ['assets/Lênin.jpg', "assets/NSLe.jpg"],
            'Em 1959, a União Soviética colocou em operação o NS Lenin, o primeiro navio de superfície movido a energia nuclear da história. Projetado para abrir caminho nas espessas camadas de gelo do Oceano Ártico, o navio provou a superioridade da propulsão nuclear em ambientes extremos, conseguindo navegar por anos na Rota do Mar do Norte sem precisar parar para reabastecer.'
        ),
        (
            '1965',
            'SNAP-10A',
            ['assets/SNAP-10A.jpg', "assets/snap.jpg"],
            'Em 3 de abril de 1965, os Estados Unidos lançaram o SNAP-10A, tornando-se o primeiro (e único) reator nuclear posto em órbita pelos EUA. Utilizando um sistema de conversão termoelétrica para gerar eletricidade a partir da fissão do urânio, o reator operou com sucesso por 43 dias no espaço, provando a viabilidade de fontes de energia atômica de longa duração para satélites e missões espaciais.'
        ),
        (
            '1979',
            '☢️ Three Mile Island',
            ["assets/tmi.jpg", "assets/tm.jpg"],
            'Em 28 de março de 1979, o Reator 2 da usina de Three Mile Island, na Pensilvânia, sofreu um derretimento parcial do seu núcleo — o pior acidente na história da energia nuclear comercial dos Estados Unidos. Provocado por uma combinação de falhas mecânicas, erros humanos e sensores confusos, o evento não deixou mortos diretos, mas paralisou a expansão da indústria nuclear americana por décadas e levou a uma reestruturação radical nas normas de segurança do setor.'
        ),
        (
            '1982',
            'Operação de Angra 1',
            ['assets/Angra1.jpg', "assets/Angra11.jpg", "assets/rAngra.jpg"],
            'Em 13 de março de 1982, o Brasil deu um salto histórico ao conectar a Usina Nuclear Angra 1 à rede elétrica nacional pela primeira vez. Localizada em Angra dos Reis (RJ) e equipada com um reator de água pressurizada (PWR), a usina deu início à operação comercial da tecnologia nuclear no país, inserindo o Brasil no seleto grupo de nações produtoras de energia atômica.'
        ),
        (
            '1986',
            '☢️ Acidente em Chernobyl',
            ['assets/Chernobyl.jpg', 'assets/Chernobyl2.jpg','assets/pédeelefante.jpg', "assets/che.jpg", "assets/cher.jpg"],
            'Em 26 de abril de 1986, uma falha crítica durante um teste de segurança causou a explosão do Reator 4 da Usina Nuclear de Chernobyl, na Ucrânia (então União Soviética). A explosão e o incêndio resultante lançaram uma imensa nuvem radioativa sobre a Europa, forçando a evacuação da cidade de Pripyat, mudando para sempre as leis mundiais de segurança nuclear e acelerando o colapso da própria União Soviética.'
        ),
        (
            '1987',
            '☢️ O Acidente Nuclear em Goiânia - Brasil',
            ["assets/goiânia.jpg", "assets/goiania.jpg"],
            'Em setembro de 1987, Goiânia (Goiás) foi palco do maior acidente radioativo em área urbana do mundo e o pior da história do Brasil. Tudo começou quando dois catadores de papel encontraram e abriram um aparelho de radioterapia abandonado num antigo hospital, expondo uma cápsula de Césio-137. O pó brilhante de cor azul fascina a população local, levando à contaminação direta de centenas de pessoas, à morte de quatro vítimas fatais nas primeiras semanas e ao isolamento de toneladas de lixo radioativo.'
        ),
        (
            '1989',
            'Criação de WANO',
            ['assets/WANO.jpg'],
            'Em 15 de maio de 1989, operadores de usinas nucleares de todo o mundo fundaram a WANO (World Association of Nuclear Operators) para garantir que um desastre como Chernobyl nunca mais se repetisse. Unindo nações dos dois lados da Guerra Fria, a organização estabeleceu um sistema global de inspeção, troca de dados e apoio mútuo, transformando a segurança nuclear em uma responsabilidade compartilhada por todos os países.'
        ),#"assets/"
        (
            '1989',
            '☢️ O Incêndio de Vandellòs I',
            ["assets/vand.jpg"],
            'Em 19 de outubro de 1989, um incêndio na sala de turbinas da Usina Nuclear Vandellòs I destruiu sistemas elétricos e alagou os pavimentos inferiores, ameaçando o resfriamento do reator. Apesar de não ter havido vazamento radioativo nem mortes, o evento foi classificado no Nível 3 da escala INES (o mais grave da história da Espanha) e levou ao fechamento definitivo da usina.'
        ),
        (
            '1999',
            '☢️ O Acidente Radiológico de Yanango ',
            ["assets/yanango.jpg"],
            'Em 20 de fevereiro de 1999, um dos piores acidentes radiológicos industriais da América Latina ocorreu na usina hidrelétrica de Yanango, no Peru. Um soldador encontrou uma fonte radioativa selada de Iridium-192 usada em radiografia industrial e, sem saber do perigo, colocou a cápsula no bolso da calça por horas. A exposição extrema resultou em amputação, queimaduras severas por radiação e graves lesões permanentes no trabalhador e em sua família.'
        ),
        (
            '1999',
            '☢️ O Acidente Radiológico de Tokaimura',
            ["assets/tok.jpg","assets/tokai.jpg"],
            'Em 30 de setembro de 1999, um grave acidente de criticidade ocorreu na usina de processamento de combustível nuclear da JCO em Tokaimura, no Japão. Causado por procedimentos ilegais, desrespeito a limites de massa e falta de treinamento adequado, o evento gerou uma reação em cadeia involuntária que expôs três trabalhadores a doses letais de radiação e tornou-se o pior acidente nuclear da história do Japão até o desastre de Fukushima em 2011.'
        ),
        (
            '2000',
            'Operação Angra 2',
            ['assets/Angra2.webp'],
            'Em 21 de julho de 2000, a Usina Nuclear Angra 2 foi sincronizada pela primeira vez à rede elétrica nacional, entrando em operação comercial no mesmo ano. Fruto do Acordo Nuclear Brasil-Alemanha, Angra 2 — com capacidade de cerca de 1.350 MW (mais de quatro vezes a potência de Angra 1) — tornou-se fundamental para a segurança energética do país e consolidou a engenharia nuclear de grande porte no Brasil.'
        ),
        (
            '2006',
            '☢️ O Incidente de Forsmark',
            ["assets/forsmark.jpg"],
            'Em 25 de julho de 2006, um curto-circuito na usina nuclear de Forsmark provocou a perda de energia externa e a falha simultânea de dois dos quatro geradores a diesel de emergência. O reator ficou a apenas 20 minutos de um derretimento parcial do núcleo devido ao apagão nos sistemas de segurança. O evento, classificado como Nível 2 na escala INES, revelou falhas graves de redundância e levou ao desligamento preventivo de dezenas de reatores ao redor do mundo para auditorias urgentes.'
        ),
        (
            '2011',
            '☢️ O Desastre Nuclear de Fukushima',
            ["assets/fuku.jpg", "assets/fukushima.jpg","assets/fukus.jpg"],
            'Em 11 de março de 2011, um terremoto de magnitude 9,0 seguido por um tsunami devastador atingiu a Usina Nuclear de Fukushima Daiichi. As ondas inundaram os geradores de emergência, interrompendo o resfriamento dos reatores e provocando o derretimento do núcleo de três unidades e explosões de hidrogênio. Classificado como Nível 7 na escala INES, o acidente forçou a evacuação de mais de 150 mil pessoas e levou o mundo a reavaliar a segurança nuclear frente a desastres naturais.'
        ),
        (
            '2026',
            'O Futuro do Átomo no Brasil',
            ["assets/2026.jpg"],
            'Em debate na Câmara dos Deputados, o país avança para criar o marco legal dos Pequenos Reatores Modulares (SMRs). Uma revolução com tecnologia 100% brasileira para levar energia limpa e contínua à Amazônia e garantir a soberania energética do país. (Fonte: Agência Câmara de Notícias)'
        ),
    ]
    
    def montar_painel(lista_eventos, titulo_painel):
        nos = [criar_no_timeline(*ev) for ev in lista_eventos]

        return ft.Container(
            padding=15,
            content=ft.Column(
                controls=[
                    ft.Text(
                        titulo_painel,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#ffffff",
                    ),
                    ft.Divider(color="#00adb5"),
                    ft.Row(controls=nos, wrap=True, spacing=15, run_spacing=15),
                ],
            ),
        )

    painel1 = montar_painel(
        eventos_painel_1, "As Descobertas Iniciais (1803 - 1945)"
    )
    painel2 = montar_painel(
        eventos_painel_2, "A Era Nuclear Moderna (1947 - Atual)"
    )


    page_view = ft.PageView(
        controls=[painel2],
        expand=True,
    )

    conteudo_principal = ft.Column(
        controls=[page_view],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    principal_view = ft.View(
        route="/", 
        controls=[conteudo_principal]
    )

    page.views.append(principal_view)
    page.update()



if __name__ == "__main__":
    ft.app(target=main)
