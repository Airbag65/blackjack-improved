# PLANERING OUTLINE:

## Card:
- Färg (suit)
- Värde
- face value
- Ace (1 eller 11 beroende på totalt värde)


## Player:
### Variables:  
- username
- password
- Namn
- Saldo
### Funktioner: 
- dra 2 kort
    - om klätt och ess
        - Return blackjack
        - 2.5 vinst om vinner över dealer annars push
- hit
- stay
    - Return totalt värde
- split
- double down


## Dealer: 
- dra 2 kort
    - om klätt och ess
        Return Blackjack
    - annars om total under 17
        - hit
    - annars om >= 17
        - stay

## Database :
- Spara användare från `Player` vid utloggning
    - Se rubriken `Player` för dataspalter
- Skapa ny användare från `Player`
- Spara spelomgångar:
    - player cards
    - dealer cards
    - outcome
    - bet storlek
    - omgångsID (autoincrement)

## Main.py
- Skapa användare
    - Spara till databas
    - Logga automatiskt in med det nya kontot
- Inloggning
    - Ange användarnamn och lösenord
    - kontrollera med databas 
        - Användarnamn finns i databas
            - Kontrollera om angett lösenord matchar databasens sparade lösenord (krypterat)
    - Logga in om allt matchar
    - Felmeddelande och försök igen om det inte matchar

# Att Göra:


# Utförs nu: 
- Skapa huvudmeny (Skapad men inte klar)
    - Spela
    - Avsluta (Klar)
    - Plånbok (Skapad men inte klar)
        - Visa saldo (Klar)
        - Insättning
        - Uttag
    - Mitt konto
        - visa uppgifter
        - se tidigare spelomgångar

# Utfört: 
- Skapa basklasser utan metoder
- Skapa databas struktur
- Skapa inloggningssystem
- Skapa startsida 
    - välja logga in eller skapa konto