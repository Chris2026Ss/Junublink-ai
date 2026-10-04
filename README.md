# JunubLink AI

JunubLink AI is a Juba-first information and opportunity portal for South Sudanese youth, students, traders, and communities. The project helps users find local jobs, scholarships, training opportunities, market reference prices, and scam-risk checks in a simple, mobile-friendly interface.

## Project overview

This repo currently contains a Streamlit prototype built in Python. It is designed as a lightweight web app that can run locally and be expanded with more verified community data and AI-powered recommendations.

### Included features
- Jobs in Juba
- Scholarships and training opportunities
- Market prices for common local goods
- Scam check tool for suspicious offers
- FAQ and contact section

## Tech stack
- Python
- Streamlit
- Pandas

## Repository structure
- `app.py` — main Streamlit application
- `Junublink.py` — compatibility wrapper entry point
- `requirements.txt` — project dependencies
- `README.md` — project documentation
- `junublink_code.pdf` — supporting project document
- `JunubLink_requirements.pdf` — supporting requirements/design document
- `JunubLink_README.pdf` — supporting documentation

## Run locally

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
streamlit run app.py
```

## Project status

This is an early-stage prototype. The app is intended to help users access useful opportunities and local information, but listings and prices should still be verified before real-world use.

## Intended use

The app is built for:
- South Sudanese youth and students
- Job seekers and interns
- Traders and small business owners
- Community organizations
- Families and users needing locally relevant information

## Notes

- The app is intentionally simple and low-friction for local use.
- It does not currently connect to live external APIs or a production WhatsApp backend.
- Any future WhatsApp or AI integration should be added deliberately and with proper validation and security review.

## Founder

Kerwar Duop Yoam
South Sudan

## License

This project is currently under development. Licensing terms will be added as the project matures.
