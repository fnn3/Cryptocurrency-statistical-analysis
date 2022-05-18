# Cryptocurrency-statistical-analysis

1 UVOD
Pojavom svima dostupnih velikih količina podataka sve se češće upotrebljavaju statistički 
modeli kako bi se opisalo njihovo ponašanje i međusobna povezanost. U radu će se opisati 
glavne funkcije statističke analize, njihova implementacija i primjer korištenja na realnom 
problemu – kriptovalutama.
Kriptovalute su digitalni novac kreiran u digitalnom obliku kao sredstvo digitalne razmjene, a 
ono što ih razlikuje od običnog novca jest činjenica da ih ne nadzire središnja banka ili 
država, već se sve transakcije i vrijednosne izmjene jedinica kriptovaluta zapisuju u 
kriptiranom obliku u tzv. Blockchain. Upravo su zato vrlo popularne što potvrđuje i broj 
korisnika s digitalnim novčanicima koji u ovom trenutku prelazi 75 milijuna.
U radu će se opisati statistička analiza podataka na primjeru četiriju kriptovaluta: Bitcoina, 
Ethereuma, Cardana (Ada) i Iote. Bitcoin i Ethereum su odabrani kao najpopularnije 
kriptovalute, a Cardano i Iota kao njihovi potencijalni nasljednici. U radu se neće ulaziti u 
tehnologiju kriptovaluta, već će se statistički obraditi kretanje njihovih vrijednosti u razdoblju 
između 2017. i 2021. godine koristeći programski jezik Python.
Python je jedan od najpopularnijih programskih jezika opće namjene, a posebno se ističe u 
statističkoj analizi zbog svoje jednostavnosti, modularnosti i dostupnosti znanstvenih 
biblioteka kao što su matplotlib za iscrtavanje grafova ili scipy za složenije tehničko 
računanje. Tako će se, između ostalog, u radu prezentirati programski kod korišten u 
implementaciji funkcija statističe analize, prikazu grafova kretanja vrijednosti svake 
kriptovalute, njihove linearne regresije i korelacije između obrađenih kriptovaluta. 
Nakon uvoda opisan je programski jezik Python, potom su definirani pojmovi statističke 
analize podataka. Četvrto poglavlje bavi se analizom cijena kriptovaluta koje se dijeli na 
deskriptivnu analizu podataka, usporedbi kretanja cijena i opisivanjem podataka, nakon toga 
slijedi zaključak. 
2
2 PROGRAMSKI JEZIK PYTHON
2.1 Opis programskog jezika Python
Python je objektno orijentirani programski jezik najčešće korišten zbog svoje modularnosti i 
preglednosti koda, što ga čini savršenim alatom za brzo razvijanje aplikacija i metoda. 
Mogućnosti i alati Pythona su sveobuhvatne i široko korištene u opisivanju, rezimiranju i 
vizualizaciji podataka. Prednost Pythona je u tome što je Pythonov izvorni kod dostupan(eng. 
open source) što znači da svatko može iščitati, izmijeniti ili dopuniti izvorni kod u kojem je 
pisan, na taj se način Pythonov programski jezik konstantno usavršava i prilagođava 
potrebama korisnika. Sljedeća velika prednost Pythona su biblioteke (eng. libraries) koje se 
mogu preuzeti ili kreirati ovisno o potrebama. Osnovne karakteristike ovog programskog 
jezika, ujedno i njegove prednosti dakle jesu:
-preglednost
-modularnost
-dostupnost znanstvenih biblioteka (npr. numpy, scipy, matplotlib...)
-visoka razvijenost i prilagođenost korisniku
-intuitivnost sintakse
-konstantna nadogradnja i razvoj
Iako Python, zbog svojih mnogobrojnih biblioteka, već ima definirane funkcije za sve 
statističke pojmove korištene u ovom radu, u nastavku rada biti će prikazani pripadajući 
kodovi kojima je moguće navedene pojmove izračunati, odnosno definirat će se Python 
funkcije za svaki navedeni pojam.
3
2.2 Python libraries (biblioteke)
Jedna od glavnih prednosti Python programskog jezika predstavljaju njegove biblioteke (eng. 
libraries). Moduli i paketi omogućavaju lakši i brži razvoj programskog kôda, a u konačnici i 
programa. Napisano je mnogo modula tj. paketa za Python koji ubrzavaju razvoj programskog 
kôda jednostavnim pozivanjem unaprijed napisanih funkcija, razreda, konstanti. Moduli tj. 
paketi su organizirani u smislene cjeline radi što lakšeg snalaženja, ne samo prilikom 
korištenja već i radi što lakšeg traženja po dokumentaciji. Module i pakete koji dolaze sa 
standardnom instalacijom Pythona nazivamo standardnom bibliotekom. Ponekad su 
programerima potrebne funkcionalnosti koje ne dolaze s modulima tj. paketima iz standardne 
biblioteke. Za takve funkcionalnosti potrebno je poslužiti se Internetom i potražiti 
odgovarajuće pakete te ih instalirati na računalo na kojem će se program izvršavati.
Uvoz Python biblioteka vrši se pomoću funkcije „import“ kojom se poziva biblioteka koja se 
koristi u kodu. Ukoliko se iz biblioteka uvoze određene funkcije tada se funkcija „import“ 
koristi zajedno sa funkcijom „from“ tako da se upisuje prvo „from“, potom naziv izvorne 
biblioteke, nakon toga funkcija „import“ kojom se pozivaju određene funkcije koje se koriste 
u trenutnom kodu.
Slika 2.1-Python biblioteke
Pandas biblioteka najčešće je korištena biblioteka za analizu te iščitavanje podataka. Ovdje je 
korištena za iščitavanje podataka csv datoteke. Sljedeće korištena biblioteka je „NumPy“ koja 
se koristi za pretvaranje formata podataka u liste, tablice ili matrice. U ovom radu „NumPy“ 
je korištena za pretvaranje formata datuma iz „dataframe“ u listu te kreiranje liste vrijednosti 
x potrebne za definiranje linearne regresije. Biblioteka „Matplotlib“ korištena je u svrhu 
definiranja i iscrtavanja grafa te je iz biblioteke „Sklearn“ uvezena funkcija 
„LinearRegression“.
4
U ovom radu prikazano je kako biblioteke imaju veliku važnost kod korištenja Pythona u 
znanstvene svrhe zbog njihovih preddefiniranih funkcionalnosti koje uvelike olakšavaju 
programiranje i dobivanje korisnih rezultata.
Također, moguće je pozvati prethodno definirane funkcije u Python datoteci, odnosno, 
moguće je koristiti prijašnju datoteku kao biblioteku. Unutar kôda koji će biti korišten kao 
biblioteka potrebno je definirati funkcije koje se naknadno mogu uvoziti u ostale Python 
kodove pomoću funkcije „def():“. Na taj način moguće je jednom definirati sve funkcije i 
metode koje se s lakoćom mogu koristiti u svim budućim kodovima u kojima je potrebno 
definirati samo ulazne parametre.
Kod definiranja funkcije u Pythonu, unutar zagrada nakon upisivanja „def“ upisuju se ulazni 
parametri, kod naknadnog korištenja definirane funkcije potrebno je dati jednak broj ulaznih 
parametara ukoliko nisu unaprijed definirane standardne vrijednosti. U sljedećem redu, nakon 
dvotočke i uvučeno, upisuje se dio koda koji obrađuje ulazne parametre sukladno potrebama. 
Naredbom „return“ definiramo izlazne parametre iste funkcije koju želimo definirati. 
Sljedeći kod dan je kao primjer definiranja jedne funkcije koja se naknadno koristi unutar 
funkcije „print()“:
def prosj(xsr):
 val_sum = sum(xsr)
 return val_sum / len(xsr)
