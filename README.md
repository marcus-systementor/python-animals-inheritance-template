# Djurens gemensamma kod – första mötet med inheritance och polymorphism

I dag får du en första introduktion till **inheritance** och **polymorphism**. Du förväntas inte behärska begreppen ännu; på onsdag går läraren igenom dem ordentligt. Målet med denna självstudielabb är att upptäcka **varför** inheritance kan vara användbart, se hur flera classes delar kod och se hur deras objects ändå kan bete sig olika.

Du bygger ett litet program med `Dog`, `Cat` och `Horse`. Först upprepar du medvetet samma kod i alla tre. **Börja inte med `Animal`**: de upprepade raderna är problemet du ska upptäcka. Därefter flyttar du det gemensamma till en parent class. Till sist anropar samma loop `speak()` på flera olika objects.

Det här är en övning, inte en examination. Arbeta steg för steg och kör ofta. Ett fungerande checkpoint är ett bra ställe att pausa. Steg 1–9 är huvudvägen; steg 10 är ett eget tillägg, och steg 11 är ett kort experiment som du kan göra direkt efter steg 9. Skriv gärna upp en fråga att ta med till onsdagen.

## Kom igång

Om labben delas som en publik GitHub-template: välj **Use this template → Create a new repository**, skapa ett eget **Private** repository och klona **ditt eget** repository. Arbeta i mappen som innehåller `README.md`. Inga extra paket behövs. Om läraren ska se ditt private repository behöver du följa lärarens anvisning om åtkomst; en länk ensam ger inte åtkomst.

Filerna du redigerar är [animals.py](animals.py) för classes och [main.py](main.py) för objects, anrop och utskrifter. Du kan använda [HJALP.md](HJALP.md) när något inte fungerar och skriva med egna ord i [REFLECTION.md](REFLECTION.md).

Kör från repositoryts rot:

```text
python main.py
```

På Windows kan `py main.py` fungera; på vissa datorer används `python3 main.py`. Startfilen skriver `Djurövning: börja med Dog` och avslutas utan fel. Den innehåller ännu inga djur-objects. I varje steg nedan är **Kör** samma kommando. Spara filerna före varje körning. Efter ett fungerande steg kan du göra en `commit` med det föreslagna engelska meddelandet i ditt eget repository.

Vi använder samma enkla regel genom hela labben: methods `eat()`, `sleep()` och `move()` **returnerar** text med djurets namn; `main.py` använder `print()` för att visa texten. `speak()` returnerar ett kort ljudord. Därför är det lätt att jämföra resultat före och efter ändringar.

## Steg 1 – bygg Dog utan inheritance

**Mål:** En `Dog` har egna attributes och fyra fungerande methods.

**Gör:** I `animals.py`, skriv `class Dog` med `__init__(self, name, age)`. Spara argumenten i `self.name` och `self.age`. Lägg till `eat(self)`, `sleep(self)` och `move(self)` som returnerar `f"{self.name} is eating"`, `f"{self.name} is sleeping"` respektive `f"{self.name} is moving"`. Lägg till `speak(self)` som returnerar `"Woof"`. I `main.py`, importera `Dog` från `animals`, skapa `dog = Dog("Fido", 4)`, skriv ut `dog.name`, `dog.age` och resultatet av **alla fyra** method-anropen. Ta gärna bort startradens utskrift när dina egna utskrifter fungerar.

**Checkpoint – kör `python main.py`:** Du ska se Fido, 4, `Fido is eating`, `Fido is sleeping`, `Fido is moving` och `Woof`. Prova tillfälligt namnet `Buddy`: de tre gemensamma texterna ska använda Buddy, medan `Woof` är samma. Återställ Fido. Kan du peka ut vilka värden som är attributes, vilka funktioner som är methods och vilket object `self` syftar på i `dog.move()`?

**Commit:** `Add Dog class`

## Steg 2 – skriv en liknande Cat

**Mål:** Märka hur mycket av en andra class som liknar den första.

**Gör:** Lägg till `class Cat` i `animals.py`, **utan inheritance**. Ge den exakt samma `__init__(self, name, age)` och samma `eat()`, `sleep()` och `move()` som Dog. Den enda skillnaden i beteende är `speak()`, som returnerar `"Meow"`. Importera också `Cat` i `main.py`, skapa `cat = Cat("Milo", 2)` och skriv ut samma sex slags värden som för Dog. Behåll Dog-testet.

**Checkpoint – kör:** Både Fido och Milo visar sina egna namn och åldrar. De gemensamma method-texterna har samma form; ljuden är `Woof` och `Meow`. Prova tillfälligt ett annat kattnamn och se att bara kattens namnbundna texter ändras. Jämför nu `Dog` och `Cat`: vilka rader är nästan identiska, och vilka skiljer sig? Vad händer med arbetet om du lägger till fem liknande classes?

