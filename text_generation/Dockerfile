FROM python:3

ADD text_gen_app_concept.py /

RUN pip install torch
RUN pip install transformers

CMD [ "python", "./text_gen_app_concept.py" ]