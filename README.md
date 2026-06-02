# CrAmki  
![Status](https://img.shields.io/badge/status-prototype-orange)


Cramki is a tool that helps me convert my reviewers into Anki flashcard faster!

# What Does It Do?
- Basically you can import a pdf and then it will generate the apkg flashcard file for anki and then all u have to do is import it into your deck and boom <33


this is just to automate how I study using gemini as I use it mainly for generating questions for me to turn it into a flashcard but it takes so so SO much of my time and
by the time I finish making a deck flashcard, im already tired TT so I built CrAmki to automate these stuff and so that I can just focus on revising the cards and the actual studying, reviewing part.

**Try the live prototype here:** [cramki.onrender.com](https://cramki.onrender.com)

*(Note: Im hosting the app on a free cloud tier in Render, so it may take about 60 seconds to "wake up" if it has been inactive!)*
*(Note: it is currently a prototype so it will be a little clunky ;[ )

# roadmap and fixes
- [ ] have to fix better viewing for mobile in case i have to quickly make apkg files when im outside
- [ ] finetune the prompt for better result of questions
- :heavy_check_mark: increase chunks for question generation
- :heavy_check_mark: change ui and fix front end code
- [ ] ability customize amount of question for apkg file
- [ ] ability to do multi-file upload, maybe?
- [ ] fix overlapping of cards from different apkg file
- [ ] add a preview before export/download
- [ ] make the code cleaner and comment documentation easier to read
- [ ] maybe add something to integrate with studystack ??

theres a bunch of webapp like CrAmki already but this one is more personalized for my experience and liking.

### Built With

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JS | front end stuff |
| **Backend Core** | Python 3, FastAPI | routing, api endpoints and the core logic |
| **Data Processing** | Genanki, JSON | for the generated the final `.apkg` deck files. |
| **AI Integration**| Google Gemini API | Parsed the PDF study material and automatically generated high-quality Q&A flashcard pairs. |
| **Infrastructure** | Render, GitHub | continuous deployment pipeline and hosted the live web application. |