list = [1,5,56,33,9,18]
print("Prosjek :",prosj(list))
U ovom primjeru definirana je funkcija aritmetičke sredine „prosj“ koja kao ulazni parametar 
koristi skup brojeva. Ulazni parametar unutar funkcije obilježava se kao varijabla „xsr“ od 
koje, u varijabli „val_sum“ izračunava sumu. Izlazni parametar jednak je omjeru varijable 
„val_sum“ i broja podataka unutar ulaznog parametra izračunatog pomoću funkcije 
„len(xsr)“. 
5
3 STATISTIČKA ANALIZA PODATAKA
3.1 Uvod u statističku analizu
Statistika je grana primijenjene matematike koja se bavi prikupljanjem, uređivanjem, 
analizom i tumačenjem podataka kao i donošenjem zaključaka o pojavama i procesima koje ti 
podatci predočuju.. Osnovna podjela odnosi se na deskriptivnu i inferencijalnu. Dok se 
deskriptivna statistika bavi mjerama centralne tendencije, varijabiliteta te vizualnim prikazima 
istih statističkih vrijednosti, inferencijalna statistika bavi se postavljanjem i provjerom 
postavljenih hipoteza pomoću statističkih testova. Općenito statistika se bavi donošenjem 
zaključaka iz velikih skupova podataka i predviđanjem mogućih budućih kretanja podataka i 
njihove značajnosti, što znači da se temelji na podacima koji ukazuju na određena obilježja, 
odnosno mjere svojstava pojava ili procesa, podaci se dobivaju mjerenjem ili pokusima, a 
mjere se dobivaju statističkom analizom.
U ovom radu obradit će se, i definirati, svi osnovni pojmovi deskriptivne statistike kao što su: 
mjere centralne tendencije, varijabilnosti i grafički prikazi podataka, te, na primjeru 
kriptovaluta, uz pomoć navedenih alata, napraviti ststističku analizu kretanja cijena, obraditi 
korelacije između dobivenih skupova podataka te postaviti i testirati nekoliko hipoteza. 
6
3.2 Aritmetička sredina
Aritmetička sredina ili srednja vrijednost predstavlja sumu svih podataka podijeljenu s 
ukupnim brojem podataka. Ona je jedan od pokazatelja centralne tendencije. Iako je 
aritmetička sredina jedna od najkorištenijih vrijednosti koje se izračunavaju na temelju 
podataka ona ima svoje mane te može biti neprecizan pokazatelj centralne tendencije, 
najčešće u slučajevima ekstremnih graničnih, minimalnih ili maksimalnih, vrijednosti. 
Formula za izračunavanje aritmetičke sredine je sljedeća:
𝑥̅=
𝑥1 + 𝑥2 + 𝑥3 + 𝑥4 + ⋯ + 𝑥𝑛
𝑛
(3.1)
Gdje je {x1,...,xn} promatrani skup podataka, a n broj podataka u skupu.
U Pythonu, aritmetičku sredinu skupa podataka danog poljem xsr možemo izračunati na 
sljedeći način:
def prosj(xsr):
 val_sum = sum(xsr)
 return val_sum / len(xsr)
3.3 Medijan
Medijan predstavlja sredinu distribucije podataka, odnosno drugi kvartil. Medijan je 
pozicijska srednja vrijednost i time uklanja utjecaj ekstremnih vrijednosti već prikazuje 
srednju vrijednost liste podataka. Ukoliko lista podataka ima neparan broj članova, medijan će 
biti središnji član ukoliko su podaci poredani po veličini, u suprotnome, medijan će prikazati 
srednju vrijednost između dva središnja člana. Definirana funkcija za dobivanje medijana u 
Pythonu je sljedeća:
def median(med):
 med = list.sort()
 if len(med) % 2 == 0:
 i = round((len(med)+1)/2)
 j = i - 1
 return (med[i] + med[j]) / 2
 else:
 k =round(len(med) / 2)
 return med[k]
7
3.4 Mod
Mod predstavlja vrijednost koja se najčešće pojavljuje u određenom skupu podataka. On je 
tjemena vrijednost određenog skupa. Ukoliko se vrijednosti ne ponavljaju unutar određenog 
skupa tada ta lista nema mod, s druge strane, ako skup ima više tjemenih vrijednosti tada te 
vrijednosti predstavljaju mod tog polimodalnog skupa. Definirana funkcija za mod u Python 
programskom jeziku je sljedeća:
def mod(mod):
 
 dict_vrij = {i: mod.count(i) for i in mod}
 
 max_list = [k for k, v in dict_vrij.items() if v ==
max(dict_vrij.values())]
 
 return max_list
3.5 Varijanca
Varijanca je vrijednost koja prikazuje koliko su podaci raspršeni oko prosjeka tog skupa. 
Najčešće korištena mjera rasapa podataka. Varijanca predstavlja vrijednost sume kvadrata 
odstupanja svih podataka od njihove srednje vrijednosti podijeljene s brojem podataka.
Formula za izračunavanje varijance populacije je sljedeća:
𝑆
2 =
∑(𝑥𝑖 − 𝑥̅)
2
𝑛
(3.2)
Gdje je {x1,...xn} dani skup podataka, 𝑥̅njegova aritmetička sredina, a n broj podataka.
Varijanca za skup podataka dan listom var može se izračunati pomoću sljedećeg Pythonovog 
koda:
def varijanca_POP(var):
 prosj_vrij = prosj(var)
 brojnik = 0
 for i in var:
 brojnik += (i-prosj_vrij)**2
 nazivnik = len(var)
 return brojnik / nazivnik
8
3.6 Standardna devijacija
Standardna devijacija prikazuje, kao varijanca, stupanj rasapa podataka, odnosno koliko su 
podaci raspršeni oko aritmetičke sredine. Ona predstavlja pozitivnu vrijednost drugog 
korijena varijance. Aritmetička sredina daje nam broj koji se često u teorijskom i praktičnom 
pogledu smatra najbližim podatcima. S druge strane, standardna devijacija kaže nam kolika je 
ta bliskost. Što je s manji, to je 𝑥̅ bliži podacima. Ako je standardna devijacija (s) = 0, sve 
vrijednosti su iste, a aritmetička sredina (𝑥̅) jednaka je svim vrijednostima. Formula za 
izračunavanje standardne devijacije je sljedeća:
𝑆 = √
∑(𝑥𝑖−𝑥̅)
2
𝑛
(3.3)
3.7 Koeficijent varijacije
Koeficijent varijacije je relativna vrijednost koju dobivamo kao omjer standardne devijacije i 
srednje vrijednosti uzorka ili populacije. Predstavlja relativnu mjeru rasapa podataka oko 
aritmetičke sredine i služi za procjenu reprezentativnosti aritmetičke sredine kao centralne 
tendencije skupa podataka. Ako je koeficijent varijacije manji od 30%, smatramo da je 
aritmetička sredina reprezentativna, u suprotnom da nije. Koeficijent nailazi na problem sa 
vrijednostima aritmetičke sredine oko nule.
def koef_var_POP(coefvar):
 return stand_dev_POP(coefvar) / prosj(coefvar)
def koef_var_UZ(coefvar):
 return stand_dev_UZ(coefvar) / prosj(coefvar)
