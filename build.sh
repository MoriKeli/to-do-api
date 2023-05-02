echo "--- BUILD START ---"

echo "Installing dependencies ..."
pip install -r requirements.txt

echo "Making migrations ..."

python manage.py migrate
python manage.py makemigrations

echo "--- END BUILD ---"