# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse


# app = FastAPI(
#     title="Vercel + FastAPI",
#     description="Vercel + FastAPI",
#     version="1.0.0",
# )


# @app.get("/api/data")
# def get_sample_data():
#     return {
#         "data": [
#             {"id": 1, "name": "Sample Item 1", "value": 100},
#             {"id": 2, "name": "Sample Item 2", "value": 200},
#             {"id": 3, "name": "Sample Item 3", "value": 300}
#         ],
#         "total": 3,
#         "timestamp": "2024-01-01T00:00:00Z"
#     }


# @app.get("/api/items/{item_id}")
# def get_item(item_id: int):
#     return {
#         "item": {
#             "id": item_id,
#             "name": "Sample Item " + str(item_id),
#             "value": item_id * 100
#         },
#         "timestamp": "2024-01-01T00:00:00Z"
#     }


# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Vercel + FastAPI</title>
#         <link rel="icon" type="image/x-icon" href="/favicon.ico">
#         <style>
#             * {
#                 margin: 0;
#                 padding: 0;
#                 box-sizing: border-box;
#             }

#             body {
#                 font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
#                 background-color: #000000;
#                 color: #ffffff;
#                 line-height: 1.6;
#                 min-height: 100vh;
#                 display: flex;
#                 flex-direction: column;
#             }

#             header {
#                 border-bottom: 1px solid #333333;
#                 padding: 0;
#             }

#             nav {
#                 max-width: 1200px;
#                 margin: 0 auto;
#                 display: flex;
#                 align-items: center;
#                 padding: 1rem 2rem;
#                 gap: 2rem;
#             }

#             .logo {
#                 font-size: 1.25rem;
#                 font-weight: 600;
#                 color: #ffffff;
#                 text-decoration: none;
#             }

#             .nav-links {
#                 display: flex;
#                 gap: 1.5rem;
#                 margin-left: auto;
#             }

#             .nav-links a {
#                 text-decoration: none;
#                 color: #888888;
#                 padding: 0.5rem 1rem;
#                 border-radius: 6px;
#                 transition: all 0.2s ease;
#                 font-size: 0.875rem;
#                 font-weight: 500;
#             }

#             .nav-links a:hover {
#                 color: #ffffff;
#                 background-color: #111111;
#             }

#             main {
#                 flex: 1;
#                 max-width: 1200px;
#                 margin: 0 auto;
#                 padding: 4rem 2rem;
#                 display: flex;
#                 flex-direction: column;
#                 align-items: center;
#                 text-align: center;
#             }

#             .hero {
#                 margin-bottom: 3rem;
#             }

#             .hero-code {
#                 margin-top: 2rem;
#                 width: 100%;
#                 max-width: 900px;
#                 display: grid;
#                 grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
#             }

#             .hero-code pre {
#                 background-color: #0a0a0a;
#                 border: 1px solid #333333;
#                 border-radius: 8px;
#                 padding: 1.5rem;
#                 text-align: left;
#                 grid-column: 1 / -1;
#             }

#             h1 {
#                 font-size: 3rem;
#                 font-weight: 700;
#                 margin-bottom: 1rem;
#                 background: linear-gradient(to right, #ffffff, #888888);
#                 -webkit-background-clip: text;
#                 -webkit-text-fill-color: transparent;
#                 background-clip: text;
#             }

#             .subtitle {
#                 font-size: 1.25rem;
#                 color: #888888;
#                 margin-bottom: 2rem;
#                 max-width: 600px;
#             }

#             .cards {
#                 display: grid;
#                 grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
#                 gap: 1.5rem;
#                 width: 100%;
#                 max-width: 900px;
#             }

#             .card {
#                 background-color: #111111;
#                 border: 1px solid #333333;
#                 border-radius: 8px;
#                 padding: 1.5rem;
#                 transition: all 0.2s ease;
#                 text-align: left;
#             }

#             .card:hover {
#                 border-color: #555555;
#                 transform: translateY(-2px);
#             }

