# Bellhaven CRM Sync

## Overview

This project synchronizes Bellhaven Senior Living communities from the public website with CRM records.

The solution includes:

1. Website scraper
2. Matching engine
3. Review queue
4. CRM findings workflow

--------------------------------------------------

## Project Structure

bellhaven-sync/

accounts.json

crm_findings.json

matcher.py

ownership_check.py

duplicate_check.py

summary.txt

data/
    website_locations.json

scraper/
    scrape_bellhaven.py

review_app/
    app.py

--------------------------------------------------

## Website Scraper

Run:

python scraper/scrape_bellhaven.py

This extracts all Bellhaven communities from the website and stores them in:

data/website_locations.json

--------------------------------------------------

## Matching Logic

Run:

python matcher.py

This compares website communities against CRM accounts and identifies:

- Missing accounts
- Duplicate accounts
- Name mismatches
- Ownership change scenarios
- Potential obsolete CRM records

--------------------------------------------------

## Review Application

Run:

cd review_app

python app.py

Open:

http://127.0.0.1:5000

The review application displays findings and proposed CRM changes for approval.

--------------------------------------------------

## Findings

Duplicate Account

Bellhaven of Owosso

Keep:
001EGU7BMJ942ZTRE6

Deactivate:
001QU150PM4Z15UA71

--------------------------------------------------

CHOW Required

Bellhaven of Marietta

Revenue: 51250

Outstanding AR: 3800

Bellhaven of Tiffin

Revenue: 84000

Outstanding AR: 12400

--------------------------------------------------

Direct Re-parent Candidate

Bellhaven Crossings of Lima

Revenue: 47000

Outstanding AR: 0

--------------------------------------------------

Name Corrections

Bellhaven at Sycamore Ridge

Bellhaven Healthcare Centre of Ashland

Bellhaven Rehabilitation & Nursing of Grove City

The Arbors at Bellhaven - Dayton

--------------------------------------------------

## Daily Schedule

Example Cron Schedule

0 6 * * * python scraper/scrape_bellhaven.py

The pipeline is designed to run daily and generate findings for review before CRM updates are applied.

--------------------------------------------------

## Current Status

Completed:
- Website scraper
- CRM extraction
- Matching logic
- Duplicate detection
- CHOW detection
- Review queue

Pending:
- CRM write-back actions
- Approval and rejection workflow persistence
- Automated CRM updates