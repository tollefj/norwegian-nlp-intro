# Natural Language Processing (NLP) - Språkprosessering

## Noen av fundamentene for NLP
- Tekstmanipulasjon
  - Hva definerer slutten på en setning
    - *?!*
  - Hva er et ord? Er det et substantiv, et verb? Er det en entitet?
    - Definere *tokens* (ordformer med tegnsetting)
      - *Tokenization*
  - Hva er en setning?
    - *I U.S.A har de...*
    - *f.eks*
- Leksikalske ressurser
  - leksikon
  - tekstkorpus (i dag har vi omtrent 109 GB tilgjengelig tekst, utbedret av nasjonalbiblioteket)
  - trebanker (grammatikk, syntakisk informasjon, ...)
  > Utvikles og vedlikeholdes bl.a. av [nasjonalbiblioteket](https://www.nb.no/sprakbanken/)
- Lingvistiske regler (substantiv, adjektiv, ...)
- Maskinlæringsalgoritmer som kan se mønster i språk

### Eksempel på trebank/syntakstre
![trebank](images/syntax2.png)

### Hva er disse annoteringene?
|Dependency Label|Grammatical Function|
|---|---|
|ADJ|Adjective|
|ADV|Adverbial|
|ADP|Adposition|
|APP|Apposition|
|ATR|Attribute|
|DET|Determiner|
|DOBJ|Direct object|
|FINV|Finite verb|
|FLAT|Flat structure|
|FOBJ|Formal object|
|FOPRED|Free object predicative|
|FRAG|Fragment|
|FSPRED|Free subject predicative|
|FSUBJ|Formal subject|
|FYLL|Filler|
|IK|Sentence-internal punctuation|
|INFV|Non-finite verb|
|INTJ/INTERJ|Interjection|
|IOBJ|Indirect object|
|IP|Sentence-separating punctuation|
|KONJ|Conjunction|
|KOORD|Coordination|
|NOUN|Noun|
|PROPN|Proper Noun|
|OPRED|Object predicative|
|PAR|Parenthetical expression|
|PSUBJ|Potential subject|
|PUTFYLL|Prepositional complement|
|REP|Disfluent repetition|
|SBU|Complementizer|
|SLETT|Disfluent restart|
|SPRED|Subject predicative|
|SUBJ|Subject|

## Hva gjør språkprosessering vanskelig?
Vi har store ressurser, som introdusert over. Hva gjør det vanskelig for Siri og Alexa å forstå oss? Hvorfor er ikke chatbotter som mennesker, og hvorfor er ikke oversettelser perfekte?

Kontekst. Kausalitet. Resonnement.

Språk er som et instinkt for mennesker. Vi *bare vet* hvordan et ord hører sammen i en setning, fra en utrolig tidlig alder. Dette hjelper oss til å forstå redundans (f.eks via en tautologi) og tvetydighet i språk. Spesielt vanskelig blir uttrykk:
- smør på flesk

Redundans og tautologier:

- en rund sirkel
- se med sine egne øyne

Tvetydighet:
- Stamme: 
  - trestamme
  - et taleproblem
  - å stamme fra noe / en folkegruppe
- Bane:
  - togbane
  - på banen (f.eks fotball)
  - en satellitt går i bane
  - å bane seg vei
- Bar
  - utested
  - måleenhet for trykk
  - granbar
  - naken; bar mage
  - ublandet; drikke whiskyen bar

Kontekst og ressonnement:
>*Jeg tok ut penger fra kontoen min i Sveits*

ble handlingen utført i sveits?
eller hører kontoen til en sveitsisk bank?


