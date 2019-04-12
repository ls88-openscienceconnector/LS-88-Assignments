test = {
    'name' : '',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> types = [type(i) for i in taxis['Pickup_dt']]
                >>> dt.datetime in types
                True
                >>> str in types
                False
                >>> types = [type(i) for i in taxis['Dropoff_dt']]
                >>> dt.datetime in types
                True
                >>> str in types
                False
                """
            }]
        }]
}
