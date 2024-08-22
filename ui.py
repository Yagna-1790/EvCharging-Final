import finder
import booking

def display_stations(stations):
    print("\nNearby EV Charging Stations:")
    for i, station in enumerate(stations):
        print(f"{i+1}. {station['AddressInfo']['Title']} - {station['AddressInfo']['AddressLine1']}")

def main():
    lat = float(input("Enter your latitude: "))
    lon = float(input("Enter your longitude: "))
    
    stations = finder.find_ev_stations(lat, lon)
    
    if stations:
        display_stations(stations)
        choice = int(input("Select a station number to book: ")) - 1
        
        if 0 <= choice < len(stations):
            station = stations[choice]
            available_slots = booking.get_available_slots()
            
            print("\nAvailable Slots:")
            for i, (start, end) in enumerate(available_slots):
                print(f"{i+1}. {start} to {end}")
            
            slot_choice = int(input("Select a slot number to book: ")) - 1
            
            if 0 <= slot_choice < len(available_slots):
                start_time, end_time = available_slots[slot_choice]
                booking.book_slot(station['AddressInfo']['Title'], start_time, end_time)
            else:
                print("Invalid slot choice!")
        else:
            print("Invalid station choice!")
    else:
        print("No stations found.")

if __name__ == "__main__":
    main()
