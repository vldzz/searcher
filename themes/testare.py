testare = {
    "testare": "Testarea este procesul de analiza a software-ului si a documentatiei pentru a identifica defectele si "
               "respectiv a imbunatati calitatea produsului",
    "calitate": "masura in care caracteristicele reale corespund cerintelor fata de acesta",
    "qa": "un set de activitati ce acopera toate etapele dezvoltarii unui produs software",
    "qc": "analiza rezultatelor testarii si calitatii in procesul de dezvoltare",
    "50": "testarea exhaustiva",
    "exchaustiv": "verificarea tuturol posibilitatilor de executie cu toate datele posibile",
    "70": "positive/negative testing",
    "80": "testarea este aplicata pe intreg app life cycle",
    "90": "tranzactia de la testare la quality assurance. Include: planificare, proiectare, creare si executare a "
          "scenariilor de testare",
    "2000": "Apar metodologii complexe",

    # principii si axiome
    "principii": [
        "testarea identifica PREZENTA unor defecte",
        "nu poate fi efectuata o testare exhaustiva",
        "testarea trebuie sa inceapa cat mai devreme in project life cicle",
        "defectele tind sa se grupeze",
        "paradoxul pesticidelor. defectele ce au supravietuit unui tip de testare, vor supravietui si dupa a 2 testare",
        "testarea depinde de context",
        "aparenta absentei erorilor nu inseamna ca nu exista erori",
    ],
    "axiome": [
        "testul bun permite detectarea erorii, nu functionarea corecta a programului",
        "cel mai greu in testare e de a decide cand sa fie terminata",
        "Testarea nu poate fi efectuata de un programator. Trebuie sa fie extrem de distructiva",
        "Descrierea rezultatelor asteptate",
        "Testele trebuie documentate intr-un format ce permite reutilizarea acestora",
        "testare atat pozitiva, atat si negativa",
        "testarea incepe cu stabilirea obiectivelor"
    ],

    # Ciclurile de dezvoltare a software-ului (SDLC)
    "ciclu": [
        "ciclu de viata(sdlc) este un proces sistematic de dezvoltare a produsului software asiguranduse calitatea "
        "acestuia",
        "este divizat in: 1.Colectarea cerintelor, 2.Evaluarea detaliata, 3.Proiectarea, 4.Codificarea, 5.Testarea, "
        "6.Instalarea, 7.Intretinerea",
        "ofera o baza pentru evaluare si planificare",
        "este un mecanism de monitorizare si control a proiectului",
        "imbunatateste vizibilitatea planificarii proiectului",
        "creste si accelereaza dezvoltarea",
        "contribuie la reducerea riscurilor si a costului de gestionare a proiectului"
    ],

    # metodologii de dezvoltare
    "cascada": [
        "vechi, nu este aplicabil",
        "etapa curenta trebuie sa fie finisate inainte de a trece la urmatoarea",
        "echipa vede doar faza anterioara si urmatoarea",
        "usor de a gestiona un proiect",
        "nu se poate de facut un pas inapoi",
        "o cantitate enorma de documentatie",
        "exemple: soft aerian, medical, militar",
        "testarea incepe la sfarsit",
        "costul mare a update-urilor",
        "Etape: 1.planificare, 2.Cerinte sistem, 3.Cerinte soft, 4.Proiectarea tehnica, 5.Design detaliat, "
        "6.Dezvoltare si depanare, 7.Integrare si testare modulara, 8.Testarea instalarii, 9.Testarea sistemica, "
        "10.Testarea de acceptare. 11.Raportare finala"
    ],

    "v": [
        "cost mare",
        "pentru sisteme ce funcioneaza continuu",
        "sisteme de intretinere a vietii, sistem de control airbag",
        "testarea incepe la inceputul proiectului",
        "testare minutioasa a proiectului",
        "pentru proiecte mici/medii cu cerinte clar definite",
        "Etape: 1.Planificare, 2.Cerinte sistem, 3.Cerinte soft, 4.Proiectare tehnica, 5.Design detaliat, "
        "6.Dezvoltare si depanare, 7.Integrare si testare modulara, 8,testarea instalarii, 9.testarea sistemica, "
        "10.testarea de acceptare, 11.raportarea finala "
    ],

    "iterativ": [
        "este suficienta o parte din cerintele produsului pentru fiecare iteratie",
        "versiunea poate sa nu fie perfecta, important sa functioneze",
        "intr-o afacere dinaimica",
        "obiectivul principal sau viziunea produsului sunt definite, dar detaliile pot evolua in timp",
        "proiectul este mare sau foarte mare",
        "oamenii si interactiunea sunt mai importanti decat proceselor si instrumentele",
        "un produs ce functioneaza este mai important decat o documentatie completa",
        "colaborarea cu clientul este mai importanta decat a se conveni asupra conditiilor contractului"
    ],

    "agile": [
        "o continuare a modelelor cascada, v, iterativ",
        "dezavantajele constau in ceea ca e dificil de a se evalua costul muncii pentru dezvoltare",
        "dupa fiecare iteratie, clientul poate observa rezultatul",
        "se bazeaza pe intruniri zilnice repetate regulate",
        "proiecte mari, sau ciclu de viata lung"
    ],

    "cerinta": "descriere bine definita a unui set de caracteristici utile pentru user pe care aceasta se asteapta "
               "sa le aiba produsul ",
    "cerinte": [
        "exhaustivitate", "atomicitate", "consistenta", "claritate", "necesitate", "fezabilitate"
    ],
    "exhaustivitate": "cerinta e completa si exhaustiva atunci cand sunt prezentate toate informatiile necesare",
    "atomicitate": "o cerinta este atomica daca nu poate fi impartita in cerinte separate fara a pierde din "
                   "exhaustivitate si descrie o situatie",
    "consistenta": "cerinta nu va contine contradictii interne si contradictii cu alte cerinte si documente",
    "claritate": "cerinta este descrisa clar",
    "fezabilitate": "cerinta este fezabila din punctul de vedere tehnologic si poate fi realizata cu bugetul si in "
                    "termenul propus ",
    "necesitate": "daca cerinta nu este obligatorie, aceasta ar trebui exclusa din setul de cerinte",

    # bugs
    "bug": "functionale, vizuale, logice, continut, uzabilitate",
    "functionale": [
        "nu pot fi salvate modificari de date ale utilizatorilor",
        "articolul nu poate fi sters din cos",
        "nu poate fi adaugat un comentariu",
        "nu functioneaza sistemul de cautare",
        "nu functioneaza sistemul de sortare"
    ],
    "vizuale": [
        "nu se afiseaza imaginea",
        "textul este decupat",
        "font nepotrivit",
        "imaginea suprapune textul"
    ],
    "logice": [
        "poate fi setata data de nastere ca o data viitoare",
        "o logica de cautare invalida pentru un anumit item pe pagina web, in magazin",
        "puteti comanda o livrare prin curier, fara a specifica adresa de livrare"
    ],
    "continut": [
        "greseli de ortografie si punctuatie",
        "imaginea produsului nu se potriveste cu descrierea acestuia",
        "pe pagina web sunt plasate texte in mai multe limbi"
    ],

    "bug report": [
        "furnizarea informatiei despre o problema",
        "prioritizarea problemei",
        "contributie la eliminarea problemei",

        "contine: identificator, o scurta denumire(summary)(ce, unde si cum), descriere detaliata, preconditions, "
        "steps to reproduce, actual result, severity, priority, mediul, comentarii, atasamente, statu(new, asigned, "
        "open, etc.)"
    ],
    "test case": [
        "descriere pas cu pas a testarii, cu nivel de detaliere ce permite oricarui noob sa-l poata realiza",
        "contine: identificator, name, preconditions, pasi, expected result"
    ],
    "test plan": "constituie un document ce descrie totalitatea activitatilor de testare",

    # Box testing
    "black": "Nu avem acces la cod",
    "white": "Avem acces la cod",
    "gray": "Mix din black and white",

    # Testare unitară, de integrare, de sistem, de acceptare
    "tipuri": [
        "unitara - elemente mici ale aplicatiei",
        "de integrare - intereactiunea intre mai multe elemente",
        "de sistem - aplicatia in ansamblu",
        "de acceptare - in ce masura produsul este gata de a fi livrat. se face de client, sau testerii clientului",

        "regresie - verificarea functionalitatii existente dupa efectuarea corectiilor in sistem",
        "retestarea - pentru a confirma corectarea erorilor si functionarea sistemului (dupa remedierea unui bug",

        "alpha - verificarea unui sistem la inceput. efectuat de testeri calificati",
        "beta - o versiune complexa a sistemului. evaluarea din punct de vedere a viitorilor clienti",
        "gamma - etapa finala de testare inainte de lansarea finala. Include la maxim clientii",

        "positive - examinarea aplicatiei fara folosirea datelor incorecte",
        "negative - examinarea aplicatiei folosind date incorecte",

        "functional - verifica daca sistemul corespune cu cerintele clientului",
        "nefunctional - uzabilitate, performanta, incarcare, securitatea, instalare, compabilitate, localizare, "
        "accesibilitate, stres"
    ],

    "regresie": "verificarea functionalitatii existente dupa efectuarea corectiilor in sistem",
    "retestarea": "pentru a confirma corectarea erorilor si functionarea sistemului (dupa remedierea unui bug",

    "alpha": "verificarea unui sistem la inceput. efectuat de testeri calificati",
    "beta": "o versiune complexa a sistemului. evaluarea din punct de vedere a viitorilor clienti",
    "gamma": "etapa finala de testare inainte de lansarea finala. Include la maxim clientii",

    "functional": "verifica daca sistemul corespune cu cerintele clientului",
    "nefunctional": "uzabilitate, performanta, incarcare, securitatea, instalare, compabilitate, localizare, "
                    "accesibilitate, stres",

    "performanta": "verificarea vitezei software-ului sau a functiilor acestuia",
    "incarcare": "testarea timpului de raspuns la diferite requesturi",
    "instalare": "verificarea procesului de instalare, configurare, dezinstalare",
    "uzabilitate": "comoditatea de utilizare a aplicatiei de catre utilizatori finali",
    "compabilitate": "veificarea soft-ului in diferite configuratii de sistem",
    "securitatea": "este protejata sau nu aplicatia",
    "localizare": "controlul corectitudinii si calitatii adaptarii produsului la utilizarea intr-o anumita limba",
    "accesibilitate": "analiza adecvarii unui produs pentru persaone cu dizabilitati",
    "stres": "testarea in conditii critice, de stres"


}
