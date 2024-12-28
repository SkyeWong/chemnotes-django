from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=50)
    dse_topic = models.SmallIntegerField(
        "DSE syllabus",
        choices={
            1: "Planet Earth",
            2: "Microscopic World I",
            3: "Metals",
            4: "Acid and Bases",
            5: "Fossil Fuels and Carbon Compounds",
            6: "Microscopic World II",
            7: "Redox Reactions, Chemical Cells and Electrolysis",
            8: "Chemical Reactions and Energy",
            9: "Rate of Reaction",
            10: "Chemical Equilibrium",
            11: "Chemistry of Carbon Compounds",
            12: "Patterns in the Chemical World",
            13: "Elective: Industrial Chemistry",
        },
    )
    self_topic = models.SmallIntegerField(
        "Self-defined topic",
        choices={
            1: "Microscopic World",
            2: "Metals",
            3: "Acid Base and Patterns in the Chemical World",
            4: "Organic Chemistry",
            5: "Redox Reactions",
            6: "Reactions and Energy",
            7: "Equilibrium and Rate of Reaction",
            8: "Mole and Molar Volume",
            9: "Elective: Industrial Chemistry",
        },
    )

    update_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="notes")
