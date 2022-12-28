from experta import Rule, Fact, KnowledgeEngine, AND

class regimeType(KnowledgeEngine):
    #declaring variables
    name = ""
    description = ""
    photo = ""
    # régime végétarian
    @Rule(AND(Fact(vegetarian='1'),Fact(vegetalian='0'), Fact(lactose_allergy='0'), Fact(gluten_allergy='0'), Fact(overweight='1'),
              Fact(diabetic='0'), Fact(muscles_gain='0'), Fact(physical_activity='0'), Fact(weight_loss='1')
             ))

    def Vegetarian(self):
        self.name = "Régime Végétarian"
        self.description = "Le régime alimentaire végétarien consiste à bannir la consommation de chair animale : viande, poisson, crustacés. En revanche, il tolère la consommation de miel, d’œufs et de produits laitiers."
        self.photo = r".\images\veg.png"


    #régime keto
    @Rule(AND(Fact(vegetarian='0'),Fact(vegetalian='0'), Fact(lactose_allergy='0'), Fact(gluten_allergy='0'), Fact(overweight='1'),
              Fact(diabetic='0'), Fact(muscles_gain='0'), Fact(physical_activity='0'), Fact(weight_loss='1'),
              ))
    def kéto(self):
        self.name = "Le régime keto"
        self.description = "Le régime keto est un régime dit strict et même restrictif. Ce dernier propose un modèle nutritionnel totalement différent par rapport aux recommandations habituelles que nous connaissons. Il consiste à réduire drastiquement la proportion de glucides ingérée quotidiennement. "
        self.photo = r".\images\keto.png"

    #régime protéinique
    @Rule(AND(Fact(vegetarian='0'), Fact(vegetalian='0'), Fact(lactose_allergy='0'), Fact(gluten_allergy='0'),
              Fact(overweight='0'),
              Fact(diabetic='0'), Fact(muscles_gain='1'), Fact(physical_activity='1'), Fact(weight_loss='1')
              ))
    def protein(self):
        self.name = "Régime protéinique"
        self.description = "Ces régimes hyperprotéinés consistent généralement à consommer de la viande, des oeufs, du poisson ou même des poudres protéinées à volonté et à restreindre drastiquement la consommation des autres aliments. Les régimes protéinés sont très controversés dans le milieu de la nutrition et de la santé."
        self.photo = r".\images\protein.png"

        #Le régime sans gluten
    @Rule(AND(Fact(vegetarian='0'),Fact(vegetalian='0'), Fact(lactose_allergy='0'), Fact(gluten_allergy='1'), Fact(overweight='0'),
              Fact(diabetic='0'), Fact(muscles_gain='0'), Fact(physical_activity='0'), Fact(weight_loss='0'),
              ))
    def Sans_gluten(self):
        self.name = "Le régime sans gluten"
        self.description = "Le régime sans gluten consiste à éliminer totalement de l'alimentation toutes les céréales contenant du gluten, les sous-produits de ces céréales et les aliments fabriqués à partir de ces sous-produits (exemples: vinaigre de malt, certaines viandes hachées, saucisses, bouillon cube, épaississants....)."
        self.photo =r".\images\sans_gluten.jpg"

    #régime végétalien
    @Rule(AND(Fact(vegetarian='0'), Fact(vegetalian='1'), Fact(lactose_allergy='1'), Fact(gluten_allergy='0'),
              Fact(overweight='0'),
              Fact(diabetic='0'), Fact(muscles_gain='0'), Fact(physical_activity='1'), Fact(weight_loss='0'),
              ))
    def Vegetalien(self):
        self.name = "Le régime végétalien"
        self.description = "Le régime alimentaire végétalien bannit tous les produits et aliments issus directement des animaux ou de leur exploitation. Cela comprend les viandes, les volailles, les poissons, les crustacés, les produits laitiers, les œufs et le miel."
        self.photo = r".\images\veg_strict.png"
#régime diabétique
    @Rule(AND(Fact(vegetarian='0'), Fact(vegetalian='0'), Fact(lactose_allergy='0'), Fact(gluten_allergy='0'),
              Fact(overweight='1'),
              Fact(diabetic='1'), Fact(muscles_gain='0'), Fact(physical_activity='0'), Fact(weight_loss='1'),
              ))
    def Diabetic(self):
        self.name = "Le régime diabétique"
        self.description = "Une alimentation équilibrée fait partie du traitement du diabète. Elle doit être adaptée à vos besoins et apporter des aliments variés. Certains d’entre eux sont à privilégier pour maintenir l’équilibre du diabète et prévenir au quotidien les maladies cardiovasculaires."
        self.photo = r".\images\diab.png"