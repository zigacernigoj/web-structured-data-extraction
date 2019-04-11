# web-structured-data-extraction

## About
This project contains three different approaches for the structured data extraction from the web:

- Using regular expressions
- Using XPath
- RoadRunner-like implementation

The whole report will be available in file report.pdf


## Structure

3 types of sites, 3 approaches:
- 3 different **regex** algorithms (3 site types)
- 3 different **xpath** algorithms (3 site types)
- 1 algorithm for **roadrunner** - same for all site types

|                  | regex (re) | xpath (xp) | roadrunner (rr)  |
|---               |---         |---         |---               |
| rtvslo (rs)      | rs-re.py   | rs-xp.py   | rr.py (just one) |
| overstock (os)   | os-re.py   | os-xp.py   | rr.py (just one) |
| free choice (fc) | fc-re.py   | fc-xp.py   | rr.py (just one) |

**How to arrange them into folders?**

a) 3 folders for **approaches** and in them files for **site types**:
(votes for this: Ziga)
- root
  - regex
    - rs-re.py
    - os-re.py
    - fc-re.py
  - xpath
    - rs-xp.py
    - os-xp.py
    - fc-xp.py
  - roadrunner
    - rr.py
 
 b) 3 folders for **site types** and in them files for **approaches**:
- root
  - rtvslo
    - rs-re.py
    - rs-xp.py
  - overstock
    - os-re.py
    - os-xp.py
  - free choice
    - fc-re.py
    - fc-xp.py
  - *additional folder for roadrunner, since it's one alg. for all three* roadrunner
    - rr.py
    
    
 
