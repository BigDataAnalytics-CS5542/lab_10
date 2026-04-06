# src/dictionaries.py

SUBSTANCE_TERMS = {
    "opioids": [
        r"\bheroin\b", r"\bfentanyl\b", r"\boxycodone\b", r"\boxycontin\b", 
        r"\bvicodin\b", r"\bpercocet\b", r"\bdope\b", r"\bsmack\b", r"\broxies\b"
    ],
    "stimulants": [
        r"\bmeth(?:amphetamine)?\b", r"\bcocaine\b", r"\badderall\b", r"\bcrack\b", 
        r"\bice\b", r"\bcrystal\b", r"\bblow\b", r"\buppers\b"
    ],
    "benzodiazepines": [
        r"\bxanax\b", r"\bvalium\b", r"\bklonopin\b", r"\bbenzos?\b", 
        r"\bbars\b", r"\bzannies\b"
    ],
    "alcohol": [
        r"\balcohol\b", r"\bbooze\b", r"\bliquor\b", r"\bdrunk\b", r"\bdrinking\b"
    ]
}

DISTRESS_AND_RELAPSE_TERMS = [
    r"\brelapse[sd]?\b", r"\bslip(?:ped)? up\b", r"\bfell off\b", r"\busing again\b",
    r"\bcravings?\b", r"\bwithdrawals?\b", r"\bdetox\b", r"\bhopeless\b",
    r"\bsuicidal\b", r"\bcan'?t take it\b", r"\bgiving up\b", r"\bruin(?:ed)? my life\b",
    r"\bhit rock bottom\b"
]