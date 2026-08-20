## 1️⃣ Modellering

Tänk er en dykarklubb som anordnar utfärder under sommarhalvåret. De har en webbsida där man kan läsa om klubben, men nu vill de lägga till möjlighet att anmäla sig till dykutflykterna.
- klubben behöver spara kontaktuppgifter till de som anmäler sig
- när man har betalt en avgift ska det också registreras
- man ska kunna hyra utrustning, eller ta med sig egen
- klubbens utrustning består av exempelvis våtdräkter och syrgastuber, men man har ett begränsat sortiment
- man kan avboka sig
- varje utflykt äger rum på en specifik dag och plats
- intresserade ska kunna söka efter utflykter baserat på plats
- en person måste vara ledare med huvudansvar för varje utflykt

### Uppgift
1. ge ett förslag på vilka klasser som behöver finnas
2. ta fram vilka egenskaper och metoder klasserna behöver ha
3. redogör för vilka parametrar och returvärden metoderna behöver

[![UML-diagram](images/dykarklubb.png)](images/dykarklubb.png)

[Klicka på diagrammet för att öppna det i full storlek]

## 2️⃣ Kodning

Vänerns Vänner är en friluftsförening som brukar träffas en gång i månaden och gå runt Vänern. (Men inte hela på ett tillfälle!) Nu behöver de ett anmälningssystem för sina utflykter och det är upp till er att lösa det med TDD. Er uppgift:
1. Skriv testfall för Inventory och Excursion
2. Efter varje testfall, implementera funktionen du testar

Inventory - representerar klubbens inventarier som de kan hyra ut till medlemmar
- set_item(name, rent_price, amount)
- rent(item_name)   # hyr ut ett exemplar
- get_amount_left(name)  # returnerar antalet

Item - en "dum" klass som inte behöver testas (innehåller inga metoder utöver konstruktorn)
- konstruktor
- egenskaperna name, rent_price och amount

Excursion
- get_members()  → returnerar lista med namnen som strängar
- add_member(name)
- remove_member(name)
- register_item_rented(member_name, item_name)
- register_item_returned(member_name, item_name)
- get_all_who_has_not_returned_items() → returnerar lista med namn på alla medlemmar som inte har lämnat tillbaka alla saker de hyrde


## Testöversikt

### Implementation
#### Inventory
Efter att ha identifierat grundläggande testbehov för klassens metoder skrev jag de första testfunktionerna. När testerna signalerade rött 
implementerade jag motsvarande funktionalitet i `Inventory` så att testerna signalerade grönt. Jag fortsatte sedan att identifiera och implementera 
alltmer komplexa testscenarier tills jag bedömde att klassens metoder var tillräckligt testade.

Då testfallen var färdiga konstaterade jag att det förekom en hel del identisk kod avseende skapande och användande av artiklar (Items) samt 
instansiering av `Inventory`. Jag valde därför att förenkla testkoden genom att använda fixtures för artiklarna och `Inventory`-objektet.

``` python
@pytest.fixture
def inventory():
    """
    Creates an inventory item for testing.
    """
    return Inventory()


@pytest.fixture
def compass():
    """
    Creates a compass item for testing.
    """
    return Item("Compass", 25, 30)
```
[Exempel från koden]

## Testöversikt – Inventory

### Items

| Test                     | Scenario                         |
|:-------------------------|:---------------------------------|
| `test_set_item()`        | Lägger till ett item i inventory |
| `test_get_amount_left()` | Hämtar antal tillgängliga items  |

### Rent

| Test                                           | Scenario                                                                                        |
|:-----------------------------------------------|:------------------------------------------------------------------------------------------------|
| `test_rent()`                                  | Hyr ett item                                                                                    |
| `test_rent_no_items()`                         | Försöker hyra när lagret är tomt                                                                |
| `test_rent_multiple_same_items()`              | Hyr samma item flera gånger                                                                     |
| `test_rent_correct_item_from_multiple_items()` | Hyr ett item från ett inventory med flera items och kontrollerar att övriga items inte påverkas |
| `test_rent_multiple_different_items()`         | Hyr flera olika items                                                                           |
| `test_rent_non_existing_item()`                | Försöker hyra ett item som inte finns i inventory                                               |


### Implementation
#### Excursion
Jag använde samma arbetsmetodik som vid design av testfall för klassen `Inventory`.
Även i detta fall tyckte jag att det förekom en hel del identisk kod, särskilt avseende
skapande av medlemmar, artiklar och `Excursion`-objektet.