#             .card h3 {
#                 font-size: 1.125rem;
#                 font-weight: 600;
#                 margin-bottom: 0.5rem;
#                 color: #ffffff;
#             }

#             .card p {
#                 color: #888888;
#                 font-size: 0.875rem;
#                 margin-bottom: 1rem;
#             }

#             .card a {
#                 display: inline-flex;
#                 align-items: center;
#                 color: #ffffff;
#                 text-decoration: none;
#                 font-size: 0.875rem;
#                 font-weight: 500;
#                 padding: 0.5rem 1rem;
#                 background-color: #222222;
#                 border-radius: 6px;
#                 border: 1px solid #333333;
#                 transition: all 0.2s ease;
#             }

#             .card a:hover {
#                 background-color: #333333;
#                 border-color: #555555;
#             }

#             .status-badge {
#                 display: inline-flex;
#                 align-items: center;
#                 gap: 0.5rem;
#                 background-color: #0070f3;
#                 color: #ffffff;
#                 padding: 0.25rem 0.75rem;
#                 border-radius: 20px;
#                 font-size: 0.75rem;
#                 font-weight: 500;
#                 margin-bottom: 2rem;
#             }

#             .status-dot {
#                 width: 6px;
#                 height: 6px;
#                 background-color: #00ff88;
#                 border-radius: 50%;
#             }

#             pre {
#                 background-color: #0a0a0a;
#                 border: 1px solid #333333;
#                 border-radius: 6px;
#                 padding: 1rem;
#                 overflow-x: auto;
#                 margin: 0;
#             }

#             code {
#                 font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
#                 font-size: 0.85rem;
#                 line-height: 1.5;
#                 color: #ffffff;
#             }

#             /* Syntax highlighting */
#             .keyword {
#                 color: #ff79c6;
#             }

#             .string {
#                 color: #f1fa8c;
#             }

#             .function {
#                 color: #50fa7b;
#             }

#             .class {
#                 color: #8be9fd;
#             }

#             .module {
#                 color: #8be9fd;
#             }

#             .variable {
#                 color: #f8f8f2;
#             }

#             .decorator {
#                 color: #ffb86c;
#             }

#             @media (max-width: 768px) {
#                 nav {
#                     padding: 1rem;
#                     flex-direction: column;
#                     gap: 1rem;
#                 }

#                 .nav-links {
#                     margin-left: 0;
#                 }

#                 main {
#                     padding: 2rem 1rem;
#                 }

#                 h1 {
#                     font-size: 2rem;
#                 }

#                 .hero-code {
#                     grid-template-columns: 1fr;
#                 }

#                 .cards {
#                     grid-template-columns: 1fr;
#                 }
#             }
#         </style>
#     </head>
#     <body>
#         <header>
#             <nav>
#                 <a href="/" class="logo">Vercel + FastAPI</a>
#                 <div class="nav-links">
#                     <a href="/docs">API Docs</a>
#                     <a href="/api/data">API</a>
#                 </div>
#             </nav>
#         </header>
#         <main>
#             <div class="hero">
#                 <h1>Vercel + FastAPI</h1>
#                 <div class="hero-code">
#                     <pre><code><span class="keyword">from</span> <span class="module">fastapi</span> <span class="keyword">import</span> <span class="class">FastAPI</span>

# <span class="variable">app</span> = <span class="class">FastAPI</span>()

# <span class="decorator">@app.get</span>(<span class="string">"/"</span>)
# <span class="keyword">def</span> <span class="function">read_root</span>():
#     <span class="keyword">return</span> {<span class="string">"Python"</span>: <span class="string">"on Vercel"</span>}</code></pre>
#                 </div>
#             </div>

#             <div class="cards">
#                 <div class="card">
#                     <h3>Interactive API Docs</h3>
#                     <p>Explore this API's endpoints with the interactive Swagger UI. Test requests and view response schemas in real-time.</p>
#                     <a href="/docs">Open Swagger UI →</a>
#                 </div>

#                 <div class="card">
#                     <h3>Sample Data</h3>
#                     <p>Access sample JSON data through our REST API. Perfect for testing and development purposes.</p>
#                     <a href="/api/data">Get Data →</a>
#                 </div>

