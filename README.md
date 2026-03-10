# 📁 Game Character Stats Tracker
> A Python class that models an RPG game character with clamped health and mana stats, levelling up, and property based access control.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Learning](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project builds on earlier RPG and OOP work by introducing property-based stat management to a game character. Rather than raising errors on invalid values, the `health` and `mana` setters silently clamp inputs to their valid range a common pattern in game development where you want stats to cap gracefully rather than crash. The `level_up()` method restores both stats to full on promotion.

## 🧠 What I Learned

- **Clamping values with setters** — Rather than raising exceptions, using `if/elif` inside a setter to silently cap values within a valid range (e.g. health stays between 0 and 100), which is the right approach for game stat systems
- **Read-only properties** — Defining a `@property` for `name` and `level` with no setter, making them accessible but not directly modifiable from outside the class
- **`level_up()` as a coordinated state change** — Writing a method that updates multiple attributes together (`_level`, `health`, `mana`) and uses the setters internally to ensure the reset values still pass through validation
- **`__str__` for readable output** — Formatting a multi-line character sheet using `\n` inside an f-string to keep the return statement clean and readable
- **Building on previous knowledge** — Applying @property, private attributes, and OOP patterns from the Salary Tracker in a new context, reinforcing the concepts through repetition

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

`GameCharacter` is initialised with a name. Stats start at fixed values and are managed through properties:
| Stat | Default | Min | Max |
|------|---------|-----|-----|
| Health | 100 | 0 | 100 |
| Mana | 50 | 0 | 50 |
| Level | 1 | - | - |

`level_up()` increments the level and restores health and mana to their maximums.

**Example Output:**
```
Name: Ren
Level: 1
Health: 100
Mana: 50

Ren leveled up to 2!

Name: Ren
Level: 2
Health: 100
Mana: 50
```

## 🚀 Future Improvements

- [ ]  Add `take_damage(amount)` and `use_ability(mana_cost)` methods that interact with the clamped setters
- [ ]  Scale max health and mana with level so stats grow on each level up
- [ ]  Add a character class (Warrior, Mage, Rogue) that sets different starting stats
- [ ]  Link back to the RPG Character Creator project so characters can be created and then played

## 📂 Project Structure
```
game-character/
│
├── P8GameCharacterStatTracker.py    # GameCharacter class
└── README.md
```

*Part of my Python learning journey 🐍 — reinforcing properties and OOP by building on earlier RPG and Salary Tracker patterns*
