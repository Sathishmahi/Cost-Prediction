echo "ENV CREATED START"
conda create -p venv/ python=3.10 -y
source activate venv/
echo "REQUIRE LIB CREATED STARTED"
pip install -r requirements.txt
echo "END" 