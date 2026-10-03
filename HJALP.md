# Hjälp – små kontroller när du fastnar

Börja med det steg du arbetar med i [README.md](README.md). Läs de sista raderna i din `traceback`: den **sista raden** namnger ofta felet. Raderna ovanför visar fil och radnummer. Läs den raden i din aktuella fil, inte ett gammalt radnummer i en skärmbild. Gör en liten ändring och kör `python main.py` igen. Tillfälliga `print()` av ett värde eller `type(value)` kan visa vad programmet faktiskt använder; ta bort dem när du förstått felet.

- **Programmet hittar inte `main.py` eller `animals.py`:** stå i mappen med båda filerna. Spara filerna. Prova `py main.py` eller `python3 main.py` om `python` inte hittas.
- **`NameError` för Animal när du skriver `class Dog(Animal)`:** Python måste ha läst definitionen av Animal före Dog. Lägg base class ovanför subclasses i samma fil. Kontrollera också att namnet stavas likadant.
- **Dog verkar inte ärva:** jämför class-rubriken med det aktuella steget. Har du verkligen skrivit Animal inom parentes i `class Dog(Animal)`? Gör samma kontroll för Cat och Horse när de ska ärva.
- **`IndentationError`:** methods ska ha indrag under sin class; raderna i en method ska ha ytterligare indrag. Anrop och utskrifter i `main.py` ska inte av misstag ligga inne i en class.
- **Fel om saknat argument:** kontrollera att `self` står först i varje method-definition. När du skriver `dog.eat()` skickar du inte `self` själv. Constructor-anropet ska ha namn och ålder i den ordning som `__init__` väntar sig.
- **Ändringen i Animal verkar inte synas:** kontrollera att Dog, Cat och Horse inte fortfarande har egna kopior av `eat()`, `sleep()` eller `move()` efter refaktoreringen. En egen method i subclassen med samma namn används i stället för den ärvda. Kontrollera också att du kör den fil du faktiskt redigerar och att dina ändringar är sparade.
- **Fel ljud eller inget ljud:** kontrollera stavningen `speak` i definition och anrop. `dog.speak` utan `()` är en method-referens; `dog.speak()` anropar den och ger ett return-värde som du kan skriva ut.
- **Ett nytt djur syns inte i loopen:** skapade du ett object och lade du just det objectet i `animals`-listan? Class-definitionen ensam lägger inte till något i listan.
- **Ett test fungerar men det andra inte:** kontrollera att alla methods som ska jämföras **returnerar** text och att `main.py` använder `print()` på returvärdet. Blanda inte in nya utskrifter inne i methods mitt under refaktoreringen.

Om du fortfarande sitter fast: skriv ner stegnummer, körkommando, vilka namn/åldrar du använde, vad du väntade dig, vad du såg och sista raden i `traceback`. Det gör det lättare för dig och läraren att pröva samma sak.
