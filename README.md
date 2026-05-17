# Python_Learning
Python-Learning

## My Python Learning Journey

I started this journey to master Python and leverage it as a foundation for working with Artificial Intelligence. AI is rapidly transforming industries, and  I’ve chosen to understand it, use it, and build with it.

My goal is to use AI as a tool to accelerate learning, solve real-world problems, and create impactful applications. This repository documents my progress, experiments, and projects as I grow into the AI space.

This repository documents my learning progress, experiments, and projects as I move toward AI development.


## 🛠️ Completed: Week 1 Foundation (Feb 11 - Feb 23 (2026))
I have successfully mastered the core logical building blocks of Python.

### Key Skills Mastered:
- **Control Flow:** Mastering `if/else` and `while/for` loops for decision making.
- **Data Structures:** Implementing Lists and Dictionaries to manage complex datasets.
- **Functional Programming:** Building reusable code blocks with `def` and `return`.
- **State Management:** Tracking variables and user input across an interactive session.

### 📂 Featured Projects:
- **[Number Guessing Game](./guessgame.py):** A logic-based game utilizing the `random` module and `while` loops.
- **[Student Management System](./dict.py/):** A real-world application using **Lists of Dictionaries** to store and retrieve data.
- **[Modular Calculator](./functions.py/):** A project focused on logic separation and functional return values.

## Completed: Week 2 — CLI Project (Mar 3 - Mar 7 (2026))
Built a complete command-line Expense Tracker from scratch, following a structured approach: make it work → structure it → add features → polish.

### Key Skills Mastered:
- **File Handling:** Saving and loading data using `json` module.
- **Error Handling:** Using `try/except` to handle invalid user input gracefully.
- **Modular Design:** Separating each feature into its own clean function.
- **CLI UX:** Building an interactive menu-driven interface with a `while` loop.

### 📂 Featured Project:
- **[Expense Tracker CLI](./Expense Tracker/expense.py):** A fully working CLI app to add, view, and filter expenses by category. Data persists across sessions via JSON file storage.


## Completed: Week 3 — SQLite + Python (Mar 8 - Mar 16 (2026))
Built a complete Student Management System using SQLite, moving from in-memory data to a real persistent database.

### Key Skills Mastered:
- **SQLite Integration:** Connecting Python to a database using the `sqlite3` module.
- **Full CRUD:** Implementing Create, Read, Update, and Delete operations.
- **Search:** Using SQL `LIKE` query for name-based search.
- **Database Best Practices:** Using `rowcount` to verify if update/delete actually affected a row.

### 📂 Featured Project:
- **[Student Management System](./Student Management System/main.py):** A CLI app to manage student records with full CRUD operations backed by a SQLite database.

## Completed: Week 4 — NumPy & Pandas + Live API Pipeline (Apr 8 - Apr 15 (2026))
Built a real-time weather data pipeline pulling live data from OpenWeather API.

### Key Skills Mastered:
- **NumPy Vectorization:** Rewrote loop-based salary calculator using NumPy — achieved 40x speed improvement
- **Pandas:** DataFrame creation, filtering, sorting, groupby, handling missing values
- **Live API Integration:** Pulled real-time JSON data from OpenWeather API using requests
- **JSON Parsing:** Manually extracted nested JSON fields into clean DataFrame structure
- **Environment Variables:** Used dotenv to securely handle API keys

### 📂 Featured Project:
- **[Live Weather Pipeline](./pandas/liveapi.py):** Pulls real-time weather data for Indian cities — temperature, humidity, feels like, weather condition. Analyzes which city feels hottest and filters by humidity threshold.


## Completed: Phase 1 Final — Chennai Real-Time Data Pipeline (Apr 15 - May 8 (2026))
Built a complete data engineering pipeline pulling live Chennai weather and gold prices, storing in SQLite, and analyzing trends over time.

### Key Skills Mastered:
- **Web Scraping:** Scraped live headlines from The Hindu using BeautifulSoup
- **Merging DataFrames:** Combined multiple datasets using inner, left, right, outer joins — same as SQL
- **Pivot Tables:** Multi-dimensional aggregations across departments and categories
- **Datetime Handling:** Converted Unix timestamps and string dates to proper datetime objects
- **Matplotlib:** Line, bar, and histogram charts on real scraped data
- **Seaborn:** Heatmaps and pairplots showing correlations between weather variables
- **SQLite Pipeline:** Two-table database storing weather and gold price data across multiple runs
- **Data Analysis:** Answered 10 real questions from live data with code

### Key Findings:
- Chennai Temperature vs Humidity correlation: **-0.81** — strong negative. Hotter days are drier.
- Gold price increased **₹4,040** between May 6 and May 8 2026
- Chennai weather is **mist 89% of the time** based on recorded data
- Average Chennai temperature: **31.26°C**

### 📂 Featured Project:
- **[Chennai Data Pipeline](./Chennai_Pipeline/pipeline.py):** Pulls live weather and gold prices, stores in SQLite. Run `pipeline.py` to fetch fresh data, then `analyze.py` to answer 10 analytical questions with visualizations.


## Completed: Phase 2 — ML Week 1 & 2 — Machine Learning From the Inside Out (May 8 - May 17 (2026))
Built core ML algorithms from scratch using only NumPy — no Scikit-learn.

### Key Skills Mastered:
- **Linear Regression from Scratch:** Implemented predict, cost function, and gradient descent manually using only NumPy
- **Train/Test Split:** Understood overfitting by evaluating on unseen data
- **Evaluation Metrics:** Calculated MAE, RMSE, R² manually — not just using libraries
- **Logistic Regression from Scratch:** Implemented sigmoid, predict, and gradient descent for classification
- **Confusion Matrix:** Calculated TP, TN, FP, FN manually from predictions
- **Classification Metrics:** Accuracy, Precision, Recall, F1 Score — calculated manually AND in code
- **Entropy from Scratch:** Implemented entropy formula using NumPy — foundation of Decision Trees
- **Information Gain:** Built weighted average entropy and information gain functions from scratch
- **Overfitting vs Underfitting:** Understood Bias vs Variance trade-off with real examples

### Key Insights:
- Gold price model R² = **-1650** — proved that 6 data points is not enough for reliable prediction
- Logistic Regression achieved **80% accuracy** on student pass/fail prediction
- Perfect split at hours > 4 gave **Information Gain = 0.97** — maximum possible

### 📂 Featured Projects:
- **[Linear Regression](./ML/Linear_regression.py):** Predict, cost function, gradient descent — NumPy only. Trained on real gold price data.
- **[Logistic Regression](./ML/Logistic_regression.py):** Sigmoid, classification, confusion matrix, precision, recall, F1 — all from scratch.
- **[Decision Tree Math](./ML/Entropy.py):** Entropy and Information Gain implemented manually — the math behind Decision Trees.