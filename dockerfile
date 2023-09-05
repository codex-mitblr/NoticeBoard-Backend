FROM python
RUN apt-get update -y && apt-get install -y curl python3 
COPY . /root/
WORKDIR /root/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
EXPOSE 5000