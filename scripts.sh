
# Activate virtual environment
source .venv/Scripts/activate
which python
# Run tests
pytest tests/
status=$?
exit $status