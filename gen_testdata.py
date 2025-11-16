import random
import string
from datetime import datetime, timedelta
from typing import Dict, List

def generate_rdks_test_data_point() -> Dict:
    """
    Generates a single randomized RDKS test data point with realistic values.
    
    Returns:
        dict: A dictionary with the specified structure and randomized values.
    """
    # Random timestamp within the last 7 days
    now = datetime.utcnow()
    random_offset = timedelta(days=random.randint(0, 7), 
                              hours=random.randint(0, 23), 
                              minutes=random.randint(0, 59), 
                              seconds=random.randint(0, 59))
    timestamp = (now - random_offset).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Random line (A, B, C, D)
    lines = ["A", "B", "C", "D"]
    linie = random.choice(lines)

    # Random vehicle ID: TRL-YYYY-XXX
    year = random.randint(2020, 2025)
    vehicle_id = f"TRL-{year}-{random.randint(1, 999):03d}"

    # Random sensor ID: SENS-XX-XXX
    sensor_types = ["VA", "VB", "VC", "VD", "HA", "HB", "HC", "HD"]
    sensor_positions = ["VL", "VR", "HL", "HR"]
    sensor_type = random.choice(sensor_types)
    sensor_position = random.choice(sensor_positions)
    sensor_id = f"SENS-{sensor_type}-{sensor_position}"

    # Random radposition (VL, VR, HL, HR)
    radposition = sensor_position

    # Random values with realistic ranges
    druck_bar = round(random.uniform(1.8, 3.5), 2)
    temperatur_C = round(random.uniform(15.0, 35.0), 1)
    batterie_V = round(random.uniform(2.5, 3.2), 1)

    # Status: OK, WARN, FAIL (with 85% OK, 10% WARN, 5% FAIL)
    status_probs = ["OK"] * 85 + ["WARN"] * 10 + ["FAIL"] * 5
    status = random.choice(status_probs)

    # Error code: null or random error code
    error_code = None if status == "OK" else f"ERR-{random.randint(100, 999)}"

    # CAN ID: random 32-bit hex
    can_id = f"0x{random.randint(0x10000000, 0x1FFFFFFF):08X}"

    # Operator: random name from list
    operators = ["Linda", "Max", "Anna", "Tom", "Sara", "Felix", "Julia", "Paul"]
    operator = random.choice(operators)

    # Test station: random name
    stations = ["Nördlingen-1", "Nördlingen-2", "München-1", "Stuttgart-1", "Frankfurt-1"]
    teststation = random.choice(stations)

    # Return the complete data point
    return {
        "id": random.randint(1, 10000),
        "timestamp": timestamp,
        "linie": linie,
        "fahrzeugId": vehicle_id,
        "sensorId": sensor_id,
        "radposition": radposition,
        "druck_bar": druck_bar,
        "temperatur_C": temperatur_C,
        "batterie_V": batterie_V,
        "status": status,
        "errorCode": error_code,
        "canId": can_id,
        "operator": operator,
        "teststation": teststation
    }

    # Realistic timestamp (within last 7 days).
    # Valid fahrzeugId format: TRL-YYYY-XXX.
    # Realistic sensor IDs and positions.
    # Physical values within plausible ranges (e.g., pressure: 1.8–3.5 bar, temp: 15–35°C).
    # Status distribution: 85% OK, 10% WARN, 5% FAIL.
    # errorCode is null if status is OK.
    # Random CAN ID in hex format.
    # Random operator and test station.
