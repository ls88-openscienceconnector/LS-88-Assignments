test = {
    'name' : '',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> "Complaint_dt" in complaints.labels
                True
                >>> "CMPLNT_FR_DT" not in complaints.labels
                True
                >>> "CMPLNT_FT_TM" not in complaints.labels
                True
                >>> types = [type(i) for i in complaints["Complaint_dt"]]
                >>> dt.datetime in types
                True
                >>> str in types
                False
                >>> labels = ["Complaint_dt", "Latitude", "Longitude", "OFNS_DESC", "PD_DESC", "LAW_CAT_CD"]
                >>> sum([i in complaints.labels for i in labels])
                6
                >>> sum([i in labels for i in complaints.labels])
                6
                """
            }]
        }]
}
