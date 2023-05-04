enum a random dej do __init__.py

uprav requirements na to co potrebujes

projed zda je vse jak ma byt v pipfile

setupni si pylint

setupni si flake8
setupni si autopep8

race_details predelat na objekty
zakomponovat do objektu head
zakomponovat do objektu apearence

vytvorit objektove pridani do hlavniho objektu celkovou rasu abych se vyhnul zbytecnem radkum jako v body

z generator_atributu vyber pointspooly a dej je do enum

pridat nejake yumly kde bude videt workflow jak to randomuje odkud a pak po co

??? nebyla by lepsi graphql???

rozhodni zda to pujde do webu ci jen text ci pdf ci excel ci...
asi by bylo nejlepsi mit moznost savu do vicero formatu
a popripade i json, pak i generator obrazku, generator pres chatgpt...

########################
### RANDOM
########################
vytvor def random ktery vyrandomuje cislo a bude se moc pouzivat kdekoliv

vytvor master random ktery vyrandomuje z enumu a bude se moc pouzivat kdekoliv

vytvor master random ktery vyrandomuje x hodnot kde max bude velikost enumu z enumu a bude se moc pouzivat kdekoliv

vytvor master random ktery vyrandomuje z listu ci tuplu a bude se moc pouzivat kdekoliv

########################
### vse jde pouzit i pro rodice, oblibeneho mazlicka a pod...
### TODO: dodelat, rozvinout a roztridit logicky DATA z GeneralSocial
########################
chci mit jeden objekt:
"postava" bude NPC, Postava
ten budu extendovat o:
apearence objekt
    ten se sklada z:
        hlava
        rasove detaily
        vzhled - postava, vyska, obleceni, tetovani
Generator jmen
    zde pravidla:
    (bud s ohledem na pohlavi ci random, dle random zeme, vetsi procento ma zeme rodicu)
        pro:
            jmena
            prijmeni
    (bud s ohledem na viru rodicu ci random)
        pro:
            bohy
    nutno zvolit zda vyznava mnohobozstvi a pak max 5 bohu klidne i vicero panteonu, ale pohanskych
    z:
        jmeno
        prezdivka
        prijmeni
        jmeno boha a popis + aktivni verici (denne xkrat se modli, pokud tak jak dlouho a kolikrat v roce, tydnu, jakym zpusobem, co u toho dela, obetiny (vyber z (chramu, ...)a zpusob obeti (veci, krve, deti, zvirata, jidlo, penize, prace, sebemrskacstvi))?)

atributes objekt
    z:
        bude mit meze z:
            race_basic_atributes
        bude extendovan o veci v hokus ci generator_atributu
        bude tam kolik ma karmy
        pred dotvorenim bude mit vypocet BS
            # TODO: u kazdeho meritu a flow bude mit za kolik to je, domyslet jak, nejlepe ciselnik
        bude mit moznost byt ovlivnen vybavou a magii, tzn. polozku temporary bonus
social objekt
    !!! nutno urcit spravne poradi kvuli navaznostem potom!!!
    z:  
        gender jen on ci ona, mozna kdyz padne jedno cislo ze 100, tak s obema pohlavnimi organy, jeden vsak zakrsly a nepouzitelny k reprodukci bez pomoci chirurgie
        sexual preferency
        relatives rodice stejna zeme 50%
        religion - rodice stejna vira 50% zaklad 51%+ ze veri -- dodelat zpusoby viry jako v sebe, v lidi... pro ateisty a poloateisty
        positive characteristic 2x random, not same 
        negative characteristic 2x random, not same 
        social class
        politicky nazor
family_background
    uzce propojeno s characteristics, nektere objekty vytahnout ven budou se pouzivat jak v characteristics, tak v fam background
    !!! muze byt umrti rodice!!!
    nutno vygenerovat zda mel dalsiho, zda mel nekoho koho prijmul na jeho misto, 
    stavy sirotku a pod, nutno rozvahu
    family ranking... propojit s ranking a to hodit nekam jinam, ranking bude stejne jako zde high, average
###### TODO: dodelat siblings
###### TODO: dodelat zbytek z ostaniho
social interactions
    uzce propojeno s characteristics, nektere objekty vytahnout ven budou se pouzivat jak v characteristics, tak v fam background