9
3.8 Regresijska analiza
Regresijski modeli imaju dugu i zanimljivu tradiciju u statistici, gdje se regresija, pored 
korelacijske analize, koristi kako bi se analizirali i objasnili odnosi izmedu dva skupa 
varijabli. Statistika je razvila niz različitih regresijskih metoda, čija primjenjivost ovisi o vrsti 
podataka i pretpostavkama koje o podacima možemo napraviti. 
Kod statističkog modeliranja regresijska analiza predstavlja vrlo bitan alat koji je najčešće 
korišten kako bi se prikazao trend kretanja podataka, odnosno, povezanost jedne zavisne sa 
jednom ili više nezavisnih varijabli. Regresijska analiza daje nam mogućnost da kvantitativno 
prikažemo međuovisnost varijabli. U ovom radu korištena je linearna regresija, takva regresija 
opisana je jednadžbom pravca.
𝑟𝑒𝑔(𝑥) = 𝑎𝑥 + 𝑏 (3.4)
Varijable koje čine vektor x nazivaju se nezavisne, prediktorske varijable ili regresori, dok se 
varijable y nazivaju zavisna, kriterijska ili izlazna varijabla. U kontekstu strojnog učenja, 
varijabla x je vektor značajki, koje mogu biti kategoričke ili numeričke, u prvom slučaju 
značajke će se tipično kodirati tako da je svaka vrijednost kategoričke značajke prikazana
binarnom značajkom. Linearna regresija je model regresije kod kojeg je funkcija linearna 
kombinacija ulaznih značajki. Definiranje parametara a,b jednadžbe pravca određuje se 
najčešće pomoću metode najmanjih kvadrata, i ti su parametri jednaki:
 
𝑎 =
∑ 𝑥𝑖𝑦𝑖−𝑛∗𝑥̅∗𝑦̅
𝑛
𝑖=1
∑ 𝑥𝑖
𝑛 2
𝑖=1 −𝑛∗𝑥̅
2
, 𝑏 = 𝑦̅ − 𝑎 ∗ 𝑥̅ (3.5)
𝑥𝑖
, 𝑦𝑖
: predstavlja vrijednosti x i y osi i − tog elementa
𝑥̅, 𝑦̅: predstavlja srednje vrijednosti za x i y os
𝑛: predstavlja broj vrijednosti u skupu podataka
Veličina a predstavlja regresijski koeficijent, on predstavlja nagib pravca linearne regresije, 
odnosno prikazuje za koliko se prosječno mijenja vrijednost zavisne varijable za jediničnu 
promjenu nezavisne varijable. 
10
Aproksimacija linearnom regresijom ima brojne prednosti te je često korišteni alat kod 
statističke analize te najčešće vrlo dobro predviđa kretanje nezavisnih varijabli, međutim 
postoje slučajevi u kojima predviđanje libnearnom regresijom može dati pogršnu predodžbu o 
kretanju analiziranih varijabli. Na sljedećim slikama prikazana su dva slučaja, jedan slučaj 
kvalitetne aproksimacije linearnom regresijom te drugi slučaj kod kojeg ista aproksimacija ne 
daje točnu predodžbu kretanja podataka. U tim slučajevima najbolje je koristiti polinomnu 
regresiju.
Slika 3.1- Primjer regresijske analize 1 ([14])
Slika 3.2- Primjer regresijske analize 2 ([14])
11
3.9 Kovarijanca
Kovarijanca predstavlja povezanost promjena dva skupa podataka, odnosno koliko su 
međusobno povezane dvije varijable, za razliku od varijance koja opisuje osciliranje od 
srednje vrijednosti jedne varijable. Za ovaj slučaj potrebno je imati dva skupa podataka 
kojima je moguće analizirati međuzavisnost. Kada je kovarijanca negativna znači da porastom 
vrijednosti jedne varijable vrijednosti druge padaju, a u slučaju da je kovarijanca pozitivna
rastom vrijednosti jedne varijable rastu i vrijednosti druge, kovarijanca oko 0 govori da 
analizirane vrijednosti skupova nisu međusobno povezane.
Kovarijanca ima veću pozitivnu vrijednost za svaki par vrijednosti skupova koji se razlikuju
od vlastitih srednjih vrijednosti u istom smjeru, te više negativnu vrijednost za svaki par koji 
odstupa od vlastitih srednjih vrijednosti u suprotnom smjeru što je vidljivo prema 
matematičkom izrazu danom za skup od N vrijednosti dviju varijabli:
𝑐𝑜𝑣𝑥,𝑦 =
∑(𝑥𝑖 − 𝑥̅)(𝑦𝑖 − 𝑦̅)
𝑁 − 1
(3.6)
Definiranje funkcije kovarijance u Pythonu:
def kovarijanca(cov):
 list_1 = cov[0]
 list_2 = cov[1]
 list_1_prosj = prosj(list_1)
 list_2_prosj = prosj(list_2)
 brojnik = 0
 
 for i in range(len(list_1)):
 brojnik += (list_1[i]-list_1_prosj)*(list_2[i]-list_2_prosj)
 nazivnik =len(list_1) - 1
 return brojnik / nazivnik
Kovarijanca se najčešće koristi za izračunavanje korelacije koja nam vjernije prikazuje 
povezanost dva skupa podataka na skali od -1 do 1 s tim da su podaci s korelacijom -1 
obrnuto proporcionalni.
12
3.10 Koeficijent korelacije
Koeficijent korelacije izražava ovisnost između statističkih varijabli. Kod linearne korelacije 
jakost korelacije izražena je koeficijentom r, koji može imati vrijednosti između -1 i +1. 
Koeficijent korelacije jednak je +1 kada je vjerojatnost da određenoj vrijednosti jedne 
varijable odgovara određena vrijednost druge varijable jednaka 1; r = 0 kada je navedena 
vjerojatnost jednaka 0, odnosno kada nema nikakve linearne ovisnosti između varijabla. U 
slučaju da je r = –1 tada je navedena vjerojatnost opet jednaka 1, ali je ovisnost u obliku 
obrnute proporcionalnosti.
Najčešće se koriste:
• Pearsonov koeficijent korelacije ili Produkt-moment koeficijent korelacije (r),
• Spearmanov koeficijent korelacije ili koeficijent rang korelacije (ρ),
Interpretacija koeficijenta korelacije
Najviše ovisi o kontekstu, o prirodi pojava. Okvirne granice su:
• od 0.00 do ±0.20 ➩ neznatna povezanost
• od ±0.20 do ±0.40 ➩ lagana povezanost
• od ±0.40 do ±0.70 ➩ značajna povezanost
• od ±0.70 do ±1.00 ➩ visoka ili vrlo visoka povezanost
Definiranje funkcije korelacije u Pythonu:
def koef_korelacije(kor):
 list_1 = kor[0]
 list_2 = kor[1]
 list_1_sd = stand_dev_UZ(list_1)
 list_2_sd = stand_dev_UZ(list_2)
 
 brojnik = kovarijanca(kor)
 nazivnik = list_1_sd * list_2_sd
 
 return brojnik / nazivnik
