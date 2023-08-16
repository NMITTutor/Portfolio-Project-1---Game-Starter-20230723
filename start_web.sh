#source venv/Scripts/activate
cd webserver
python local_server.py &
cd ..
uvicorn main:app  --reload --host 0.0.0.0 --port 8000

