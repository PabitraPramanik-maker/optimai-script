## Setup

1. Clone the repository or download the script files.

git clone https://github.com/PabitraPramanik-maker/optimai-script.git
cd optimai-script

2.Create a file named tokens.txt in the project folder and add your OptimAI access tokens, one per line:

your_access_token_1
2..
3...

3.Create a file named proxies.txt in the project folder and add your HTTP proxies, one per line, in this format:
http://123.45.67.89:8080
http://98.76.54.32:3128

If you do not want to use proxies, leave this file empty or add one line with None.

4.Install required Python packages:

pip install rich pyfiglet

5.Run the script:
python optimx.py

git add README.md
git commit -m "Update README with Setup instructions"
git push origin main
