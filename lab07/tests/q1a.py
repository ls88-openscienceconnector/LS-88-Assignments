test = {
    'name' : '',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> sum([i in taxis.labels for i in ('Pickup_dt', 'Dropoff_dt', 'Pickup_longitude', 'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude', 'Passenger_count')])
                7
                >>> sum([i not in ('Pickup_dt', 'Dropoff_dt', 'Pickup_longitude', 'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude', 'Passenger_count') for i in taxis.labels])
                0
                >>> sum([i in complaints.labels for i in ('CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'OFNS_DESC', 'PD_DESC', 'LAW_CAT_CD', 'Latitude', 'Longitude')])
                7
                >>> sum([i not in ('CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'OFNS_DESC', 'PD_DESC', 'LAW_CAT_CD', 'Latitude', 'Longitude') for i in complaints.labels])
                0
                """
            }]
        }]
}