#             </div>
#         </main>
#     </body>
#     </html>
#     """


from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from public.app.database import SessionLocal, init_db
from public.app.models import crud, models
from public.app.schemas import schemas
from public.app.email_utils import send_email
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000')

app = FastAPI(title='Formbricks - FastAPI Backend')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event('startup')
def on_startup():
    init_db()


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.post('/forms')
def create_form(form: schemas.FormCreate, db: Session = Depends(get_db)):
    created = crud.create_form(db, form.dict())
    return {'form': {'id': created.id, 'title': created.title}}


@app.get('/forms')
def list_forms(form_type: str | None = None, db: Session = Depends(get_db)):
    forms = crud.get_forms(db, form_type)
    result = []
    for f in forms:
        result.append(
            {
                'id': f.id, 
                'title': f.title,
                'form_type': f.form_type, 
                "created_at": f.created_at, 
                "questions": len(f.questions)
            }
        )
    return {'forms': result}


@app.get('/forms/{form_id}')
def get_form(form_id: str, db: Session = Depends(get_db)):
    f = crud.get_form(db, form_id)
    if not f:
        raise HTTPException(status_code=404, detail='Form not found')
    # convert questions
    questions = []
    for q in f.questions:
        questions.append({
            'id': q.id,
            'question_text': q.question_text,
            'question_type': q.question_type,
            'options': q.options,
            'validation_rules': q.validation_rules,
            'conditional_logic': q.conditional_logic,
            'is_required': q.is_required,
            'order_index': q.order_index,
            'section': q.section,
            'help_text': q.help_text,
        })
    return {
        'form': {
            'id': f.id,
            'title': f.title,
            'description': f.description,
            'form_type': f.form_type,
            'questions': sorted(questions, key=lambda x: x['order_index']),
        }
    }


@app.put('/forms/{form_id}')
def update_form(form_id: str, form: schemas.FormCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Form).filter(models.Form.id == form_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail='Form not found')
    existing.title = form.title
    existing.description = form.description
    existing.form_type = form.form_type
    existing.is_template = form.is_template
    existing.is_active = form.is_active
    existing.settings = form.settings
    db.commit()
    db.refresh(existing)
    return {'form': {'id': existing.id, 'title': existing.title}}


@app.delete('/forms/{form_id}')
def delete_form(form_id: str, db: Session = Depends(get_db)):
    existing = db.query(models.Form).filter(models.Form.id == form_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail='Form not found')
    db.delete(existing)
    db.commit()
    return {'ok': True}


@app.post('/forms/{form_id}/questions')
def create_questions_endpoint(form_id: str, questions: list[dict], db: Session = Depends(get_db)):
    form = crud.get_form(db, form_id)
    if not form:
        raise HTTPException(status_code=404, detail='Form not found')
    created = crud.create_questions(db, form_id, questions)
    return {'created': [q.id for q in created]}


@app.put('/questions/{question_id}')
def update_question(question_id: str, updates: dict, db: Session = Depends(get_db)):
    updated = crud.update_question(db, question_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail='Question not found')
    return {'question': {'id': updated.id}}


