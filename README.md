## Text-Mining Project: emoji Prediction of Tweets
by  **Jiarong Yu**, **Shuai Hao** and **Shuo Liu**
Dept. of Computer Science, Georgetown Univ.
Text Mining & Analysis (COSC-586), Fall 2017

### Division of work:
* **Jiarong Yu** and **Shuai Hao**: feature extraction and implementation;
* **Shuo Liu**: feature extraction (part of), baseline implementation, model training and evaluation.

### Code intro. & File structure:
├ **Data**
│  ├ tokenized trining & trial set ( *.tknz, delimiter=" " )
│  └ corresponding labels of each tweets ( *.label )
├ **evaluation**
│  ├ **models**
│  │  └ some of trained models saved for future checking out
│  ├ *evaluation.py*: code for evaluation
│  ├ reports on different methods: