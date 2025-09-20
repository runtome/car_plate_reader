from db import save_to_db

def db_worker(db_queue):
    while True:
        item = db_queue.get()
        save_to_db(item)
        print("Saved:", item)