@app.delete('/questions/{question_id}')
def delete_question(question_id: str, db: Session = Depends(get_db)):
    ok = crud.delete_question(db, question_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Question not found')
    return {'ok': True}


@app.get('/responses')
def list_responses(form_id: str | None = None, db: Session = Depends(get_db)):
    if not form_id:
        raise HTTPException(status_code=400, detail='form_id is required')
    responses = crud.get_responses(db, form_id)
    result = []
    for r in responses:
        result.append({'id': r.id, 'status': r.status, 'respondent_email': r.respondent_email, 'submitted_at': r.submitted_at})
    return {'responses': result}


@app.get('/responses/{response_id}')
def get_response(response_id: str, db: Session = Depends(get_db)):
    r = crud.get_response(db, response_id)
    if not r:
        raise HTTPException(status_code=404, detail='Response not found')
    answers = []
    for a in r.answers:
        answers.append({'id': a.id, 'question_id': a.question_id, 'answer_text': a.answer_text, 'answer_number': a.answer_number, 'answer_json': a.answer_json})
    return {'response': {'id': r.id, 'status': r.status, 'answers': answers}}


@app.put('/responses/{response_id}')
def update_response(response_id: str, updates: dict, db: Session = Depends(get_db)):
    updated = crud.update_response(db, response_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail='Response not found')
    return {'response': {'id': updated.id, 'status': updated.status}}


@app.put('/responses/{response_id}/answers')
def update_response_answers(response_id: str, answers: list[dict], db: Session = Depends(get_db)):
    resp = crud.get_response(db, response_id)
    if not resp:
        raise HTTPException(status_code=404, detail='Response not found')
    created = crud.update_answers(db, response_id, answers)
    return {'updated': [c.id for c in created]}


@app.post('/tickets')
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    # Create a ticket and send the base form link
    t = crud.create_ticket(db, ticket.email, ticket.initial_form_id)

    base_form_id = ticket.initial_form_id
    if base_form_id:
        link = f"{API_BASE_URL}/forms/fill/{base_form_id}?ticket_id={t.id}"
        if ticket.email:
            send_email(ticket.email, 'Please complete the base form', f'Please complete the form: {link}')

    return {'ticket': {'id': t.id, 'email': t.email}}


@app.post('/tickets/{ticket_id}/assign')
def assign_form(ticket_id: str, payload: schemas.AssignFormPayload, db: Session = Depends(get_db)):
    ticket = crud.assign_form_to_ticket(db, ticket_id, payload.form_id)
    if not ticket:
        raise HTTPException(status_code=404, detail='Ticket not found')

    # send email to the ticket holder
    if ticket.email:
        link = f"{API_BASE_URL}/forms/fill/{payload.form_id}?ticket_id={ticket.id}"
        send_email(ticket.email, 'Please complete the event-specific form', f'Please complete the form: {link}')

    return {'ticket': {'id': ticket.id, 'assigned_form_id': ticket.assigned_form_id}}


@app.post('/responses')
def submit_response(payload: schemas.SubmitResponse, db: Session = Depends(get_db)):
    # Create response and answers
    payload_dict = payload.dict()
    response = crud.submit_response(db, payload_dict)

    # Build a map of answers by questionId for workflow evaluation
    answers_list = payload_dict.get('answers', []) or []
    answers_map = {}
    for a in answers_list:
        qid = a.get('questionId')
        # pick a sensible single value representation
        answers_map[qid] = a.get('answerText') if a.get('answerText') is not None else (
            a.get('answerNumber') if a.get('answerNumber') is not None else (
                a.get('answerJson') if a.get('answerJson') is not None else a.get('answerDate')
            )
        )

    # Evaluate conditional logic workflows defined on questions (if any)
    workflow_result = None
    try:
        workflow_result = crud.process_workflows(db, response, answers_map)
    except Exception:
        # don't let workflow failures break the response submission
        workflow_result = None

    # If the response references a ticket, and the ticket has an assigned form, mark pending approval
    if payload.referenceType == 'ticket' and payload.referenceId:
        # If admin assigned a specific form, we could change status
        # For now, mark pending_approval when reference is present
        crud.update_response_status(db, response.id, 'pending_approval')

    result = {'response': {'id': response.id, 'status': response.status}}
    if workflow_result and isinstance(workflow_result, dict) and workflow_result.get('next_form_id'):
        result['next_form_id'] = workflow_result.get('next_form_id')
    return result


@app.post('/responses/{response_id}/approve')
def approve_response(response_id: str, payload: schemas.ApprovePayload, db: Session = Depends(get_db)):
    if payload.approve:
        updated = crud.update_response_status(db, response_id, 'approved')
    else:
        updated = crud.update_response_status(db, response_id, 'rejected')
    if not updated:
        raise HTTPException(status_code=404, detail='Response not found')
    return {'response': {'id': updated.id, 'status': updated.status}}
