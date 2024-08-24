```sh
pip list --format=freeze --local | grep -E "^(pandas|matplotlib|numpy|scikit-learn|seaborn|mlflow|pickleshare)==" > requirements.txt
```