13
3.11 Matrica kovarijanci i korelacijska matrica
Nerijetko je korisno kovarijance i korelacije više varijabli zapisati u matričnom obliku. Time 
se olakšava prikaz i daljnje korištenje podataka. Ako za slučajni vektor Z = [X, Y] postoje 
matematička očekivanja E(X) i E(Y) , zapisivat ćemo ih u vektorskom obliku kao [E(X), 
E(Y)] i zvati očekivanje slučajnog vektora Z = [X, Y] . Varijance i kovarijancu također 
zapisujemo matrično. Označimo li E(Z) = [E(X), E(Y) ] tada je
𝐸(𝑍 − 𝐸𝑍)(𝑍 − 𝐸𝑍) = [
𝐸(𝑋 − 𝐸𝑋)
2 𝐸(𝑋 − 𝐸𝑋)(𝑌 − 𝐸𝑍)
𝐸(𝑋 − 𝐸𝑋)(𝑌 − 𝐸𝑍) 𝐸(𝑌 − 𝐸𝑌)
2
] = [
𝑉𝑎𝑟(𝑋) 𝐶𝑜𝑣(𝑋, 𝑌)
𝐶𝑜𝑣(𝑌, 𝑋) 𝑉𝑎𝑟(𝑌)
] 
(3.7)
Matricu 𝐸(𝑍 − 𝐸𝑍)(𝑍 − 𝐸𝑍) zovemo matrica kovarijanci slučajnog vektora [X,Y]. Matrica 
kovarijanci je simetrična zbog činjenice da je Cov(X,Y) = Cov(Y,X).
Ukoliko se matrica kovarijanci standardizira tako da dobivene vrijednosti variraju u rasponu od [-1,1]
što dobijemo standardiziranjem vektora pomoću formule
𝑍𝑠 = [
𝑋−𝜇𝑥
𝜎𝑥
,
𝑌−𝜇𝑦
𝜎𝑥
] (3.8)
Tada se dobivena matrica naziva korelacijska matrica i označava se sa Corr(X,Y).
𝐶𝑜𝑟𝑟(𝑋, 𝑌) = [
1 𝜌𝑥,𝑦
𝜌𝑦,𝑥 1
] (3.9)
Korelacijska matrica vektora 𝑍 = [𝑋1, …, 𝑋𝑛] definirana je:
𝐶𝑜𝑟𝑟(𝑍) = [
1 ⋯ 𝐶𝑜𝑟𝑟(𝑋1, 𝑋𝑛)
⋮ ⋱ ⋮
𝐶𝑜𝑟𝑟(𝑋𝑛,𝑋1) ⋯ 1
] (3.10)
14
4 STATISTIČKA ANALIZA CIJENA KRIPTOVALUTA
4.1 Opis problema
U ovom će se poglavlju prikazati dio mogućnosti Pythona u statističkoj analizi na primjeru
kretanja cijena 4 popularne kriptovalute. Odabrane kriptovalute su: Bitcoin, Ethereum, 
Cardano (Ada) i Iota. Navedene kriptovalute odabrane su zbog popularnosti i specifičnosti 
tehnologija korištenih u razvoju. 
Sa interneta su preuzeti podaci za svaku kriptovalutu te prilagođen raspon vremena kako bi se 
moglo usporedno obraditi sve kriptovalute. Raspon odgovara najkraće postojećoj kriptovaluti 
(Cardano) koja je izašla na tržište 2.10.2017. Zadnji dostupni podatak s navedenog izvora je 
27.2.2021. te to predstavlja kraj vremenskog raspona podataka. Uvezene tablice imaju 
podatke definirane japanskim svijećama, odnosno imaju 4 vrijednosti za svaki dan: otvaranje 
tržišta, najviša cijena, najniža cijena i zatvaranje tržišta. Budući da su ti podaci predviđeni za 
tržište dionicama kod kojih imamo vrijeme otvorenog i zatvorenog tržišta, za razliku od 
kriptovaluta kojima se trguje 24 sata u danu, nisu potrebni svi podaci. Uzima se vrijednost 
otvaranja tržišta, odnosno vrijednost kriptovalute na određeni dan u 00:00 sati. 
Podaci preuzeti s interneta dani su u .csv obliku odvojeni zarezom. Podaci sadrže podatke 
otvaranja i zatvaranja svakog dana, najviše i najniže cijene tog dana, te volumen trgovanja i 
ukupni udio na tržištu (market capitalization).
Slika 4.1-Ulazni podaci
15
4.2 Deskriptivna analiza podataka
U ovom poglavlju obradit će se deskriptivna analiza na primjeru jedne kriptovalute (CardanoAda). Za početak potrebno je podatke svrstati u razrede kako bi se odredila distribucija 
frekvencija, potom će biti prikazan histogram frekvencija, nakon toga prikazat će se 
aritmetička sredina, medijan i kvartili. 
Za prikaz histograma odabrano je 30 razreda jednakih širina. Budući da su širine jednake, a 
promjene relativne uz cijenu valute razumljivo je pretpostaviti da će većina podataka pripasti 
u prvih nekoliko širina zbog toga što su u tim slučajevima apsolutne promjene vrijednosti 
manje nego kod slučaja s većom cijenom,a širine razreda jednake. Iz tog razloga prikazat će 
se i relativne vrijednosti, odnosno histogram verižnih indeksa u nastavku rada. Za prikaz 
distribucije frekvencija korišten je sljedeći kod:
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
dataADA = pd.read_csv("Data/coin_Cardano.csv")
ADA = dataADA.Open.to_numpy()
num_bins = 30
n, bins, patches = plt.hist(ADA, num_bins)
plt.show()
Slika 4.2- Distribucija frekvencija-ADA
16
Kako bi se dobio uvid u kretanja podataka potrebno je odrediti pokazatelje centralne 
tendencije i rasapa podataka. Pomoću sljedećeg koda odredit će se prosjek, varijanca, medijan 
te prvi i treći kvartili:
avADA = np.average(ADA)
varADA = np.var(ADA)
sdADA = np.std(ADA)
vcADA = sdADA/avADA*100
medADA = np.median(ADA)
q1ADA = np.quantile(ADA,0.25)
q3ADA = np.quantile(ADA,0.75)
print("prosjek=",avADA,"\nvarijanca=",varADA,"\nstandardna 
devijacija=",sdADA,"\nkoeficijent 
varijacije=",vcADA,"%","\nmedijan=",medADA,"\nQ1=",q1ADA,"\nQ3=",q3ADA)
Ovdje navedeni kod daje sljedeći izlaz:
Slika 4.3- Pokazatelji varijabilnosti- ADA
Na gornjoj slici je vidljivo kako aritmetička sredina nije reprezentativni pokazatelj centralne 
tendencije s obzirom da koeficijent varijacije ima vrlo visoku vrijednost. 
Podatke ispisane gore navedenim kodom moguće je grafički prikazati pomoću „Matplotlib“ 
funkcije „boxplot“ koja grafički prikazuje prvi i treći kvartil, maksimalne i minimalne 
vrijednosti te medijan. „Boxplot“ izgledom podsjeća na japannske svijeće koje se koriste kod 
trgovanja dionicama s nekim ključnim razlikama. Kod „boxplot-a“ pravokutnik predstavlja 
50% podataka, odnosno prvi i treći kvartil, dok linije koje iz njega izlaze predstavljaju
minimum i maksimum, dok horizontalna linija predstavlja medijan, odnosno središnju 
vrijednost.
17
Prvi „boxplot“ prikaz generiran je za kompletan skup podataka, što je vidljivo na sljedećoj 
slici. On prikazuje kvartile i medijan dobivene na prethodnoj slici. Sljedeći „boxplot“ 
dijagram prikazuje iste podatke na godišnjoj bazi. Kod pomoću kojeg se ispisuju navedeni 
dijagrami je sljedeći:
A1=ADA[:91]
A2=ADA[91:457]
A3=ADA[457:823]
A4=ADA[823:1189]
A5=ADA[1189:1245]
adata = [A1,A2,A3,A4,A5]
xis =[1,2,3,4,5]
xos = [2017,2018,2019,2020,2021]
plt.boxplot(adata)
plt.title("Box-plot ADA")
plt.xticks(xis,xos)
plt.show()
plt.boxplot(ADA)
plt.show()
Slika 4.4- Box plot- ADA
Slika 4.5- Box plot ADA godišnje
18
4.3 Iscrtavanje grafova linearne regresije
Za bolji uvid u problematiku potrebno je iscrtati grafove kretanja cijena za određeni period, na 
istom grafu iscrtati će se i linearna regresija kako bi se pokazao trend kretanja cijene.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
dataADA = pd.read_csv("Data/coin_Cardano.csv")
opADA = dataADA.Open.to_numpy()
date1 = dataADA.Date.to_numpy()
datumi = []
for i in date1:
 datum_i_vrijeme=i.split(" ")
 datumi.append(datum_i_vrijeme[0])
x = np.arange(1245).reshape(-1, 1)
reg = LinearRegression().fit(x, opADA)
y = reg.predict(x)
fig, ax = plt.subplots()
ax.plot(date1,opADA,"r")
ax.plot(y)
ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, 
len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(dat
umi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])
plt.title("Linearna regresija ADA cijene")
plt.legend(["ADA open cijena","Linearna regresija"])
plt.ylabel("USD")
plt.show()
Gore navedeni izvorni kod iscrtava graf sa pripadajućom linijom linearne regresije. 
19
Na sljedećim slikama prikazat će se rezultati koda s prethodne stranice za svaku kriptovalutu, 
odnosno graf kretanja cijena sa pripadajućim linearnim regresijama:
Slika 4.6- Graf lin. regresije BTC
Slika 4.7- Graf lin. regresije ETH
20
Slika 4.8- Graf lin. regresije ADA
Slika 4.9- Graf lin. regresije ADA
Prema ovim slikama vidljivo je da linearna regresija nije dobar prediktor cijene zbog 
ekstremnih pomaka cijena koje su uzrokovane brojnim vanjskim faktorima koji nisu, i ne 
mogu biti, uračunati u statističku analizu. Vanjski faktori koji utječu na veće oscilacije cijena 
su: novosti vezane uz razvoj kriptovalute, nadogradnje, informatički napadi, stanje globalnog 
tržišta i ostali.
21
4.4 Iscrtavanje krivulja na usporednom grafu i matrica korelacija
Kako bi se vizualiziralo postojanje korelacija između kretanja cijene pojedinih kriptovaluta 
iscrtat će se sve vrijednosti cijena na jednome grafu. Budući da vrijednosti pojedinih 
kriptovaluta imaju različite redove veličine za kreiranje sljedećeg dijagrama koristila se 
logaritamska skala. Također, za potrebe usporedbe potrebno je ograničiti raspon datuma 
prema najkraće postojećoj valuti (Cardano-Ada). Paralelno sa iscrtavanjem usporednog grafa 
sljedeći kod definira matricu korelacija.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
dataBTC = pd.read_csv("Data/coin_Bitcoin.csv")
dataADA = pd.read_csv("Data/coin_Cardano.csv")
dataIOTA = pd.read_csv("Data/coin_Iota.csv")
dataETH = pd.read_csv("Data/coin_Ethereum.csv")
opBTCdf = dataBTC.Open.to_numpy()
opADAdf = dataADA.Open.to_numpy()
opIOTAdf = dataIOTA.Open.to_numpy()
opETHdf = dataETH.Open.to_numpy()
dateBTC = dataBTC.Date
dateADA = dataADA.Date
dateIOTA = dataIOTA.Date.to_numpy()[110:]
opBTC_n = opBTC[1617:]
opIOTA_n = opIOTA[110:]
opETH_n = opETH[786:]
data= {'BTC': opBTC_n,
 'ETH': opETH_n,
 'IOTA': opIOTA_n,
 'ADA': opADA,
 }
