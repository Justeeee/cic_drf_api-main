# cic_drf_api-main

This app is meant to be used by school to exchange with news in school:

It currently doesn't allow students/staff to login.
Solely, it's expected to be used on a single machine or online for managers only.

```
Run

```python
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration, or you can use the commmand below
make mig # migrations
python manage.py runserver # run the server
```
Then locate http://172.0.0.1:8000

## Roadmap
To build a fully fledged open source school management.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Coding Standards
```bash
isort .
black .
```

## Test
```base
python manage.py test
```
