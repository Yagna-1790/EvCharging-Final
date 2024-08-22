import datetime

def book_slot(station_name, start_time, end_time):
    # Mock booking process
    print(f"Booking a slot at {station_name} from {start_time} to {end_time}...")
    confirmation = True  # Simulate a successful booking
    
    if confirmation:
        print("Booking confirmed!")
        return True
    else:
        print("Booking failed!")
        return False

def get_available_slots():
    # Mock available slots
    now = datetime.datetime.now()
    return [
        (now + datetime.timedelta(hours=1), now + datetime.timedelta(hours=2)),
        (now + datetime.timedelta(hours=3), now + datetime.timedelta(hours=4)),
    ]