df = pd.DataFrame(data,columns=['BTC','ETH','IOTA','ADA'])
corrMatrix = df.corr()
print (corrMatrix)
datumi = []
for i in dateIOTA:
 datum_i_vrijeme=i.split(" ")
 datumi.append(datum_i_vrijeme[0])
x = np.arange(1245).reshape(-1, 1)
22
reg1 = LinearRegression().fit(x, opADA)
reg2 = LinearRegression().fit(x, opIOTA_n)
reg3 = LinearRegression().fit(x, opBTC_n)
reg4 = LinearRegression().fit(x, opETH_n)
y1 = reg1.predict(x)
y2 = reg2.predict(x)
y3 = reg3.predict(x)
y4 = reg4.predict(x)
#print(x)
fig, ax = plt.subplots()
ax.plot(dateIOTA,opADA,"r")
ax.plot(opBTC_n,"b")
ax.plot(opIOTA_n,"orange")
ax.plot(opETH_n,"g")
ax.set_yscale('log')
ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, 
len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(dat
umi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])
plt.title("Usporedni graf (Logaritamska skala)")
plt.legend(["ADA","BTC","IOTA","ETH"])
plt.ylabel("USD")
plt.show()
23
Ovdje navedeni kod ima dva izlaza: iscrtani graf koji prikazuje kretanja cijena u periodu od 
10.2.2017 do 27.2.2021. te pisane vrijednosti matrice korelacija. Matrica korelacija simetrična 
je s obzirom na dijagonalu te su joj vrijednosti dijagonale jednake 1 zbog toga što dijagonalne 
vrijednosti predstavljaju korelaciju vrijednosti valute same sa sobom. Rezultati koda za 
usporedbu kriptovaluta dani su na sljedeće dvije slike:
Slika 4.10- Usporedni graf (logaritamska skala)
Slika 4.11- Tablica korelacija
Ovdje prikazana matrica korelacije daje nam podatke o stupnju povezanosti kretanja cijena 
kriptovaluta. Ovdje je vidljiv najviši stupanj korelacije između Ade i Ethereuma, sljedeći je 
između Bitcoina i Ethereuma. Zanimljiv podatak je također da usprkos visokoj povezanosti 
24
Ade i Ethereuma i visokoj povezanosti Ethereuma i Bitcoina, Ada i Bitcoin nemaju toliko 
visok stupanj povezanosti. Taj podatak pokazuje da različiti čimbenici stimuliraju promjenu 
cijene za Ethereum i Bitcoin u odnosu na promjenu Ade i Ethereuma, odnosno, da ukoliko 
neki čimbenik istovremeno utječe na Adu i Ethereum, manje je izgledno da će to stimulirati i 
pomak Bitcoina. Na sljedećim slikama prikazati će se usporedni dijagrami kretanja cijena 
podijeljenih s prosječnom cijenom kako bi stupanj korelacije bio vidljiviji. 
Slika 4.12- Usporedni graf u omjeru 1
Slika 4.13- Usporedni graf u omjeru 2
25
Slika 4.14-Usporedni graf u omjeru 3
Radi usporedbe dana je i slika usporedbe sve tri kriptovalute na jednom dijagramu, kako 
bismo mogli vizualizirati na kojim točkama se valute s visokim stupnjem povezanosti počinju 
razlikovati. Sljedećom slikom prikazati će se usporedni dijagram Iote i Bitcoina kako bi se 
prikazao dijagram dvije valute s niskom stupnjem korelacije (0.15 – iz matrice korelacija)
Slika 4.15- Usporedni graf u omjeru 4
26
4.5 Verižni indeksi
Verižni indeksi predstavljaju relativne brojeve u postocima koji pokazuju promjene stanja u 
uzastopnim razdobljima, odnosno pokazuju za koji postotak se vrijednost pojave u jednom 
razdoblju promijenila u odnosu na prethodno razdoblje. Verižni indeksi koriste se kod 
statističke analize vremenskih nizova te predstavljaju individualne indekse sa promjenjivom 
bazom budući da je baza indeksa prethodno razdoblje.
Verižni indeksi računaju se formulom:
𝑉𝑖 =
𝑌𝑖
𝑌𝑖−1
∗ 100, 𝑖 = 1,2, … , 𝑛 (4.1)
Gdje je:
𝑉𝑖
: Verižni indeks i − tog elementa
𝑌𝑖
: Cijena i − tog dana
𝑌𝑖−1: Cijena prethodnog dana od promatranog
Za izračunavanje verižnih indeksa pojedinih kriptovaluta potrebno je ispisati gore navedenu 
formulu u obliku Python koda za svaku kriptovalutu. Dio potreban za izračunavanje verižnih 
indeksa je sljedeći:
verADA = []
for index,i in enumerate(ADA):
 if ADA[index]==0:
 rez=100
 else:
 rez = (ADA[index]/ADA[index-1])*100
 verADA.append(rez)
