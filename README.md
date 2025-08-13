<!-- Header with animated capsule -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:6ec9ff,100:b388ff&text=Soheil%20Salmani&fontAlign=50&fontAlignY=38&fontSize=38&desc=Data%20Engineer%20%7C%20Python%20%7C%20ETL%20%26%20Analytics&descAlign=50&descAlignY=62&fontColor=ffffff" alt="header"/>
</p>

<!-- Typing effect -->
<p align="center">
  <a href="https://github.com/SoheilGtex">
    <img src="https://readme-typing-svg.herokuapp.com?color=6EC9FF&center=true&vCenter=true&width=700&lines=Data+Engineer+%E2%80%94+Python+%E2%80%94+ETL%2C+BI%2C+EDA;Financial+Data+Pipelines+%26+Analytics;Open+to+Work+%28Germany+%2F+Ireland%29"/>
  </a>
</p>

<!-- Badges -->
<p align="center">
  <img src="https://komarev.com/ghpvc/?username=SoheilGtex&style=for-the-badge&color=6ec9ff" />
  <img src="https://img.shields.io/badge/Python-3.11+-6ec9ff?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-PostgreSQL%20%7C%20SQLite-b388ff?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/ETL-Pandas%20%7C%20NumPy-6ec9ff?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-Bash-b388ff?style=for-the-badge&logo=linux&logoColor=white" />
</p>

---

## 👋 About me
- Data engineer و توسعه‌دهنده Python؛ تمرکز روی **دریافت/پاکسازی دیتا، ETL و آنالیز** مخصوصاً در دامنه **داده‌های مالی و BI**  
- ساخت **پایپ‌لاین‌های سریع و مطمئن**، استانداردسازی دیتاست‌های بزرگ، و همکاری نزدیک با تیم‌های تحلیل/داشبورد  
- فعال برای **Remote** و **Relocation** (آلمان / ایرلند)  

**Contact:**  
- Email: <a href="mailto:Soheilsalmanisafarpour@gmail.com">Soheilsalmanisafarpour@gmail.com</a>  
- LinkedIn: <a href="https://www.linkedin.com/in/soheil-salmani-822b89232">linkedin.com/in/soheil-salmani-822b89232</a>  
- GitHub Pages (Resume Site): <a href="https://soheilgtex.github.io">soheilgtex.github.io</a> *(اگر فعال کردی)*

---

## 🧰 Tech Stack (visual)
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="36" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="36" />
</p>

---

## 🚀 Featured Projects (cards)
<a href="https://github.com/SoheilGtex/finance-data-pipelines-pro-crypto">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=SoheilGtex&repo=finance-data-pipelines-pro-crypto&theme=react&hide_border=true" />
</a>
<a href="https://github.com/SoheilGtex/voice-cloning-sv2tts-pro">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=SoheilGtex&repo=voice-cloning-sv2tts-pro&theme=react&hide_border=true" />
</a>

---

## 📊 GitHub Analytics (animated / charts)
<p>
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=SoheilGtex&show_icons=true&theme=react&hide_border=true" />
  <img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=SoheilGtex&theme=react&hide_border=true" />
</p>

<p>
  <img height="200" src="https://github-readme-activity-graph.vercel.app/graph?username=SoheilGtex&bg_color=0d1117&color=6ec9ff&line=b388ff&point=6ec9ff&area=true&hide_border=true" />
</p>

<p>
  <img src="https://github-profile-trophy.vercel.app/?username=SoheilGtex&theme=onestar&no-frame=true&row=1&column=6" />
</p>

<!-- Contribution Snake (needs workflow below) -->
<p align="center">
  <img src="https://raw.githubusercontent.com/SoheilGtex/SoheilGtex/output/snake.svg" alt="snake"/>
</p>

---

## 🎓 Education & Certs (highlights)
- B.Sc. Mathematics and Applications — Kharazmi University (2024– )  
- **CS50x Puzzle Day (2023–2025)**, **CS50x**, **freeCodeCamp (Data Analysis / ML / Sci. Computing)**  
- Microsoft Learn, Udemy (Python & Git), Mimo (Python/SQL)

---

## 📝 Resume
- نسخه PDF: [Download CV](./resume/Soheil_Salmani_CV.pdf) *(فایل PDF رو داخل مسیر `resume/` اضافه کن)*  
- نسخه وب (glass UI): [Open](https://soheilgtex.github.io) *(اگر GitHub Pages رو فعال کردی)*

---

## 📦 Sample: Minimal ETL Snippet
```python
import pandas as pd, requests
df = pd.DataFrame(requests.get("https://api.coindesk.com/v1/bpi/historical/close.json").json()["bpi"].items(),
                  columns=["date","close"])
df["date"] = pd.to_datetime(df["date"])
df["return"] = df["close"].pct_change().fillna(0)
df.tail()
