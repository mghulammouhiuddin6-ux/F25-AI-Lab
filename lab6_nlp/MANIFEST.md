# Submission manifest

## Included

- Project documentation: `README.md`, `Lab6_Report.docx`
- Dataset and evaluation inputs: `corpus.json`, `queries.json`
- Dependencies and Git ignore rules: `requirements.txt`, `.gitignore`
- Task, helper, guided example, and scenario source code: all `.py` files in this folder
- Existing retrieval results: `retrieval_log.csv` (TF-IDF run only)

The individual saved console transcripts were omitted because they duplicate script output; the report and retrieval CSV retain the relevant recorded results.

## Verification and limitations

- Python syntax compilation, `task1_tokens.py`, `task2_chunks.py`, `create_dataset.py`, and `task2_analysis.py` ran successfully in the available environment. The Urdu token example is escaped when a legacy Windows terminal cannot display it.
- The environment lacks `numpy`, `scikit-learn`, and `sentence-transformers`; FAQ and retrieval scripts therefore could not be independently run here. Embedding evaluation remains pending and must be run with the dependencies and model available. No embedding results are claimed.
- The included report and CSV came from the uploaded archive. Their recorded TF-IDF measurements were not regenerated in this environment.
- The manual itself was not present in the cached conversation or uploaded ZIP, so this package was checked against the project README and report rather than an independent manual checklist.
- No terminal screenshots, GitHub repository URL, or commit ID are included. Create those only if the course submission instructions require them.
