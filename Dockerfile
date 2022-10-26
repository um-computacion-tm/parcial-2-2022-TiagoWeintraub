FROM python

RUN https://github.com/um-computacion-tm/parcial-2-2022-TiagoWeintraub.git

WORKDIR /parcial-2-2022-TiagoWeintraub

COPY . .

CMD ["python", "test.py"]