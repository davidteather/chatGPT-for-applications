# chatGPT-for-applications
Generate cover letters, resumes, and more with chatGPT!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/davidteather/) [![Sponsor Me](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub)](https://github.com/sponsors/davidteather)  [![GitHub](https://img.shields.io/github/license/davidteather/TikTok-Api)](https://github.com/davidteather/TikTok-Api/blob/master/LICENSE) ![](https://visitor-badge.laobi.icu/badge?page_id=davidteather.chatGPT-for-applications) [![Support Server](https://img.shields.io/discord/783108952111579166.svg?color=7289da&logo=discord&style=flat-square)](https://discord.gg/yyPhbfma6f)


## Getting Started

### Installation

Requires python 3.7+

Download or clone the code first
```
pip install -r requirements.txt
```

Finish installing playwright
```
python -m playwright install
```

### Getting Setup

Update `my_links.txt` with links to your website and other pages you'd like to prompt chatGPT with. Make sure that the first line of the file is your name.

Here's my current example
```
David Teather
https://dteather.com/
https://dteather.com/summer-2022-collab/
https://dteather.com/spring-2022-advent-international/
https://dteather.com/summer-2021-warner-music-group-copy/
```

> **Note:** It currently works best with blog-like formatting (and websites without much Web Scraping). I'm going to try to get it work with LinkedIn better in the future.

### Running the code

Just run
```
python main.py
```

Make sure you follow instructions in the terminal after that!

## Examples
Check out [prompts.md](./prompts.md) for more prompts and tips!

I will say because of the amount of content I have online, it's easier for me to bulk prompt it with references to myself.

> **Prompt: Write me a detailed convincing cover letter applying to Google as a software engineering intern with an introductory story evoking emotion that this is my dream job**

> Dear Hiring Manager at Google,
>
> As a software engineering intern at Google, I would be able to fulfill my dream of working at the forefront of technology and innovation. I am excited at the prospect of contributing to projects that have a meaningful impact on people's lives, and I am confident that my skills and experiences make me an excellent fit for this role.
> 
> As a computer science major at the University of Wisconsin - Madison, I have gained a strong foundation in algorithms, data structures, and software development. I have also completed coursework in machine learning and artificial intelligence, giving me a glimpse of the cutting-edge technologies that drive Google's success.
> 
> In addition to my academic background, I have hands-on experience as a software engineering intern at several companies. At Advent International Global Private Equity, I used data science to estimate the number of customers of target companies, helping the company make informed investment decisions. At Warner Music Group, I developed a web tool for managing and viewing Ruby Resque jobs, improving developer productivity. And at TrendPop, I developed a producer consumer web crawler in Python, increasing customer satisfaction.
> 
> Furthermore, I have a passion for open-source software and have developed an open-source Python package called TikTokAPI, which has been cited in over 10 academic papers and is used by over 250 companies. This project has gained 700K+ downloads and 2.5K+ GitHub stars, and has given me experience in cultivating an open-source community.
> 
> I am a quick learner and a team player, and I am eager to apply my skills and experiences to the challenges and opportunities at Google. I am confident that I would make valuable contributions as a software engineering intern at Google, and I am excited at the prospect of joining the team.
> 
>Sincerely,
>David Teather

> **Prompt: Write me a detailed convincing cover letter including important career highlights for me that would get me accepted to Google as a software engineering intern with an introductory story evoking emotion that this is my dream job**

> Dear Hiring Manager,
> 
> I am writing to apply for the software engineering intern position at Google. As a current computer science major at the University of Wisconsin-Madison, I am eager to apply my technical skills and problem-solving abilities at a company as innovative and forward-thinking as Google.
>
> Since I was a child, I have been fascinated by technology and the endless possibilities it presents. The thought of working for a company like Google, where I could be a part of developing cutting-edge technology and making a meaningful impact, is truly a dream come true for me.
>
> Throughout my academic and professional career, I have gained a strong foundation in computer science and have proven my ability to apply my knowledge in real-world settings. As a software engineering intern at Collab, I have closed additional enterprise customers by extracting and storing over 1 billion records from a new data source. I have also increased request throughput by 450M requests/day by creating an efficient API-based abstraction using Go. In addition, I have future-proofed jobs with Apache Spark in Scala, enabling horizontal job scaling in the future.
>
> In my other internships at Advent International Global Private Equity and Warner Music Group, I have demonstrated my ability to deliver valuable insights and increase ROI. At Advent, I estimated the number of customers of target companies, resulting in a more informed investment decision. At Warner Music Group, I introduced a new data source, enabling deeper analysis of the industry and increasing the ROI of 30% of musician signings and 99% of investment decisions.
>
> In addition to my professional experience, I have also developed a passion for security analysis and research. Through my personal blog, The Response Times, I have documented my exploits and security analysis of various software. My research has been featured in publications such as Vice and The Verge, and has helped to improve the security of software used by millions of people.
>
> I am confident that my technical skills, problem-solving abilities, and passion for technology make me an ideal candidate for this internship at Google. I am excited at the prospect of joining a team of talented and innovative individuals, and I am eager to contribute to the continued success of Google. Thank you for considering my application.
>
> Sincerely,
> David Teather
