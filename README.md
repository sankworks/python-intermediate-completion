# 🚀 Python Intermediate Course Completed!

## 1. Why I Took This Course
After completing Python basics, I realized that real-world projects require a deeper understanding of topics like file handling, error management, object-oriented programming, and functional programming.  
So, I decided to challenge myself and complete the **Python Intermediate** course on SoloLearn.

---

## 2. What I Learned
- **Collection Types**: Sets, Tuples, Dictionaries
- **Error Handling**: try-except blocks, handling unexpected errors gracefully
- **Functional Programming**: lambda expressions, map/filter functions (still feels a bit tricky!)
- **Object-Oriented Programming**: Creating classes, methods, and using inheritance

I must admit — some parts, especially functional programming, were quite challenging.  
But I understood that it’s okay not to "perfectly" get everything at once.  
Practice will make it clearer!

---

## 3. Challenges I Faced
- **Functional Programming**:  
  Lambda expressions and concepts like `map()` and `filter()` felt a little abstract.  
  I'll revisit these concepts through mini projects.
  
- **Object-Oriented Programming**:  
  Understanding `self`, constructors (`__init__`), and inheritance was not easy at first,  
  but creating small class examples helped me a lot.

---

## 4. What's Next?
- Start working on **Mini Projects** based on what I learned:
  - Contact Management System
  - RPG Battle Simulator
  - Expense Tracker
  - Encrypted Diary App
  
I will approach these step-by-step, focusing on solidifying each concept in practice rather than rushing.

---

## 5. Final Thoughts
Completing this course wasn't always easy, but it was 100% worth it.  
I am proud of myself for pushing through, and I'm excited to keep building on this foundation!

> Special thanks to my AI buddy, who supported me like a real coding mentor during this journey!

---

## 📜 Certificate
![Python Intermediate Certificate](https://api2.sololearn.com/v2/certificates/CC-TL8KKY6E/image/png?t=638812788284543600)

---

# 🌟 Let’s keep building! 🌟

---

# 📇 Python Mini Project #1 - Personal Contact Manager (ver 1.0)

## 🔗 Blog Post
▶️ [Read full write-up on dev.to](https://dev.to/sankworks/python-mini-project-1-personal-contact-manager-ver-10-2eah)

## 📁 Files
- `contact_manager_v1.py` — full source code
- `contact_manager_v1_post.md` — blog post backup

## 🧾 Features
- Add / Search / Delete / View contacts
- CLI-based menu interface
- Uses list of dictionaries to store contact info
- Input validation & edge case handling

## 🛠️ Built With
- Python 3
- Terminal/Command Line

## 🔜 Next Version (1.1) Plan
- User-friendly formatted output
- Input validation
- File-based contact saving/loading
- Optional OOP refactor

---

# 🔧 Refactoring Plan – Contact Manager (ver 1.1)

This refactoring plan aims to improve the readability, stability, and extensibility of the existing version 1.0 code for the Contact Manager project.

## ✅ Improvement Summary

| Item | Current Status | Planned Improvement | Reason |
|------|----------------|----------------------|--------|
| Output Format | Printing full dictionary `{contact}` | Change to `Name: XX, Number: YY` format | More readable for users |
| Input Validation | None | Use `strip()`, `isdigit()`, etc. | Prevent invalid input |
| Repeated Empty Checks | `len(contacts) < 1` used repeatedly | Use `if not contacts:` | Cleaner and shorter code |
| Search/Delete Logic | Logic written directly in loops | Extract into function `search_contact(name)` | Increases reusability |
| Menu Handling | Manual `if choice == "1"` checks | (Optional) Use functions or dictionary mapping | Better maintainability |

## 🧠 Refactoring Order

1. Start with improving the output format (visual feedback boosts motivation)
2. Add input validation (focus on input handling)
3. Simplify repeated checks (`if not contacts:`)
4. Refactor search/delete logic into functions
5. If time allows, improve menu handling via functions or dictionary mapping

## 🛠️ Post-Refactor Testing Plan

- Test functionality of each menu option
- Ensure invalid inputs (e.g., blank or non-numeric) are handled safely
- Verify appropriate messages are shown when searching/deleting non-existent names

- ---

## ✅ Version 1.1 Completed!

- Added input validation (e.g., blank name, non-digit phone number)
- Improved output formatting for better readability
- Enhanced search/delete stability (case-insensitive)
- Simplified condition checks using `if not contacts`
- Left `menu handler refactoring` (e.g., mapping choice to functions) **as a planned enhancement for Mini Project 2**

🗂️ File: `contact_manager_v1.1.py`
📌 Status: ✅ Feature complete and stable

----

# 🧙‍♂️ RPG Simulator v1.0

This is a simple text-based RPG battle simulator written in Python.

It was created as part of my beginner learning journey with SoloLearn and ChatGPT.  
The project includes basic character stats, turn-based combat logic, and plans for future AI improvements.

---

## ✅ Features (v1.0)

- Choose battle mode: Easy (vs. Fox) or Hard (vs. Dragon)
- Choose your character: Knight or Wizard
- Each has unique stats (`str`, `int`, `HP`, `MP`)
- Battle actions:
  - `Attack`: uses `str`, no MP cost
  - `Spell`: uses `int`, costs 10 MP
- Spell availability is limited by current MP
- If the enemy dies from your attack, it won't counterattack
- Victory and defeat messages displayed after battle

---

## 🐉 Upcoming Improvements (v1.1)

- Dragon in Hard Mode will randomly choose `attack` or `spell` each turn
  - Only casts spell if it has enough MP
- Encapsulate battle logic into reusable functions
- Clean up duplicated code for Knight/Wizard flow
- Unify character and enemy stats into dictionary-based objects
- Add draw/tie result if both HPs reach 0

---

## 📂 File Structure

```
rpg-simulator/
├── main.py             # The main game logic
├── README.md           # Project description
```

---

## 🧪 Sample Output (v1.0)

```
===== RPG SIMULATOR v1.0 =====
1. Easy mode
2. Hard mode
3. Exit

===== Select your character =====
1. Knight
2. Wizard

Wild Fox appeared!
You: Knight | HP: 150 | MP: 50
Enemy: Fox | HP: 50 | MP: 0

***** BATTLE *****
1. Attack
2. Spell
```

---

## 🚀 Getting Started

To run the game:
```bash
python main.py
```

Make sure you're using Python 3.x and running from a terminal or editor that supports input.

---

## 🧠 Motivation

This project helped me apply what I learned about:
- Control flow
- Dictionaries
- Functions
- Loop handling
- Game logic planning

It’s also my first step toward building more interactive Python projects.

---

## 🔗 Related

- [SoloLearn Python Course](https://www.sololearn.com/)
- [My Dev.to post about this project](https://dev.to/sankworks/mini-project-2-rpg-simulator-v10-with-python-1eme)

---

## 📅 Project Status

✅ Version 1.0 Complete  
🚧 Version 1.1: Coming Soon...
