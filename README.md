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

## Testöversikt

## Testöversikt – Inventory

### Items

| Test | Scenario |
|---|---|
| `test_set_item()` | Lägger till ett item i inventory |
| `test_get_amount_left()` | Hämtar antal tillgängliga items |

### Rent

| Test | Scenario |
|---|---|
| `test_rent()` | Hyr ett item |
| `test_rent_no_items()` | Försöker hyra när lagret är tomt |
| `test_rent_multiple_same_items()` | Hyr samma item flera gånger |
| `test_rent_correct_item_from_multiple_items()` | Hyr ett item från ett inventory med flera items och kontrollerar att övriga items inte påverkas |
| `test_rent_multiple_different_items()` | Hyr flera olika items |
| `test_rent_non_existing_item()` | Försöker hyra ett item som inte finns i inventory |

## Testöversikt – Excursion

### Members

| Test | Scenario |
|---|---|
| `test_add_get_member()` | Lägger till och hämtar en medlem |
| `test_add_get_member_many_members()` | Lägger till och hämtar flera medlemmar |
| `test_remove_member()` | Tar bort en medlem |

### Rented items

| Test | Scenario |
|---|---|
| `test_register_item_rented()` | Registrerar ett uthyrt item |
| `test_register_item_returned()` | Registrerar ett återlämnat item |

### Items not returned

| Test | Scenario |
|---|---|
| `test_get_all_who_has_not_returned_items_one_member()` | En medlem har ett item |
| `test_get_all_who_has_not_returned_items_member_many_items()` | En medlem har flera items |
| `test_get_all_who_has_not_returned_items_member_return_one()` | Ett item återlämnas |
| `test_get_all_who_has_not_returned_items_member_return_all()` | Alla items återlämnas |
| `test_get_all_who_has_not_returned_items_many_members()` | Flera medlemmar har items |
| `test_get_all_who_has_not_returned_items_members_many_items()` | Flera medlemmar har flera items |
## 3️⃣  Extra uppgift