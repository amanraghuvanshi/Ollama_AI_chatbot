# API Documentation

## Overview

The API serves as the communication layer between the frontend (Streamlit/Gradio) and the backend. It enables interaction with the `deepseek-r1:1.5b` model via endpoints exposed by the backend.

---

## Base URL

Since this is a locally hosted project, the base URL for API endpoints is:

```
http://localhost:8000
```

---

## Endpoints

### 1. **POST /query**

* **Description:**
  Handles user queries and sends them to the `deepseek-r1:1.5b` model for processing.
* **Request:**

  * **Headers:**

    * `Content-Type: application/json`
  * **Body:**

    ```json
    {
      "prompt": "Your query here"
    }
    ```
* **Response:**

  * **Headers:**

    * `Content-Type: application/json`
  * **Body:**

    ```json
    {
      "response": "Response from the AI model"
    }
    ```
* **Example:**

  * **Request:**

    ```bash
    curl -X POST http://localhost:8000/query \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Explain machine learning"}'
    ```
  * **Response:**

    ```json
    {
      "response": "Machine learning is a subset of artificial intelligence..."
    }
    ```

---

### 2. **GET /status**

* **Description:**
  Checks the status of the backend and model.
* **Request:**

  * **Headers:** None
  * **Body:** None
* **Response:**

  * **Headers:**

    * `Content-Type: application/json`
  * **Body:**

    ```json
    {
      "status": "running",
      "model": "deepseek-r1:1.5b"
    }
    ```
* **Example:**

  * **Request:**

    ```bash
    curl http://localhost:8000/status
    ```
  * **Response:**

    ```json
    {
      "status": "running",
      "model": "deepseek-r1:1.5b"
    }
    ```

---

### 3. **POST /preprocess** (Optional)

* **Description:**
  Preprocesses a user query before sending it to the model.
* **Request:**

  * **Headers:**

    * `Content-Type: application/json`
  * **Body:**

    ```json
    {
      "input_text": "Raw user query here"
    }
    ```
* **Response:**

  * **Headers:**

    * `Content-Type: application/json`
  * **Body:**

    ```json
    {
      "preprocessed_text": "Processed query ready for the model"
    }
    ```
* **Example:**

  * **Request:**

    ```bash
    curl -X POST http://localhost:8000/preprocess \
      -H "Content-Type: application/json" \
      -d '{"input_text": "What is AI?"}'
    ```
  * **Response:**

    ```json
    {
      "preprocessed_text": "Define artificial intelligence."
    }
    ```

---

## Error Handling

* **Response Format:**
  All errors follow this structure:

  ```json
  {
    "error": "Error message here"
  }
  ```

### Common Errors

1. **400 Bad Request**

   * Occurs when the request body is malformed or missing required fields.
   * Example:

     ```json
     {
       "error": "Invalid request payload"
     }
     ```

2. **500 Internal Server Error**

   * Occurs when there is an issue processing the request.
   * Example:

     ```json
     {
       "error": "Internal server error. Please try again later."
     }
     ```

---

## Authentication

No authentication is required for this locally hosted application.

---

## Future Enhancements

* Add user authentication and session management.
* Implement caching for repeated queries to improve performance.
* Expand API to support multi-model setups.
