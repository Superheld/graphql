# import sys
# print("Python Path:", sys.path)

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from schemas.kategorienSchema import schema

app = FastAPI()

@app.on_event("startup")
async def startup():
    from models import db
    db.bind(provider='sqlite', filename=':memory:')
    db.generate_mapping(create_tables=True)

@app.post("/graphql")
async def graphql(request: Request):
    data = await request.json()
    result = schema.execute(
        data.get('query'),
        context_value=request,
        variable_values=data.get('variables'),
        middleware=None
    )

    if result.errors:
        errors = [{"message": str(error)} for error in result.errors]
        return JSONResponse(content={"errors": errors}, status_code=400)
    else:
        return JSONResponse(content={"data": result.data})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)