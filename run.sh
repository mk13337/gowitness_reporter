gowitness file --file /data/urls.txt -t 10
cp -r /data/screenshots /app/screenshots
gowitness report serve --address 127.0.0.1:7171 &
cd /app
python3 main.py
cp -r /app/assets/ /app/gallery.html /app/table.html /app/perception.html /data/
