test = {
    'name' : '',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> near_11_taxis.num_rows
                1
                >>> near_11_taxis["Pickup_dt"][0] == dt.datetime(2016, 1, 4, 23, 2, 3)
                True
                """
            }]
        }]
}
