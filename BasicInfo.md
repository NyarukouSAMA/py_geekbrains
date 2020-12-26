# Python-project basic knowledge
After you create work directory and add it to git you will need to do some actions and implement some settings.

1. First of all you should set virtual environment. It's very important. To do it you should open terminal and run next command: <code>python -m venv env</code>. **env** - it's name of the local directory, where your virtual environment will be created.
2. After creating you should activate it. Actition script will be placed by path something similar to this:**env/Scripts/Activate.ps**. If vscode is used, then it should be enough to select interpreter from virtual enironment and start it (venv will be activated).
3. Do not forget to create readme (it's allready created) =) It should be of format .txt or .md
4. To guarantee dependency consistency you should create file **requirements.txt**. To do it run: <code>pip freeze > requirements.txt</code>. Each time you add or update libraries in project you should update this file.
5. To start work with existing project you should install libs from **requirements.txt**. For this run <code>pip install -r requirements.txt</code>