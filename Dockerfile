FROM python:3

#running from personal directory on PC. Hopefully this isn't an issue? 
WORKDIR "C:/School/Year 3/Semester 2/Software Tools for Startups"

COPY unittest.py .

CMD ["python -m", "unittest.py test.py"]
