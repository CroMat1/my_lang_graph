examples= [
    {
        "question": "Give the CVfields of a view Calculation View ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001 ",
        "query": "MATCH (cv:CalculationView {{name: \"ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001\"}}) -[:HAS_FIELD]->(field:CVField) RETURN field",
    },
    {
        "question": "How many of calculation view are in?",
        "query": "MATCH (cv:CalculationView) RETURN count(cv)",
    },
    {
        "question": "Give the the properties of calculation view ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001",
        "query": "Match (cv:CalculationView {{name: \"ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001\"}}) return cv",
    },
    {
        "question": "Give me the lineage of CVField CHSBVERS of ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001 with all the element of the path",
        "query": "MATCH Path = (start:CVField {{Name:\"CHSBVERS\", parentCV: \"ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001\", parent_node: \"Semantics\"}}) -[:IS_MAPPED*]-(end:DBField) UNWIND Nodes(Path) as element RETURN element"
    },
    {
        "question": "Give me the lineage of CVField CHSBVERS of ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001 of node Projection_1 with all the element of the path",
        "query": "MATCH Path = (start:CVField {{Name:\"CHSBVERS\", parentCV: \"ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001\", parent_node: \"Projection_1\"}}) -[:IS_MAPPED*]-(end:DBField) UNWIND Nodes(Path) as element RETURN element"
    },
    {
        "question": "Give me the lineage of CVField CHSBVERS of ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001",
        "query": "MATCH Path = (start:CVField {{Name:\"CHSBVERS\", parentCV: \"ZSAC.ZBDG.ZRETAIL.ZHS/CVHSB001\", parent_node: \"Semantics\"}}) -[:IS_MAPPED*]-(end:DBField) UNWIND Nodes(Path) as element RETURN element"
    },
]