**Commit:** `Add Cat class`

## Steg 3 – lägg till Horse och stanna upp

**Mål:** Se upprepningen tydligt med tre classes.

**Gör:** Lägg till `class Horse` utan inheritance. Använd samma attributes och samma `eat()`, `sleep()` och `move()` som hos Dog och Cat. Låt bara `speak()` returnera `"Neigh"`. Importera Horse i `main.py`, skapa `horse = Horse("Star", 7)` och skriv ut namn, ålder och de fyra method-resultaten. Behåll de tidigare två djuren.

**Checkpoint – kör:** Fido, Milo och Star visas; ljuden är `Woof`, `Meow`, `Neigh`. Prova tillfälligt en annan ålder för Star: bara hans åldersutskrift ändras. **Pausa innan nästa steg:** upprepar du `__init__`? Upprepas `eat()`, `sleep()` och `move()`? Är detta lätt att underhålla? Om alla djur ska få en ny `move()`-text, hur många ställen måste du ändra just nu? Skriv en kort notering i [REFLECTION.md](REFLECTION.md).

**Commit:** `Add Horse class`

## Steg 4 – sätt ord på problemet

Dog, Cat och Horse har mycket gemensamt. När samma kod finns på flera ställen tar den längre tid att skriva, är lättare att ändra olika av misstag och blir svårare att underhålla. Vi kan samla det gemensamma i en mer generell class:

```text
Animal
├── Dog
├── Cat
└── Horse
```

`Animal` är en **parent class** (eller **base class**). `Dog`, `Cat` och `Horse` blir **child classes** (eller **subclasses**). En child class kan få attributes och methods från sin parent class och ändå behålla sådant som är eget.

**Mål och gör:** Innan du ändrar koden, skriv två meningar i [REFLECTION.md](REFLECTION.md): vilka delar verkar gemensamma, och vilken method måste förbli olika? Rita gärna samma lilla träd för hand.

**Checkpoint:** Kör fortfarande `python main.py`; samma tre djur fungerar, eftersom du ännu inte har refaktorerat. Kan du förutsäga vilka rader som borde kunna finnas på ett enda ställe? Prova att läsa de tre `move()`-methods och kontrollera att de faktiskt är lika.

**Commit:** `Describe repeated animal code`

## Steg 5 – skapa Animal med det gemensamma

**Mål:** Få en generell class att fungera innan någon annan class ärver från den.

**Gör:** Lägg `class Animal` **ovanför** Dog, Cat och Horse i `animals.py`. Ge den samma constructor som de andra:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Lägg också `eat()`, `sleep()` och `move()` i Animal med samma enkla return-texter som tidigare. Ändra **inte** de tre andra classes än. Lägg **inte** `speak()` i Animal ännu. I `main.py`, importera Animal och skapa `animal = Animal("Test", 5)`. Skriv ut dess namn, ålder och de tre gemensamma method-resultaten före eller efter de andra djuren.

**Checkpoint – kör:** Test har ålder 5 och ger `Test is eating`, `Test is sleeping`, `Test is moving`. Fido, Milo och Star fungerar fortfarande som tidigare. Prova tillfälligt `Animal("Demo", 1)` och se att texterna följer namnet; återställ Test. Det finns nu **ännu mer** upprepning – den försvinner i de två nästa stegen.

**Commit:** `Add Animal base class`

## Steg 6 – låt Dog ärva

**Mål:** Ta bort upprepningen från en class utan att förlora beteendet.

**Gör:** Ändra rubriken `class Dog:` till `class Dog(Animal):`. Ta sedan bort `Dog`-versionerna av `__init__`, `eat()`, `sleep()` och `move()` från classens indragna block. Behåll bara Dog:s egen `speak()`. **Behåll** `dog = Dog("Fido", 4)` och alla anrop i `main.py`.

Dog innehåller nu inte egna versioner av `__init__`, `eat()`, `sleep()` eller `move()`, men de fungerar fortfarande: Dog får dem från Animal. Anropet `Dog("Fido", 4)` använder Animal:s constructor för att spara namn och ålder på just detta Dog-object.

**Checkpoint – kör:** Dog ger **samma** sex utskrifter som före ändringen; Cat och Horse fungerar också. Prova namnet Buddy igen och återställ Fido. Varifrån får Dog `name` och `age`? Varifrån får den `eat()`? Vilken method finns specifikt i Dog?

**Commit:** `Make Dog inherit from Animal`

## Steg 7 – refaktorera Cat och Horse

**Mål:** Samla all upprepad kod i Animal.

**Gör:** Ändra `class Cat:` till `class Cat(Animal):` och `class Horse:` till `class Horse(Animal):`. Ta bort deras egna `__init__`, `eat()`, `sleep()` och `move()`. Låt bara respektive `speak()` vara kvar. Rör inte anropen i `main.py` förrän du har kört och sett resultatet.

