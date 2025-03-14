FROM python:3.12.8-slim

# Set working directory
WORKDIR /app

# Copy only essential files
COPY req.txt .
COPY .env *.py *.xlsx ./
COPY __app__ __app__
COPY __data__ __data__
COPY __state_user__ __state_user__

# DEBUG
RUN ["ls", "-la"]

# Install dependencies
RUN pip install --no-cache-dir -r req.txt

# Command to run the application
CMD ["python", "bot.py"]