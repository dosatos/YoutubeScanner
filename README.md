To run the script, one has to add the environment variable
```bash
export google_api_key=<YOUR_GOOGLE_API_TOKEN>
```

If you run it with pycharm, you should make sure you set the environment variable accordingly.

```bash
poetry init
poetry install
ln -s $(poetry env info --path) .venv
```

### How to deploy to AWS lambda

Docs: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

```
cd YoutubeScanner
pip install -r requirements.txt -t ./package
zip -r my-deployment-package.zip ./package/
zip -r -g my-deployment-package.zip src/ -x '*.pytest_cache*' '*__pycache__*'
aws lambda update-function-code --function-name YoutubeScannerLambda --zip-file fileb://my-deployment-package.zi
```
