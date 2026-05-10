import datetime

class DevelopmentGuardian:
    # WHO Standart Gelişim Tablosu (Simüle edilmiş veri)
    WHO_STANDARDS = {12: {"height_cm": 74.0, "weight_kg": 9.2}}

    def __init__(self, birth_date="2025-04-12"):
        self.birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

    def evaluate_growth(self, current_height):
        age_months = (datetime.datetime.now() - self.birth_date).days // 30
        standard = self.WHO_STANDARDS.get(age_months, {"height_cm": 0})
        
        deviation = current_height - standard["height_cm"]
        return {
            "age": age_months,
            "status": "Healthy" if abs(deviation) < 5 else "Consult Pediatrician",
            "deviation": f"{deviation:+.2f} cm"
        }
      
