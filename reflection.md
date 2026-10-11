# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game would determine to enter a higher number or lower when I guessed a number.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The answer was higher than the hint. An example would be when I entered 5 it would say lower when the final answer was higher. Another that I saw in the game when I clicked new game when it would only run for once to play. The way that I think might've been the error would be on the app.py when the code of "too high" to "Go HIGHER".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--5-----|-Too low-----|----Too high----|
--None------app.py-------------|

|--10-----|-Too low-----|----Too high----|
--None------app.py-------------|
|- 60-----|-Too low-----|----Too high----|
--None------app.py-------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The one example would be when the game doesn't reset when trying to play another game and it does stay locked when I played one game.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

The one example would be the range mismatch since when I ran the first game it was giving 61 as the number not higher than 100.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
