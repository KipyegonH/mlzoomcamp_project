FROM python:3.8-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy Pipfile and Pipfile.lock from environment_project to /app
COPY Pipfile Pipfile.lock /app/

# 4. Install dependencies using Pipenv
RUN pip install pipenv && pipenv install --deploy --system

# 5. Copy the rest of the project files from environment_project to /app
COPY environment_project /app/
EXPOSE 9696

# 7. Command to run the prediction script
CMD ["pipenv", "run", "python", "predict.py"]
