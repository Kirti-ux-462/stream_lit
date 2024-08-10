import streamlit as st

def calculate_travel_cost(distance, vehicle_type):
    # Example cost calculations based on vehicle type
    costs_per_km = {
        'Car': 0.5,   # cost per km in dollars
        'Bus': 0.2,
        'Train': 0.3,
        'Airplane': 1.0
    }
    return costs_per_km.get(vehicle_type, 0) * distance

def main():
    st.title('Travel Planner App')

    # Input fields
    st.sidebar.header('Travel Parameters')
    distance = st.sidebar.number_input('Distance (in km)', min_value=1, value=100)
    num_members = st.sidebar.number_input('Number of Members', min_value=1, value=1)
    vehicle_type = st.sidebar.selectbox('Type of Vehicle', ['Car', 'Bus', 'Train', 'Airplane'])

    # Calculate cost
    total_cost = calculate_travel_cost(distance, vehicle_type)
    cost_per_person = total_cost / num_members

    # Display results
    st.write(f'### Total Travel Cost')
    st.write(f'For a distance of {distance} km using a {vehicle_type},')
    st.write(f'the total cost is: ${total_cost:.2f}')
    st.write(f'The cost per person is: ${cost_per_person:.2f}')

if __name__ == '__main__':
    main()
