import requests

def search_school(api_key, school_name):
    base_url = 'https://api.data.gov/ed/collegescorecard/v1/'
    endpoint = 'schools'
    
    params = {
        'api_key': api_key,
        'school.name': school_name,
    }

    response = requests.get(f'{base_url}{endpoint}', params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results')

        if results:
            location_info = results[0].get('location')
            if location_info:
                latitude = location_info.get('lat')
                longitude = location_info.get('lon')
                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")

            latest_info = results[0].get('latest')
            if latest_info:
                school_info = latest_info.get('school')
                if school_info:
                    zip_code = school_info.get('zip')
                    city = school_info.get('city')
                    state = school_info.get('state')
                    address = school_info.get('address')
                    school_url = school_info.get('school_url')
                    online_only = school_info.get('online_only')

                    print(f"Zip Code: {zip_code}")
                    print(f"City: {city}")
                    print(f"State: {state}")
                    print(f"Address: {address}")
                    print(f"School URL: {school_url}")
                    print(f"Online Only: {'Yes' if online_only == 1 else 'No'}")

                    cost_info = latest_info.get('cost')
                    if cost_info:
                        booksupply_cost = cost_info.get('booksupply')
                        tuition_info = cost_info.get('tuition')
                        in_state_tuition = tuition_info.get('in_state')
                        out_of_state_tuition = tuition_info.get('out_of_state')

                        print(f"Book and Supply Cost: ${booksupply_cost}")
                        print(f"In-State Tuition: ${in_state_tuition}")
                        print(f"Out-of-State Tuition: ${out_of_state_tuition}")

        else:
            print(f"No results found for '{school_name}'.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    api_key = 'kK3BZnAbjkyuoZuB4BW2VapEPB7Z0giWOkm8uKb4'

    school_name = input("Enter the name of the school: ")

    search_school(api_key, school_name)

if __name__ == "__main__":
    main()