Dobivene vrijednosti raspoređene u 100 razreda jednakih širina iscrtati će se na histogramu 
frekvencija pomoću sljedećeg koda:
num_bins = 100
fig,ax = plt.subplots()
n, bins, patches = plt.hist(verADA, num_bins)
ax2=ax.twinx()
plt.show()
27
Kreiran je histogram frekvencija verižnih indeksa koji je prikazan na sljedećoj slici:
Slika 4.16- Distribucija frekvencija verižnih indeksa-ADA
Iz ovdje prikazanog histograma vidljivo je da je možda moguće aproksimirati verižne indekse 
pomoću normalne razdiobe. Za potrebe opisivanja razdiobe frekvencija verižnih indeksa 
normalnom distribucijom potrebno je odrediti aritmetičku sredinu i standardnu devijaciju 
dobivenog skupa podataka verižnih indeksa. Nakon određivanja, ti podaci koriste se kao 
ulazni parametri za Pythonovu „scipy.stats“ funkciju „norm“ koja pomoću tih parametara 
generira normalnu razdiobu.
sdADA = np.std(verADA)
avADA = np.average(verADA)
x_axis = np.arange(0, 100, 1)
print("prosjek verižnih indeksa=",avADA,"\nstandardna devijacija verižnih 
indeksa=",sdADA)
norm = norm.pdf(x_axis, avADA, sdADA)
plt.plot(norm)
plt.show()
28
Ulazni parametri (aritmetička sredina i standardna devijacija) za generiranje krivulje 
normalne razdiobe dani su na sljedećoj slici:
Slika 4.17- Parametri distribucije (ADA)
Na sljedećoj slici prikazana je dobivena normalna razdioba za koju se pretpostavlja da opisuje 
verižne indekse promjene cijena na skupu podataka Cardano-Ada kriptovalute:
Slika 4.18- Krivulja normalne razdiobe (ADA)
29
Radi (barem odokativne) provjere kvalitete opisivanja verižnih indeksa dobivenom 
normalnom distribucijom, izračunat ćemo teorijske frekvencije verižnih indeksa pod 
pretpostavkom da se ravnaju po dobivenoj normalnoj razdiobi.Kako bi se dobila teorijska 
distribucija frekvencija potrebno je koristiti jednake razrede kao kod histograma stvarnih 
frekvencija. Kod korišten za računanje distribucije teorijskih frekvencija dan je u nastavku:
#Računanje verižnih indeksa
num_bins=100
verADA = []
for index,i in enumerate(ADA):
 if ADA[index]==0:
 rez=100
 else:
 rez = (ADA[index]/ADA[index-1])*100
 verADA.append(rez)
sdADA = np.std(verADA)
avADA = np.average(verADA)
print("prosjek verižnih indeksa=",avADA,"\nstandardna devijacija verižnih 
indeksa=",sdADA)
#histogram stvarnih frekvencija
n, bins, patches = plt.hist(verADA, num_bins)
# distribucija teorijskih frekvencija
hiADA = []
for index,i in enumerate(bins):
 if index == 0:
 rez = round(scipy.stats.norm(avADA, sdADA).cdf(i)* len(verADA))
 else:
 rez = round((scipy.stats.norm(avADA, sdADA).cdf(i) -
scipy.stats.norm(avADA, sdADA).cdf(bins[index - 1])) * len(verADA))
 hiADA.append(rez)
plt.plot(bins,hiADA)
plt.show()
30
Usporedba empirijske i teorijske distribucije frekvencija verižnih indeksa prikazana je na 
sljedećoj slici:
Slika 4.19- Histogram frekvencija i distribucija (ADA)
Pomoću istog postupka na sljedećim slikama prikazani su histogrami frekvencija verižnih 
indeksa i pretpostavljenih distribucija, zajedno sa pripadajućim parametrima za izračunavanje 
teorijskih distribucija frekvencija za Bitcoin, Ethereum i Iotu:
Slika 4.20- Histogram frekvencija i distribucija (BTC)
Slika 4.21-Parametri distribucije (BTC)
31
Slika 4.22-Histogram frekvencija i razdioba (ETH)
Slika 4.23- Parametri distribucije (ETH)
Slika 4.24- Histogram frekvencija i distribucija (IOTA)
Slika 4.25- Parametri distribucije (IOTA)
32
Na prethodnim slikama vidljivo je kako aproksimacija s navedenim ulaznim parametrima za 
normalnu razdiobu nije pretjerano dobar pokazatelj distribucije frekvencija. To je iz razloga
što je za izračunavanje standardne devijacije korišten cijeli skup podataka uključujući 
ekstremne vrijednosti koje znatno povećavaju izračunatu standardnu devijaciju. Kako bi se 
postigla bolja podudarnost teorijske razdiobe i dobivenih podataka očistiti će se skup od 
ekstremnih vrijednosti prije izračunavanja novih ulaznih parametara normalne distribucije. 
Za dobivanje novog skupa „očišćenih“ podataka, korišten je raspon od tri standardne 
devijacije s obe strane aritmetičke sredine prvotno dobivenih parametara razdiobe s obzirom 
da, kod normalne razdiobe, unutar tri standardne devijacije udaljenosti od aritmetičke sredine 
spada 99% podataka. Kod pomoću kojega je sužen raspon podataka verižnih indeksa dan je u 
nastavku:
verADA2 = []
for i in verADA :
 if i>(avADA-3*sdADA) and i<(avADA+3*sdADA):
 verADA2.append(i)
sdADA2 = np.std(verADA2)
avADA2 = np.average(verADA2)
print("Ulazni parametri nakon druge iteracije-ADA","\nprosjek verižnih 
indeksa=",avADA2,"\nstandardna devijacija verižnih indeksa=",sdADA2)
hiADA2 = []
for index,i in enumerate(bins):
 if index==0:
 rez = round(scipy.stats.norm(avADA2,sdADA2).cdf(i)*len(verADA))
 else:
 rez = round((scipy.stats.norm(avADA2, sdADA2).cdf(i) -
scipy.stats.norm(avADA2, sdADA2).cdf(bins[index - 1])) * len(verADA))
 hiADA2.append(rez)
plt.plot(bins,hiADA2)
plt.plot(bins,hiADA)
plt.show()
33
Na sljedećim slikama prikazan je izlaz koda navedenog na prethodnoj stranici koji će ispisati 
nove parametre normalne razdiobe te iscrtati graf sa histogramom i razdiobe izvornih i 
očišćenih podataka:
Slika 4.26- Parametri distribucije(ADA2)
Slika 4.27- Usporedba distribucija (ADA)
Usporedbom krivulja normalnih razdioba vidljivo je da parametri druge iteracije bolje opisuju 
distribuciju frekvencija. Zbog toga je vrlo važan korak svake analize provjera i čišćenje 
podataka (eng. Data cleaning), te vizualizacija podataka kako bi se provjerila ispravnost i 
lakše detektirala potancijalna odstupanja ili pogreške prilikom analize. Ovaj postupak 
ponovljen je za ostale tri kriptovalute na sljedećoj stranici.
34
Slika 4.28- Usporedba distribucija (BTC)
Slika 4.29- Parametri distribucije (BTC2)
Slika 4.30- Usporedba distribucija (ETH2)
Slika 4.31-Parametri distribucije (ETH2)
35
Slika 4.32-Usporedba distribucija (IOTA)
Slika 4.33- Parametri distribucije (IOTA2)
36
Radi lakše usporedbe i vizualizacije navedenih podataka i razdioba frekvencija na sljedećim 
slikama iscrtat će se paralelno distribucije svih obrađivanih kriptovaluta te njihovi ulazni 
parametri:
Slika 4.34- Graf normalnih distribucija
Slika 4.35- Usporedna slika parametara distribucije
37
Naposljetku definiran je kod pomoću kojega će se provjeriti, na osnovu verižnih indeksa i 
parametara normalne distribucije, koliki postotak investicije bi se mogao očekivati nakon 
godinu dana. To je odrađeno tako da je aritmetička sredina, dio koji je iznad 100 posto, 
odnosno aritmetička sredina dobiti, pomnožena s brojem dana u godini da bismo dobili 
srednju vrijednost godišnje dobiti, te standardna devijacija pomnožena sa drugim korijenom 
od 365 dana otvorenog trgovanja kriptovaluta. Pomoću sljedećeg koda dobivene su 
vrijednosti, u postotku, dobiti navedenih kriptovaluta s pouzdanostima od 68% i 95%:
print("BTC postotak očekivane dobiti u 1 g. sa 68% 
pouzdanosti",(f.fitted_param['norm'][0]-100)*365+100,"+/-
",f.fitted_param['norm'][1]*np.sqrt(365))
print("ETH postotak očekivane dobiti u 1 g. sa 68% 
pouzdanosti",(a.fitted_param['norm'][0]-100)*365+100,"+/-
",a.fitted_param['norm'][1]*np.sqrt(365))
print("ADA postotak očekivane dobiti u 1 g. sa 68% 
pouzdanosti",(b.fitted_param['norm'][0]-100)*365+100,"+/-
",b.fitted_param['norm'][1]*np.sqrt(365))
print("IOTA postotak očekivane dobiti u 1 g. sa 68% 
pouzdanosti",(c.fitted_param['norm'][0]-100)*365+100,"+/-
",c.fitted_param['norm'][1]*np.sqrt(365))
print("BTC postotak očekivane dobiti u 1 g. sa 95% 
pouzdanosti",(f.fitted_param['norm'][0]-100)*365+100,"+/-
",f.fitted_param['norm'][1]*2*np.sqrt(365))
print("ETH postotak očekivane dobiti u 1 g. sa 95% 
pouzdanosti",(a.fitted_param['norm'][0]-100)*365+100,"+/-
",a.fitted_param['norm'][1]*2*np.sqrt(365))
print("ADA postotak očekivane dobiti u 1 g. sa 95% 
pouzdanosti",(b.fitted_param['norm'][0]-100)*365+100,"+/-
",b.fitted_param['norm'][1]*2*np.sqrt(365))
print("IOTA postotak očekivane dobiti u 1 g. sa 95% 
pouzdanosti",(c.fitted_param['norm'][0]-100)*365+100,"+/-
",c.fitted_param['norm'][1]*2*np.sqrt(365))
38
Izlaz gore navedenog koda dan je u nastavku i prikazuje sa razinama pouzdanosti od 68% i 
95% koliki bi se postotak trenutne cijene mogao očekivati za godinu dana:
BTC postotak očekivane dobiti u 1 g. sa 68% pouzdanosti 
194.94729833405808 +/- 88.84153469608624
ETH postotak očekivane dobiti u 1 g. sa 68% pouzdanosti
275.0673209737824 +/- 130.2608911212082
ADA postotak očekivane dobiti u 1 g. sa 68% pouzdanosti
292.1908313175746 +/- 167.0473581983816
IOTA postotak očekivane dobiti u 1 g. sa 68% pouzdanosti
199.3215393093287 +/- 141.09743611390275
BTC postotak očekivane dobiti u 1 g. sa 95% pouzdanosti 
194.94729833405808 % +/- 177.68306939217248 %
ETH postotak očekivane dobiti u 1 g. sa 95% pouzdanosti
275.0673209737824 % +/- 260.5217822424164 %
ADA postotak očekivane dobiti u 1 g. sa 95% pouzdanosti 
292.1908313175746 % +/- 334.0947163967632 %
IOTA postotak očekivane dobiti u 1 g. sa 95% pouzdanosti 
199.3215393093287 % +/- 282.1948722278055 %
Iz ovog izlaza koda moguće je primjetiti da, iako ADA ima veći maksimalni i srednji 
postotak, zbog njene volatilnosti, Ethereum i Bitcoin bi objektivno bili manje riskantna, i 
potencijalno kvalitetnija, investicija usprkos manjem dobitku. Vidljivo je također koliko veću 
volatilnost imaju novije kriptovalute u odnosu na one koje su se već profilirale na tržištu. 
39
4.6 Testiranje hipoteze
U prethodnom poglavlju prikazano je da se verižni indeksi kriptovaluta mogu približno 
opisati normalnom razdiobom. Sljedeći zadatak je testirati koliko je opisivanje verižnih 
indeksa normalnom razdiobom točno, odnosno s kojom sigurnošću se može tvrditi kako se 
verižni indeksi ravnaju prema normalnoj razdiobi. Potrebno je, također, provjeriti postoji li 
distribucija koje bi kvalitetnije opisala zadane skupove podataka.
Kod opisivanja distribucija verižnih indeksa, do sada, pretpostavljena je normalna razdioba, te 
je napisan kod koji vizualno prezentira tu hipotezu. U nastavku obrade verižnih indeksa i 
testiranja kvalitete te pretpostavke uvodi se nova biblioteka koja značajno olakšava taj 
zadatak i uklanja potrebu za postavljanjem ikakvih pretpostavki. Biblioteka koja se uvozi za 
ovo poglavlje naziva se „Fitter“. Funkcija „fitter“ uzima kao ulazni parametar skup podataka, 
obrađuje analize, parametre i testira iste, te kao izlaz daje rangiranu tablicu zadanih 
distribucija s pripadajućim rezultatima testiranja, od distribucije koja najbliže opisuje zadani 
skup podataka prema distribucijama koje ga lošije opisuju. Funkcija je prikazana u sljedećem 
kodu na primjeru:
f = Fitter(verADA,
 distributions=['gamma',
 'lognorm',
"beta",
"burr",
"norm"])
f.fit()
print(f.summary())
print(f.get_best(method = 'sumsquare_error'))
plt.legend()
plt.title("ADA")
plt.show()
Ovdje su podaci testirani na 5 različitih distribucija: gamma, logaritamska normalna, beta, 
burr i normalna distribucija. Ocjena kvalitete opisivanja distribucije izvršena je prema metodi 
najmanjih kvadrata. Ovaj dio koda prikazat će gore navedenu tablicu i parametre distribucije 
koja najbolje opisuje dani skup podataka.
40
Na sljedećim slikama prikazan je izlaz koda ispisanog na prethodnoj stranici. Funkcija 
„f.fit()“ generira graf sa iscrtanih pet distribucija, funkcija „f.summary()“ ispisuje tablicu i 
posljednja funkcija „f.get_best()“ daje parametre distribucije koja najvjernije opisuje dani 
skup.
Slika 4.36- Usporedni graf distribucija (ADA)
Slika 4.37-Tablica odstupanja distribucija
Slika 4.38- Dobiveni parametri najkvalitetnije distribucije (ADA)
Ovdje je vidljivo kako je donekle pogrešno pretpostavljeno da se verižni indeksi kreću prema 
normalnoj razdiobi već je ona koja, od svih pretpostavljenih, najbolje opisuje podatke burr 
distribucija. 
41
Ukoliko se, umjesto nekoliko pretpostavljenih distribucija, u kod uvrsti funkcija Fitter 
biblioteke „get_distributions()“ tada se zadani skup testira prema 106 dostupnih distribucija 
koje Fitter u pozadini obrađuje koristeći biblioteku Scipy. Zbog velikog broja kompliciranih 
izračuna vrijeme obrade tog koda znatno je duže u odnosu na prethodni koji analizira 5 danih 
distribucija, iz tog razloga poželjno je pretpostaviti određeni broj distribucija prije korištenja 
ove funkcije kako bi se skratilo vrijeme računanja. Rezultati obrade skupa verižnih indeksa 
ADA kriptovalute u odnosu na svih 106 distribucija sadržanih unutar biblioteke dani su na 
sljedećim slikama:
Slika 4.39- Usporedni graf distribucija 2 (ADA)
Slika 4.40- Tablica odstupanja distribucija (ADA)
Slika 4.41- Dobiveni parametri distribucije (ADA)
42
Iz prethodnog grafa je vidljivo kako prve tri distribucije imaju neznatne razlike kod ocjene 
kvalitete opisivanja ali svakako znatno manja odstupanja i od burr distribucije. Stoga se, i ova 
pretpostavka, da burr distribucija najvjernije opisuje zadani skup pokazala pogrešnom. Za 
ostale valute, listi distribucija unutar funkcije dodati će se nove, dobivene analizom svih 
distribucija na jednom primjeru.
Slika 4.42- Usporedni graf distribucija (BTC)
Slika 4.43- Tablica odstupanja distribucija (BTC)
Slika 4.44- Dobiveni parametri distribucije (BTC)
43
Slika 4.45- Usporedni graf distribucija (ETH)
Slika 4.46- Tablica odstupanja distribucija (ETH)
Slika 4.47- Dobiveni parametri distribucije (ETH)
44
Slika 4.48- Usporedni graf distribucija (IOTA)
Slika 4.49- Tablica odstupanja distribucija
Slika 4.50- Dobiveni parametri distribucije
45
Na sljedećim slikama prikazani su histogrami i distribucije koje ih najbolje opisuju: 
Slika 4.51- Josnsonsu distribucija (ADA)
Slika 4.52- Josnsonsu distribucija (BTC)
46
Slika 4.53- Josnsonsu distribucija (ETH)
Slika 4.54- Josnsonsu distribucija (IOTA)
47
5 Zaključak
U ovom radu nastojano je prikazati važnost statističke analize u modernom vremenu. U 
vremenu neiscrpnih izvora podataka i informacija statistička analiza drastično je dobila na 
važnosti u gotovo svim gospodarskim granama. Statistička analiza u velikoj mjeri utječe na 
odluke svih kompanija, investitora i banaka što znači da jednim dijelom statistička analiza 
utječe na njihovo kretanje. U ovom radu prikazana je efikasnost i korisnost metoda statističke 
analize na primjeru analize cijena kriptovaluta. 
Samom analizom primjećeno je kako sličniji projekti imaju veću korelaciju. Iota je, na 
primjer, bazirana na drugačijoj tehnologiji nego ostale kriptovalute, ona ne koristi „Block 
chain“ kao ostale već „usmjereni aciklički graf“ (eng. Directed acyclic graph). Ta razlika, u 
matrici korelacija iskazuje se kao odstupanje korelacija Iota valute od ostalih, Iota ima dosta 
niži koeficijent korelacije u odnosu na ostale međusobno, čemu je vrlo vjerojatno uzrok velika 
razlika u korištenim tehnologijama. Prikazano je i kakva je varijabilnost cijena te centralna 
tendencija njihovih verižnih indeksa koja je u svakom slučaju bila preko 100% što prikazuje 
deflacijarnu prirodu koje većina kriptovaluta postiže. Primjećeno je također kako mlađi 
projekti imaju veću varijabilnost što se može odnositi na veći postotak špekulacija u odnosu 
na opipljive korisnosti sustava. S druge strane vidljivo je kako s godinama i razvojem 
projekata varijabilnost opada, povećava se udio praktičnih rješenja koje tehnologije 
kriptovaluta nude te se samim time cijena stabilizira. Budući da je tržište kriptovaluta još 
uvijek vrlo novo područje za pretpostaviti je da će cijene i dalje drastično varirati što je 
povoljno za trgovce, ali nepovoljno za korisnike istih. Promjena varijabilnosti s vremenom od 
osnutka i povećanjem funkcionalnosti kriptovalute, samim time i realnom korisnosti, 
prikazana je na stranici 38. gdje je vidljivo kretanje cijena unutar godine dana.
Verižni indeksi testirani su i prikazuju kako burr distribucija, suprotno postavljenoj hipotezi 
kvalitetnije opisuje distribuciju frekvencija od normalne. Naknadno je ustanovljeno kako je 
ipak najprikladnija Johnsonova Su distribucija, koju je Johnson predložio kao transformaciju 
normalne razdiobe, što je razumljivo budući da je ona najpoznatija distribucija za modeliranje 
povratka investicije kod trgovanja dionicama. 
48
Dio koji je u ovom radu izostavljen, krucijalni je dodatak svakoj statističkoj analizi, a to je 
tehnološka analiza. Naime, ovaj rad nije se bavio tehnologijama koje pokreću kriptovalute 
koje se uvelike razlikuju pa se može pretpostaviti da neće sve zaživjeti i opstati. Potrebno je 
napomenuti da često statistička analiza sama po sebi nije dovoljna, pogotovo ako se radi o 
analizi cijena dionica ili kriptovaluta. Samo proučavanje cijena, grafova i tržišta ne može se 
smatrati kvalitetnom analizom bez razumijevanja tehnologija i proizvoda korištenih u svrhu 
razvoja pojedinih entiteta. Kretanje cijena u određenom periodu jedan je od indikatora svijesti 
javnosti i investitora o kvaliteti pojedinog proizvoda koja često može zavarati.
S obzirom da kriptovalute donose sa sobom obećavajuću tehnologiju, te mnoge, do današnjeg 
dana nedostupne, mogućnosti poput pametnih „trustless“ ugovora baziranih na programiranim 
uvjetima upisanim na „Block chain“, olakšane transakcije, baze podataka bez mogućnosti 
manipulacije i ostale, do sada ne istražene pogodnosti ovih tehnologija. Potrebno je uložiti 
mnogo vremena u analizu istih, mnogobrojnih projekata te shvatiti potencijal svakog od tih 
projekata.

