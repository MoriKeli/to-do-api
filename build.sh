echo "--- BUILD START ---"

echo "Making migrations ..."

python manage.py migrate
python manage.py makemigrations

echo "--- END BUILD ---"