# GraFOCAL
*GraFOCAL*: Combining Semantic Graph Features and a Common Data
Model to Exploit the Interoperability of Patient Databases

**Authors:** Rafael C. G. Conrado<sup>1</sup>, Mirela T. Cazzolato<sup>2</sup>, Marco A. Gutierrez<sup>3</sup>, Agma J.M. Traina<sup>1</sup>, Caetano Traina Jr.<sup>1</sup>

**Affiliations:** <sup>1</sup> Institute of Mathematics and Computer Science (ICMC) University of São Paulo (USP) - São Carlos, Brazil, <sup>2</sup> Faculty of Philosophy, Sciences and Letters at Ribeirão Preto (FFCLRP) University of São Paulo (USP) - Ribeirão Preto, Brazil, <sup>3</sup> Institute of Heart (InCOR) Clinical Hospital of Faculty of Medicine (FMUSP) - São Paulo, Brazil  

**Conference:** [Simpósio Brasileiro de Bases de Dados, 2024 @ Florianópolis, Brazil.](https://sbbd.org.br/2024/)

Please cite the paper as:

```
@INPROCEEDINGS{243153,
    AUTHOR="Rafael Conrado and Marco Gutierrez and Caetano Traina Júnior and Agma Traina and Mirela Cazzolato",
    TITLE="Combining Semantic Graph Features and a Common Data Model to Exploit the Interoperability of Patient Databases",
    BOOKTITLE="SBBD 2024 - Short Papers () ",
    ADDRESS="",
    DAYS="14-17",
    MONTH="oct",
    YEAR="2024",
    ABSTRACT="Given a set of Electronic Health Records (EHRs), how can we semantically model the available concepts and provide tools for data analysis? EHRs following a common data model (CDM) such as OMOP usually provide meaningful organization and vocabulary to health-related databases, prompting data interoperability. However, hidden relationships among attributes within the CDM bring the need for CDM-tailored analysis tools regarding exploratory tasks. We propose GraFOCAL for analyzing CDM-based databases considering semantic graph features. GraFOCAL combines pairs of attributes with semantic descriptions in graph edges and node features. Preliminary results show the usefulness of GraFOCALs features and visual tools in spotting findings in a real-world dataset. In future work, we aim to extend the proposed approach with automatic knowledge inference for the semantic linkage between variables.",
    KEYWORDS="Data mining and analytics; Graphs, networks and semistructured data management; Information integration and interoperability; Knowledge bases, knowledge graphs, and modeling",
    URL="http://XXXXX/243153.pdf"
}
```
## Requirements

Check file `requirements.txt`

To create and use a virtual environment, type:

    python -m venv grafocal_venv
    source grafocal_venv/bin/activate
    pip install -r requirements.txt
 
 
## Running the app

Run the app with the following command on your Terminal:  

    streamlit run demo/main.py


## Data Sample






