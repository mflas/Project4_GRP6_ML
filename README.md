# Project4_GRP6_ML
you will work with your group to solve, analyze, or visualize a problem using machine learning (ML) with the other technologies we’ve learned

Open the Project_4_Assessment to access the tool for the webpage and too
Data analysis is included in the Python model Project4_Working_Part1_Analysis.ipynb
Machine Learning Model build in Colab file reference Project4_Working_2FINAL.ipynb

The machine learning model and Data Analysis is in Project4_Working 2FINAL, accessible via Google Colab.

- This project dependencies will be installed in this environment.
- Note: This should contain only python 3.7—and not anaconda.
```bash
conda create -n pythondata python=3.7
```
- Activate this new environment before proceeding.
```bash
conda activate pythondata
# Note: If you run into issues, try the following command instead.
source activate pythondata
```
- Install the libraries into your new environment. You will need additional libraries for postgres, mongodb, etc when you create your own project.
```bash
# install pip packages listed in requirements file
pip install -r requirements.txt
```
- Next, to make the run.sh file executable, run the following command:
```bash
chmod a+x run.sh
```
You can test the application by running the following in your command line.
```bash
./run.sh
```
- Navigate to 127.0.0.1:5000 to view your webpage and test out the app locally.
- There's more work involved in getting the app live in the internet but for this project local server is fine...
    - Note that you can't host flask applications in `GitHub Pages` because it's limited to simple static web pages.