**Checkpoint – kör:** Alla tre djuren har fortfarande namn, ålder, äter, sover, rör sig och ger sina egna ljud. Prova tillfälligt namnet `Nova` på Cat och återställ Milo. Jämför `animals.py` med den version du hade efter steg 3: hur många kopior av constructor och de tre gemensamma methods finns nu?

**Commit:** `Refactor animal classes with inheritance`

## Steg 8 – samma method-namn, olika svar

**Mål:** Se en enkel **override**.

**Gör:** Lägg nu en generell `speak(self)` i Animal som returnerar `"Some sound"`. Låt Dog, Cat och Horse behålla sina egna `speak()`-methods. En child class kan använda en ärvd method eller skriva en egen version med **samma namn**. Den egna versionen kallas en override.

**Checkpoint – kör:** Skriv ut `animal.speak()`, `dog.speak()`, `cat.speak()` och `horse.speak()` i `main.py`. Du ska få `Some sound`, `Woof`, `Meow`, `Neigh`. Prova tillfälligt annan generell text i Animal: bara `animal.speak()` ändras, eftersom de tre child classes har egna versioner. Återställ `Some sound`.

**Commit:** `Override speak in child classes`

## Steg 9 – en loop för olika djur

**Mål:** Uppleva polymorphism i ett program som redan fungerar.

**Gör:** Lägg i `main.py` en `list` med de tre objects som du redan har: `animals = [dog, cat, horse]`. Använd en `for`-loop som för varje `animal` skriver ut `animal.name` och resultatet av `animal.speak()`:

```python
for animal in animals:
    print(animal.name)
    print(animal.speak())
```

Du kan behålla de tidigare kontrollutskrifterna eller ta bort upprepade testutskrifter när loopen fungerar. I loopen används **samma kod**, `animal.speak()`, men olika objects svarar olika. Detta är polymorphism i denna övning. Loopen behöver inga särskilda `if`-grenar som frågar om djuret är Dog, Cat eller Horse.

**Checkpoint – kör:** Loopen visar Fido/Woof, Milo/Meow och Star/Neigh. Byt tillfälligt ordning på `cat` och `dog` i listan: ordningen på utskrifterna ändras, men loopen behöver inte ändras. Återställ ordningen. Förklara med egna ord varför samma loop fungerar för alla tre.

**Commit:** `Use polymorphism with animals`

## Steg 10 – ett eget djur (extra övning)

**Mål:** Kontrollera själv att en ny child class passar in utan en ny loop.

**Gör:** Välj `Cow`, `Sheep` eller `Goat`. Lägg till en class i `animals.py` som ärver från Animal och har en egen `speak()`. Låt dess namn, ålder, `eat()`, `sleep()` och `move()` komma från Animal. Importera classen i `main.py`, skapa ett object och lägg till det i `animals`-listan. Skriv inte om loopens body.

**Checkpoint – kör:** Det nya djuret visas i samma loop med sitt eget ljud. Anropa även `eat()`, `sleep()` och `move()` på det nya objectet och se att de fungerar. Prova ett annat namn på just det objectet; den befintliga loopens struktur ska vara oförändrad.

**Commit:** `Add another animal type`

## Steg 11 – ändra en delad method

**Mål:** Se den praktiska vinsten av gemensam kod.

**Gör:** Ändra **bara** `move()` i Animal så att return-texten innehåller både `self.name` och `self.age`, exempelvis `Fido (4) is moving`. Låt `move()` i varje child class vara frånvarande. Om du hoppade över steg 10 fungerar experimentet ändå. Efter loopen i steg 9 syftar namnet `animal` på det **sista** djuret i listan. Skapa därför ett nytt `test_animal = Animal("Test", 5)` när du vill jämföra den generella classen i just detta checkpoint.

**Checkpoint – kör:** Skriv ut `move()` för `test_animal`, `dog`, `cat` och `horse` (och ditt extra djur om du gjorde steg 10). Du ska se `Test (5) is moving`, `Fido (4) is moving`, `Milo (2) is moving` och `Star (7) is moving`. Prova tillfälligt en annan ålder för Dog: bara Dog-raden får den nya åldern. Ändringen i **en** method gav ny text för alla djuren. Varför?

**Commit:** `Update shared animal movement`

## Avsluta eller ta paus

Svara kort i [REFLECTION.md](REFLECTION.md), särskilt på frågan du vill ta med till onsdagen. Notera ditt senaste fungerande steg. Om programmet får ett fel: använd [HJALP.md](HJALP.md), läs den sista raden i `traceback` och återgå till senast fungerande checkpoint. Du behöver inte memorera definitioner i dag; det viktiga är att du har sett problemet och vad den nya strukturen löser.
