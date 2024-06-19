from fastapi import FastAPI, Request, Response, status
import pickle

app = FastAPI()
model_path = 'classifier.pkl'

@app.get("/")
def root():
    return {"message": "Your API is UP!"}

# check-model
@app.get("/check-model")
def check_model(response: Response):
    try:
        with open(model_path, 'rb') as model:
            model = pickle.load(model)
            result = {'status': 'ok', 'message': 'model is ready to use'}
            return result
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'error', 'message': 'model is not found', 'detail_error': str(e)}
    