Jag valde därför att förenkla testkoden genom att använda fixtures för artiklarna och
`Excursion`-objektet. Jag tyckte att skapandet av medlemmar var väsentligt för varje
testfall och att behålla det i testet ökade tydligheten.

``` python
@pytest.fixture
def excursion():
    """
    Creates an excursion item for testing.
    """
    return Excursion()

@pytest.fixture
def compass():
    """
    Creates a compass item for testing.
    """
    return Item("Compass", 25, 30)
```
[Exempel från koden]

## Testöversikt – Excursion

### Members

| Test                                 | Scenario                               |
|:-------------------------------------|:---------------------------------------|
| `test_add_get_member()`              | Lägger till och hämtar en medlem       |
| `test_add_get_member_many_members()` | Lägger till och hämtar flera medlemmar |
| `test_remove_member()`               | Tar bort en medlem                     |

### Rented items

| Test                            | Scenario                        |
|:--------------------------------|:--------------------------------|
| `test_register_item_rented()`   | Registrerar ett uthyrt item     |
| `test_register_item_returned()` | Registrerar ett återlämnat item |

### Items not returned

| Test                                                            | Scenario                        |
|:----------------------------------------------------------------|:--------------------------------|
| `test_get_all_who_has_not_returned_items_one_member()`          | En medlem har ett item          |
| `test_get_all_who_has_not_returned_items_member_many_items()`   | En medlem har flera items       |
| `test_get_all_who_has_not_returned_items_member_return_one()`   | Ett item återlämnas             |
| `test_get_all_who_has_not_returned_items_member_return_all()`   | Alla items återlämnas           |
| `test_get_all_who_has_not_returned_items_many_members()`        | Flera medlemmar har items       |
| `test_get_all_who_has_not_returned_items_members_many_items()`  | Flera medlemmar har flera items |

## 3️⃣  Extra uppgift
Tänk dig en väderapp som består av två klasser:
- WeatherApp - representerar frontend, dvs det sätt som användaren interagerar med appen. Alla user stories vi skapar för systemet löses med hjälp av metoder i klassen.
- WeatherService - klassen som har den faktiska väderdatan. Den ska ha metoder som WeatherApp kan anropa för att lösa sina user stories.
Din uppgift:
1. Ta fram 2-3 user stories. Välj en att börja med.
2. Skapa filer för WeatherApp och WeatherService.
3. Bygg enhetstest för filen WeatherApp med hjälp av TDD (red, green, refactor)
4. Upprepa för nästa user story

User stories (krav):
1. "Som en besökare, vill jag söka på min stad, så att jag kan se vilket väder det kommer att vara idag."
2. "Som en besökare, vill jag kunna se om det ska bli regn, så att jag vet om jag behöver ta med paraply."
3. "Som en besökare, vill jag kunna se temperaturen i en stad, så att jag vet om det är en baddag."


|  Krav  | Testfall                         | Testar                                                   |
|:------:|:---------------------------------|:---------------------------------------------------------|
|   1    | `test_search_city`               | Om användaren söker en stad returneras vädret.           |
|   2    | `test_get_city_rain_probability` | Om användaren söker en stad returneras risken för regn.  |
|   3    | `test_get_city_temperature`      | Om användaren söker en stad returneras temperaturen.     |

### Implementation
Då uppgiften krävde att klassen enhetstestas valde jag att mocka `WeatherService`. Då varje testfall kräver en `WeatherApp` och en mockad `WeatherService` valde 
jag att förbereda testerna med dessa som fixtures.

``` python
@pytest.fixture
def weather_service(mocker):
    return mocker.Mock()

@pytest.fixture
def weather_app(weather_service):
    return WeatherApp(weather_service)
```
Jag valde relativt enkla user stories eftersom jag ville fokusera på själva TDD-arbetet och framför allt på hur mockning kan användas för att testa 
`WeatherApp` isolerat från `WeatherService`. Fixtures hade jag redan arbetat med i den föregående programmeringsuppgiften.

För varje user story började jag med att skriva ett test som initialt signalerade rött. Därefter implementerade jag den minsta funktionalitet som krävdes 
för att testet skulle signalera grönt. Slutligen refaktorerade jag koden vid behov innan jag gick vidare till nästa user story.