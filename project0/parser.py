class Incident:
    def __init__(
            self,
            date_time,
            incident_number,
            location,
            nature,
            incident_ori):
        self.date_time = date_time
        self.incident_number = incident_number
        self.location = location
        self.nature = nature
        self.incident_ori = incident_ori

    def __eq__(self, other):
        if (isinstance(other, Incident)):
            return self.date_time == other.date_time and self.incident_number == other.incident_number and self.location == other.location and self.nature == other.nature and self.incident_ori == other.incident_ori

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return f'Incident (\n\tDateTime: {self.date_time}\n\tIncidentNumber: {self.incident_number}\n\tLocation: {self.location}\n\tNature: {self.nature}\n\tIncidentORI: {self.incident_ori}\n)'


def extract_incidents(incidents: list) -> list[Incident]:
    parsed_incidents: list[Incident] = []
    for incident in incidents:
        parsed_incidents.append(Incident(
            incident[0],
            incident[1],
            incident[2],
            incident[3],
            incident[4]
        ))

    return parsed_incidents
