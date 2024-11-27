from fastapi import FastAPI
from handler.autenticazione import router as autenticazione_router
from handler.impianti import router as impianti_router
from handler.macchinari import router as macchinari_router

app = FastAPI(  

    openapi_url="/documentation/json",

    docs_url="/documentation",

    redoc_url=None

)
app.include_router(autenticazione_router)
app.include_router(impianti_router)
app.include_router(macchinari_router)