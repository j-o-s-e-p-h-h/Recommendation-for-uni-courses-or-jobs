# ============================================================
#  Botswana Career & Course Recommendation Data
#  Structured as a nested dictionary tree:
#  interest -> career/course -> details
# ============================================================
 
data = {
 
    # ─────────────────────────────────────────────
    #  1. TECHNOLOGY & COMPUTING
    # ─────────────────────────────────────────────
    "Technology & Computing": {
        "careers": {
            "Software Developer": {
                "description": "Design and build software applications for businesses or consumers.",
                "requirements": [
                    "Bachelor's degree in Computer Science or Software Engineering (UB, BIUST, or Limkokwing)",
                    "Proficiency in at least one programming language (Python, Java, JavaScript)",
                    "Problem-solving and logical thinking skills",
                    "Portfolio of personal or academic projects recommended",
                ],
                "where_to_work": ["BOFINET", "Botswana Innovation Hub", "Orange Botswana", "Mascom", "Private tech startups"],
                "avg_monthly_salary_bwp": "8,000 – 18,000",
            },
            "IT Support Technician": {
                "description": "Maintain computer systems, networks, and provide technical help to users.",
                "requirements": [
                    "Diploma or degree in Information Technology (Botho University, ABM University)",
                    "CompTIA A+ or N+ certification (advantageous)",
                    "Knowledge of Windows/Linux operating systems",
                    "Good communication skills",
                ],
                "where_to_work": ["Government ministries", "Banks (FNBB, Stanbic)", "Hospitals", "Schools"],
                "avg_monthly_salary_bwp": "4,500 – 9,000",
            },
            "Cybersecurity Analyst": {
                "description": "Protect an organisation's computer systems and networks from cyber threats.",
                "requirements": [
                    "Bachelor's degree in IT, Computer Science, or Cybersecurity",
                    "Certifications: CompTIA Security+, CEH, or CISSP (advantageous)",
                    "Knowledge of networking protocols and firewalls",
                    "Analytical mindset",
                ],
                "where_to_work": ["Bank of Botswana", "Botswana Police Service (Cyber Crime Unit)", "Telecom companies", "Private firms"],
                "avg_monthly_salary_bwp": "9,000 – 20,000",
            },
            "Data Analyst": {
                "description": "Collect, process, and analyse data to help organisations make decisions.",
                "requirements": [
                    "Degree in Statistics, Computer Science, Mathematics, or Data Science",
                    "Proficiency in Excel, SQL, Python, or R",
                    "Knowledge of data visualisation tools (Power BI, Tableau)",
                    "Strong analytical and communication skills",
                ],
                "where_to_work": ["Statistics Botswana", "Ministry of Finance", "Banks", "Mining companies"],
                "avg_monthly_salary_bwp": "7,000 – 16,000",
            },
        },
        "courses": {
            "BSc Computer Science": {
                "institution": "University of Botswana (UB) / BIUST",
                "duration": "4 years",
                "entry_requirements": "BGCSE with at least C in Mathematics and English; aggregate 36 or better",
            },
            "BSc Information Technology": {
                "institution": "Botho University / ABM University College",
                "duration": "4 years",
                "entry_requirements": "BGCSE with at least D in Mathematics and English",
            },
            "Diploma in ICT": {
                "institution": "Botswana Accountancy College (BAC) / Botho University",
                "duration": "2 years",
                "entry_requirements": "BGCSE with at least D in Mathematics and English",
            },
            "Certificate in Computer Applications": {
                "institution": "Francistown College of Technical & Vocational Education (FCTE)",
                "duration": "1 year",
                "entry_requirements": "JC (Junior Certificate) or equivalent",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  2. HEALTH & MEDICINE
    # ─────────────────────────────────────────────
    "Health & Medicine": {
        "careers": {
            "Medical Doctor": {
                "description": "Diagnose and treat illnesses; provide patient care across all age groups.",
                "requirements": [
                    "MBBCh degree from University of Botswana School of Medicine (5–6 years)",
                    "Internship at a government hospital (1–2 years)",
                    "Registration with the Botswana Health Professions Council (BHPC)",
                    "Strong BGCSE results in Sciences (Biology, Chemistry, Physics) – aggregate 12 or better",
                ],
                "where_to_work": ["Princess Marina Hospital", "Nyangabgwe Hospital", "Private clinics", "Ministry of Health"],
                "avg_monthly_salary_bwp": "15,000 – 40,000",
            },
            "Registered Nurse": {
                "description": "Provide and coordinate patient care, educate patients about health conditions.",
                "requirements": [
                    "Diploma in Nursing from the Institute of Health Sciences (IHS) – 3 years",
                    "Registration with the Nursing and Midwifery Council of Botswana",
                    "BGCSE with passes in Biology and English",
                    "Compassion and good interpersonal skills",
                ],
                "where_to_work": ["Government hospitals", "Clinics", "NGOs (PEPFAR, ACHAP)", "Private hospitals"],
                "avg_monthly_salary_bwp": "4,000 – 8,500",
            },
            "Pharmacist": {
                "description": "Dispense medications and counsel patients on their safe and effective use.",
                "requirements": [
                    "BPharm degree (4 years) – study locally at UB or abroad",
                    "Internship (1 year) at a licensed pharmacy",
                    "Registration with the Pharmacy Council of Botswana",
                    "Good BGCSE in Chemistry, Biology, and Mathematics",
                ],
                "where_to_work": ["Hospitals", "Retail pharmacies (Clicks, Alpha Pharm)", "Ministry of Health Central Medical Stores"],
                "avg_monthly_salary_bwp": "10,000 – 22,000",
            },
            "Public Health Officer": {
                "description": "Promote health and prevent disease at the community and national level.",
                "requirements": [
                    "Degree in Public Health, Environmental Health, or Nursing",
                    "Good knowledge of Botswana's health policies",
                    "Analytical and communication skills",
                ],
                "where_to_work": ["Ministry of Health", "WHO Botswana", "UNAIDS", "District Health Teams"],
                "avg_monthly_salary_bwp": "6,000 – 14,000",
            },
        },
        "courses": {
            "MBBCh (Medical Degree)": {
                "institution": "University of Botswana Faculty of Medicine",
                "duration": "5–6 years",
                "entry_requirements": "BGCSE aggregate ≤ 12; A grades in Biology, Chemistry, Mathematics/Physics",
            },
            "Diploma in Nursing": {
                "institution": "Institute of Health Sciences (Gaborone, Francistown, Lobatse)",
                "duration": "3 years",
                "entry_requirements": "BGCSE with at least C in Biology and English",
            },
            "BSc Public Health": {
                "institution": "University of Botswana",
                "duration": "4 years",
                "entry_requirements": "BGCSE with C or better in Biology and English",
            },
            "Certificate in Community Health": {
                "institution": "Institute of Health Sciences",
                "duration": "1 year",
                "entry_requirements": "BGCSE or JC with relevant experience",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  3. BUSINESS & FINANCE
    # ─────────────────────────────────────────────
    "Business & Finance": {
        "careers": {
            "Accountant": {
                "description": "Prepare and examine financial records for individuals or organisations.",
                "requirements": [
                    "BCom Accounting or BAcc degree (UB, Botho, BAC)",
                    "ACCA, CIMA, or ICAB qualification (advantageous)",
                    "Proficiency in accounting software (Pastel, QuickBooks, SAP)",
                    "BGCSE with Mathematics and English passes",
                ],
                "where_to_work": ["KPMG Botswana", "Deloitte Botswana", "Government (PPADB)", "Banks", "Mining companies"],
                "avg_monthly_salary_bwp": "6,000 – 18,000",
            },
            "Bank Teller / Banking Officer": {
                "description": "Handle financial transactions and provide customer service at a bank.",
                "requirements": [
                    "Diploma or degree in Finance, Banking, or Business Administration",
                    "Good numeracy and communication skills",
                    "Trustworthiness and attention to detail",
                ],
                "where_to_work": ["First National Bank Botswana (FNBB)", "Stanbic Bank", "Barclays (Absa)", "BBS", "Bank of Botswana"],
                "avg_monthly_salary_bwp": "3,500 – 7,000",
            },
            "Entrepreneur / Small Business Owner": {
                "description": "Start and manage your own business in any sector.",
                "requirements": [
                    "Business plan and market research",
                    "Registration with CIPA (Companies and Intellectual Property Authority)",
                    "Access to funding: LEA (Local Enterprise Authority), CEDA, Youth Development Fund",
                    "Business management knowledge (formal training helpful but not mandatory)",
                ],
                "where_to_work": ["Own business / Self-employed"],
                "avg_monthly_salary_bwp": "Varies widely",
            },
            "Financial Analyst": {
                "description": "Evaluate investment opportunities and advise on financial decisions.",
                "requirements": [
                    "Degree in Finance, Economics, or Accounting",
                    "CFA (Chartered Financial Analyst) certification is a major advantage",
                    "Strong Excel and financial modelling skills",
                    "Analytical mindset",
                ],
                "where_to_work": ["Botswana Stock Exchange", "Investment firms", "Pension funds (BPOPF)", "Insurance companies"],
                "avg_monthly_salary_bwp": "9,000 – 22,000",
            },
        },
        "courses": {
            "BCom Accounting": {
                "institution": "University of Botswana / Botho University",
                "duration": "4 years",
                "entry_requirements": "BGCSE with at least C in Mathematics and English",
            },
            "ACCA (Association of Chartered Certified Accountants)": {
                "institution": "Botswana Accountancy College (BAC) / Private providers",
                "duration": "2–4 years (part-time possible)",
                "entry_requirements": "Minimum 2 BGCSE passes including Mathematics and English; or relevant diploma",
            },
            "Diploma in Business Administration": {
                "institution": "Botho University / Gaborone University College",
                "duration": "2 years",
                "entry_requirements": "BGCSE with at least D in English and Mathematics",
            },
            "Certificate in Entrepreneurship": {
                "institution": "Local Enterprise Authority (LEA) Training Centres",
                "duration": "Short course (weeks to months)",
                "entry_requirements": "Open to adults with a business idea; JC recommended",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  4. ENGINEERING & CONSTRUCTION
    # ─────────────────────────────────────────────
    "Engineering & Construction": {
        "careers": {
            "Civil Engineer": {
                "description": "Design and oversee construction of roads, bridges, buildings, and water systems.",
                "requirements": [
                    "BEng Civil Engineering (BIUST – 4 years)",
                    "Registration with the Engineers Registration Board (ERB) of Botswana",
                    "Strong BGCSE Mathematics and Physical Science (at least B grade)",
                    "AutoCAD and project management skills",
                ],
                "where_to_work": ["Department of Roads", "Water Utilities Corporation (WUC)", "Private construction firms", "Debswana"],
                "avg_monthly_salary_bwp": "10,000 – 25,000",
            },
            "Electrical Engineer": {
                "description": "Design and maintain electrical systems, power grids, and electronics.",
                "requirements": [
                    "BEng Electrical Engineering (BIUST)",
                    "Registration with the ERB",
                    "Knowledge of CAD tools and electrical codes",
                    "BGCSE with strong Mathematics and Physics",
                ],
                "where_to_work": ["Botswana Power Corporation (BPC)", "Mining companies", "Telecoms", "Construction firms"],
                "avg_monthly_salary_bwp": "11,000 – 28,000",
            },
            "Artisan / Electrician / Plumber": {
                "description": "Install, maintain, and repair electrical wiring, plumbing, or mechanical systems.",
                "requirements": [
                    "Trade certificate from a Botswana Technical College (BTC) or Apprenticeship",
                    "Registration with relevant trade board",
                    "Physical fitness and practical skills",
                    "JC (Junior Certificate) minimum entry for vocational training",
                ],
                "where_to_work": ["Construction sites", "Mines", "Government", "Self-employment"],
                "avg_monthly_salary_bwp": "3,000 – 8,000",
            },
            "Quantity Surveyor": {
                "description": "Manage and control costs within construction projects.",
                "requirements": [
                    "BSc Quantity Surveying or Construction Management",
                    "Membership with the Botswana Institute of Quantity Surveyors (BIQS)",
                    "Good Mathematics and analytical skills",
                ],
                "where_to_work": ["Ministry of Infrastructure", "Private construction firms", "Real estate developers"],
                "avg_monthly_salary_bwp": "8,000 – 18,000",
            },
        },
        "courses": {
            "BEng Civil / Electrical / Mechanical Engineering": {
                "institution": "Botswana International University of Science & Technology (BIUST)",
                "duration": "4 years",
                "entry_requirements": "BGCSE with at least B in Mathematics and Physical Science; aggregate ≤ 20",
            },
            "Diploma in Building & Civil Engineering": {
                "institution": "Botswana Technical Colleges (BTC) – Gaborone, Francistown",
                "duration": "3 years",
                "entry_requirements": "BGCSE with C in Mathematics and English",
            },
            "Certificate in Electrical Installation (Trade)": {
                "institution": "Botswana Technical Colleges / Apprenticeship schemes",
                "duration": "2–3 years",
                "entry_requirements": "JC with passes in Mathematics and Science",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  5. EDUCATION & TEACHING
    # ─────────────────────────────────────────────
    "Education & Teaching": {
        "careers": {
            "Primary School Teacher": {
                "description": "Educate children aged 6–13 in core subjects.",
                "requirements": [
                    "Diploma in Primary Education (DPE) from Tonota or Tlokweng College of Education – 3 years",
                    "BGCSE with at least C in English and any 4 other subjects",
                    "Patience, communication, and classroom management skills",
                    "Registration with Teaching Service Management (TSM)",
                ],
                "where_to_work": ["Government primary schools", "Private schools"],
                "avg_monthly_salary_bwp": "3,500 – 6,500",
            },
            "Secondary School Teacher": {
                "description": "Teach specialised subjects to students in Forms 1–5.",
                "requirements": [
                    "Bachelor of Education (BEd) in a relevant subject (UB – 4 years)",
                    "BGCSE with strong results in chosen teaching subject",
                    "Registration with TSM",
                ],
                "where_to_work": ["Government secondary schools", "Private schools", "Tutoring centres"],
                "avg_monthly_salary_bwp": "5,000 – 10,000",
            },
            "Lecturer / University Educator": {
                "description": "Teach and conduct research at tertiary institutions.",
                "requirements": [
                    "Master's degree minimum; PhD preferred for senior positions",
                    "Research and publication experience",
                    "Subject expertise",
                ],
                "where_to_work": ["University of Botswana", "BIUST", "Botho University", "BAC"],
                "avg_monthly_salary_bwp": "10,000 – 25,000",
            },
            "Special Needs Educator": {
                "description": "Support and teach learners with disabilities or learning differences.",
                "requirements": [
                    "Diploma or Degree in Special Needs Education",
                    "Patience, creativity, and strong interpersonal skills",
                    "Registration with TSM",
                ],
                "where_to_work": ["Itirele School for the Deaf", "Government inclusive schools", "NGOs"],
                "avg_monthly_salary_bwp": "4,000 – 8,000",
            },
        },
        "courses": {
            "Diploma in Primary Education (DPE)": {
                "institution": "Tonota College of Education / Tlokweng College of Education",
                "duration": "3 years",
                "entry_requirements": "BGCSE with at least C in English and 4 other passes",
            },
            "Bachelor of Education (BEd)": {
                "institution": "University of Botswana",
                "duration": "4 years",
                "entry_requirements": "BGCSE aggregate ≤ 36; C or better in chosen teaching subjects",
            },
            "Postgraduate Diploma in Education (PGDE)": {
                "institution": "University of Botswana",
                "duration": "1 year",
                "entry_requirements": "First degree in any subject",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  6. LAW & GOVERNMENT
    # ─────────────────────────────────────────────
    "Law & Government": {
        "careers": {
            "Lawyer / Advocate": {
                "description": "Represent clients and provide legal advice in civil and criminal matters.",
                "requirements": [
                    "LLB degree from University of Botswana (4 years)",
                    "1-year practical legal training (PLT) / pupillage",
                    "Admission to the Botswana Law Society",
                    "BGCSE with strong English and History results",
                ],
                "where_to_work": ["Private law firms", "Attorney General's Chambers", "Directorate on Corruption and Economic Crime (DCEC)", "Corporations"],
                "avg_monthly_salary_bwp": "10,000 – 35,000+",
            },
            "Police Officer": {
                "description": "Maintain law and order, investigate crimes, and protect citizens.",
                "requirements": [
                    "BGCSE with at least 5 passes including English",
                    "Physical fitness test and medical examination",
                    "Botswana Police Service (BPS) training college – 9 months",
                    "Botswana citizenship",
                ],
                "where_to_work": ["Botswana Police Service stations nationwide"],
                "avg_monthly_salary_bwp": "3,200 – 7,000",
            },
            "Civil Servant / Government Officer": {
                "description": "Work in government ministries and departments to implement public policy.",
                "requirements": [
                    "Diploma or degree relevant to the ministry (varies by post)",
                    "Botswana citizenship",
                    "Application through the Directorate of Public Service Management (DPSM)",
                ],
                "where_to_work": ["All government ministries and departments"],
                "avg_monthly_salary_bwp": "4,000 – 15,000 (depends on grade)",
            },
            "Human Rights Officer": {
                "description": "Advocate for and monitor human rights across communities and institutions.",
                "requirements": [
                    "Degree in Law, Social Sciences, or Human Rights",
                    "Knowledge of Botswana's Constitution and international human rights instruments",
                    "Strong advocacy and communication skills",
                ],
                "where_to_work": ["Botswana Human Rights Commission (BHRC)", "NGOs", "UN agencies"],
                "avg_monthly_salary_bwp": "6,000 – 14,000",
            },
        },
        "courses": {
            "LLB (Bachelor of Laws)": {
                "institution": "University of Botswana Faculty of Law",
                "duration": "4 years",
                "entry_requirements": "BGCSE aggregate ≤ 30; at least C in English; History or Social Studies an advantage",
            },
            "Diploma in Public Administration": {
                "institution": "Botho University / Institute of Development Management (IDM)",
                "duration": "2 years",
                "entry_requirements": "BGCSE with at least D in English",
            },
            "Certificate in Paralegal Studies": {
                "institution": "Botswana Law Society / Private colleges",
                "duration": "1 year",
                "entry_requirements": "BGCSE with English pass",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  7. AGRICULTURE & ENVIRONMENT
    # ─────────────────────────────────────────────
    "Agriculture & Environment": {
        "careers": {
            "Agricultural Officer / Extension Officer": {
                "description": "Advise farmers on best practices, crop production, and livestock management.",
                "requirements": [
                    "Diploma or degree in Agriculture (Botswana College of Agriculture / UB)",
                    "Knowledge of Botswana's soils and climate",
                    "Good communication skills for community outreach",
                ],
                "where_to_work": ["Ministry of Agriculture", "FAO Botswana", "BAMB", "Private farms"],
                "avg_monthly_salary_bwp": "4,500 – 9,000",
            },
            "Veterinarian": {
                "description": "Diagnose and treat animals; crucial for Botswana's large livestock sector.",
                "requirements": [
                    "BVSc degree (study abroad or at local colleges for pre-vet; full degree often done in South Africa or Zimbabwe)",
                    "Registration with the Botswana Veterinary Board",
                    "Strong Biology and Chemistry background",
                ],
                "where_to_work": ["Department of Animal Health (DAH)", "Private vet clinics", "BAMB", "Farms"],
                "avg_monthly_salary_bwp": "9,000 – 20,000",
            },
            "Environmental Officer": {
                "description": "Monitor and protect Botswana's natural environment from pollution and degradation.",
                "requirements": [
                    "Degree in Environmental Science, Ecology, or Natural Resource Management",
                    "Knowledge of environmental laws (Environmental Assessment Act)",
                    "Report-writing and fieldwork skills",
                ],
                "where_to_work": ["Department of Environmental Affairs (DEA)", "Mining companies (EIA roles)", "NGOs"],
                "avg_monthly_salary_bwp": "5,500 – 12,000",
            },
            "Wildlife / Parks Ranger": {
                "description": "Protect wildlife and manage national parks and game reserves.",
                "requirements": [
                    "Certificate or Diploma in Wildlife Management (Botswana Wildlife Training Institute – Maun)",
                    "Physical fitness",
                    "Passion for conservation",
                ],
                "where_to_work": ["Department of Wildlife and National Parks (DWNP)", "Private safari companies", "Community Trusts"],
                "avg_monthly_salary_bwp": "3,000 – 7,000",
            },
        },
        "courses": {
            "BSc Agriculture": {
                "institution": "Botswana College of Agriculture (BCA) / University of Botswana",
                "duration": "4 years",
                "entry_requirements": "BGCSE with C in Biology, Agriculture or Science, and English",
            },
            "Diploma in Wildlife Management": {
                "institution": "Botswana Wildlife Training Institute (BWTI), Maun",
                "duration": "2 years",
                "entry_requirements": "BGCSE with D or better in Biology and English",
            },
            "Certificate in Animal Health & Production": {
                "institution": "Botswana College of Agriculture",
                "duration": "1–2 years",
                "entry_requirements": "JC or BGCSE",
            },
            "BSc Environmental Science": {
                "institution": "University of Botswana",
                "duration": "4 years",
                "entry_requirements": "BGCSE with C in Biology and any science subject",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  8. ARTS, DESIGN & MEDIA
    # ─────────────────────────────────────────────
    "Arts, Design & Media": {
        "careers": {
            "Graphic Designer": {
                "description": "Create visual content for marketing, media, and communication.",
                "requirements": [
                    "Diploma or degree in Graphic Design / Visual Communication (Limkokwing University)",
                    "Proficiency in Adobe Photoshop, Illustrator, and InDesign",
                    "Strong portfolio of design work",
                    "Creativity and attention to detail",
                ],
                "where_to_work": ["Advertising agencies", "Media companies", "Government (DSTV Botswana)", "Freelance"],
                "avg_monthly_salary_bwp": "4,000 – 10,000",
            },
            "Journalist / Media Practitioner": {
                "description": "Gather, verify, and report news stories for print, broadcast, or online media.",
                "requirements": [
                    "Degree or Diploma in Journalism / Media Studies (UB, Limkokwing, BUAN)",
                    "Strong writing and research skills",
                    "Knowledge of media ethics and Botswana's media landscape",
                ],
                "where_to_work": ["Botswana Television (BTV)", "Daily News", "Weekend Post", "Sunday Standard", "Radio Botswana"],
                "avg_monthly_salary_bwp": "4,000 – 10,000",
            },
            "Fashion Designer": {
                "description": "Design clothing and accessories, often integrating African aesthetics.",
                "requirements": [
                    "Diploma in Fashion Design (Limkokwing or private colleges)",
                    "Sewing, pattern-making, and design skills",
                    "Business skills for self-employment",
                ],
                "where_to_work": ["Self-employed / Studio", "Retail clothing stores", "Theatre / Events"],
                "avg_monthly_salary_bwp": "2,500 – 8,000+",
            },
            "Musician / Performing Artist": {
                "description": "Perform, compose, or produce music or stage performances.",
                "requirements": [
                    "Formal music training (UB Music Department) or self-taught",
                    "Stage performance experience",
                    "Music production skills (advantageous)",
                    "Networking within the Botswana music industry",
                ],
                "where_to_work": ["Self-employed", "Events industry", "BTV and Radio", "Tourism (cultural performances)"],
                "avg_monthly_salary_bwp": "Varies widely",
            },
        },
        "courses": {
            "BA Fine Art / Design": {
                "institution": "University of Botswana (Department of Art & Design)",
                "duration": "4 years",
                "entry_requirements": "BGCSE with C in Art and English; portfolio interview",
            },
            "Diploma in Graphic Design": {
                "institution": "Limkokwing University of Creative Technology, Gaborone",
                "duration": "3 years",
                "entry_requirements": "BGCSE with at least 5 passes; portfolio an advantage",
            },
            "Diploma in Journalism & Media": {
                "institution": "University of Botswana / Limkokwing",
                "duration": "2–3 years",
                "entry_requirements": "BGCSE with C in English",
            },
            "Certificate in Fashion Design": {
                "institution": "Limkokwing University / Private fashion schools",
                "duration": "1–2 years",
                "entry_requirements": "BGCSE or JC",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  9. TOURISM & HOSPITALITY
    # ─────────────────────────────────────────────
    "Tourism & Hospitality": {
        "careers": {
            "Safari Guide / Tour Guide": {
                "description": "Lead tourists on safari or cultural tours, sharing knowledge of wildlife and culture.",
                "requirements": [
                    "Certificate or Diploma in Tourism / Wildlife Guiding (Hospitality & Tourism Training Institute – HTTI)",
                    "In-depth knowledge of Botswana's ecosystems and wildlife",
                    "First Aid certification",
                    "Good English communication; additional languages an advantage",
                ],
                "where_to_work": ["Okavango Delta lodges", "Chobe National Park operators", "Tour companies", "DWNP"],
                "avg_monthly_salary_bwp": "4,000 – 12,000 (+ tips)",
            },
            "Hotel Manager": {
                "description": "Oversee all operations of a hotel or lodge.",
                "requirements": [
                    "Degree or Diploma in Hospitality Management (HTTI or abroad)",
                    "Experience in front office, F&B, and housekeeping operations",
                    "Leadership and customer service skills",
                ],
                "where_to_work": ["Avani Gaborone", "Cresta Hotels", "Camps in Botswana (Wilderness Safaris, &Beyond)"],
                "avg_monthly_salary_bwp": "8,000 – 20,000",
            },
            "Chef / Culinary Artist": {
                "description": "Prepare food in restaurants, hotels, or safari lodges.",
                "requirements": [
                    "Diploma in Culinary Arts (HTTI – 2 years)",
                    "Apprenticeship or on-the-job training",
                    "Creativity and food safety knowledge",
                ],
                "where_to_work": ["Hotels", "Restaurants", "Safari camps", "Private catering"],
                "avg_monthly_salary_bwp": "3,500 – 9,000",
            },
        },
        "courses": {
            "Diploma in Tourism & Hospitality Management": {
                "institution": "Hospitality & Tourism Training Institute (HTTI), Gaborone",
                "duration": "2–3 years",
                "entry_requirements": "BGCSE with at least D in English and any 4 subjects",
            },
            "Certificate in Food & Beverage": {
                "institution": "HTTI / Botswana Technical Colleges",
                "duration": "1 year",
                "entry_requirements": "BGCSE or JC",
            },
            "Certificate in Professional Cookery": {
                "institution": "HTTI",
                "duration": "1–2 years",
                "entry_requirements": "JC or BGCSE",
            },
        },
    },
 
    # ─────────────────────────────────────────────
    #  10. MINING & GEOLOGY
    # ─────────────────────────────────────────────
    "Mining & Geology": {
        "careers": {
            "Mining Engineer": {
                "description": "Plan and oversee extraction of minerals safely and efficiently.",
                "requirements": [
                    "BEng Mining Engineering (BIUST – 4 years)",
                    "Registration with the Engineers Registration Board",
                    "Strong Mathematics and Physical Science background",
                    "Knowledge of occupational health and safety regulations",
                ],
                "where_to_work": ["Debswana Diamond Company", "BCL Mine", "Khoemacau Copper Mine", "Sandvik (contractor)"],
                "avg_monthly_salary_bwp": "15,000 – 40,000",
            },
            "Geologist": {
                "description": "Study the earth's structure to locate and assess mineral deposits.",
                "requirements": [
                    "BSc Geology or Earth Sciences (BIUST or UB)",
                    "Fieldwork skills and knowledge of GIS software",
                    "Strong Chemistry and Physics background",
                ],
                "where_to_work": ["Department of Geological Survey (DGS)", "Debswana", "Exploration companies"],
                "avg_monthly_salary_bwp": "9,000 – 22,000",
            },
            "Mine Safety Officer": {
                "description": "Ensure all mining operations comply with safety standards.",
                "requirements": [
                    "Degree or Diploma in Occupational Health & Safety or Mining Engineering",
                    "Knowledge of Mines, Quarries, Works & Machinery Act of Botswana",
                    "NEBOSH certificate (advantageous)",
                ],
                "where_to_work": ["All mining operations in Botswana"],
                "avg_monthly_salary_bwp": "8,000 – 18,000",
            },
        },
        "courses": {
            "BEng Mining Engineering": {
                "institution": "BIUST, Palapye",
                "duration": "4 years",
                "entry_requirements": "BGCSE with at least B in Mathematics and Physical Science; aggregate ≤ 20",
            },
            "BSc Geology": {
                "institution": "BIUST / University of Botswana",
                "duration": "4 years",
                "entry_requirements": "BGCSE with C or better in Chemistry, Physics/Physical Science, and Mathematics",
            },
            "Certificate in Mine Safety & Health": {
                "institution": "Botswana Technical Colleges / Industry short courses",
                "duration": "Varies (weeks – months)",
                "entry_requirements": "JC or BGCSE; relevant work experience helpful",
            },
        },
    },
}
 

print(data)