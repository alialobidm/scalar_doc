from fastapi import FastAPI, responses

from scalar_doc import (
    ScalarColorSchema,
    ScalarConfiguration,
    ScalarDoc,
    ScalarHeader,
    ScalarTheme,
)

DESCRIPTION = """
# Welcome!

## Sidebar SubSection

### Title

Start using Scalar on your `FastAPI`, and all other `Python` APIs!
"""

app = FastAPI(
    title="ScalarDoc on Python",
    description=DESCRIPTION,
    docs_url=None,
    redoc_url=None,
)
docs = ScalarDoc.from_spec(spec=app.openapi_url, mode="url")

docs.set_configuration(ScalarConfiguration(with_default_fonts=False))

docs.set_header(
    ScalarHeader(
        logo_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        logo_url_dark="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        links={"Python.org": "https://www.python.org"},
    )
)
docs.set_theme(
    ScalarTheme(
        favicon_url="https://www.python.org/static/apple-touch-icon-144x144-precomposed.png",
        color_scheme_light=ScalarColorSchema(
            color_1="#0c2344",
            color_2="#4B6EAF",
            color_3="#FFD43B",
            background_1="#ffffff",
            background_2="#f5f5f5",
            background_3="#e0e0e0",
            color_accent="#306998",
            background_accent="#dbe9f7",
            link_color="#1c6cc7",
            code="#2f4f4f",
        ),
        color_scheme_dark=ScalarColorSchema(
            color_1="#ffffff",
            color_2="#aaaaaa",
            color_3="#FFD43B",
            background_1="#0a0a0a",
            background_2="#111111",
            background_3="#1a1a1a",
            color_accent="#FFD43B",
            background_accent="#ffd43b33",
            link_color="#FFD43B",
            code="#f0f0f0",
        ),
    )
)


@app.post("/foo")
def post_foo(a: str):
    return a + " - ok"


@app.get("/docs", include_in_schema=False)
def get_docs():
    docs_html = docs.to_html()
    return responses.HTMLResponse(docs_html)
