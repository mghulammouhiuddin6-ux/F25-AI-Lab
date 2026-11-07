"""Conservative FAQ chatbot: exact questions answer; paraphrases show candidates."""
from lab6_search import Retriever
FAQ = [
 {"id":"faq:password", "question":"How do I reset my password?", "answer":"Use the recovery link on the login page.", "source":"it_help.txt"},
 {"id":"faq:submit", "question":"Where do I submit my assignment?", "answer":"Use the assignment upload page in the learning portal.", "source":"assessment.txt"},
 {"id":"faq:late", "question":"Can illness justify a late submission?", "answer":"Request an extension with medical evidence before the deadline.", "source":"handbook.txt"},
 {"id":"faq:damage", "question":"What should I do if my parcel is damaged?", "answer":"Contact support within 48 hours and attach photographs of the item and packaging.", "source":"returns_guide.txt"},
 {"id":"faq:token", "question":"How do I renew an expired API token?", "answer":"Send POST /v2/token/refresh with the refresh_token field; never print its value in logs.", "source":"api_docs.txt"},
]
def build_bot(backend="tfidf"):
    records=[dict(r, text=r["question"]+" "+r["answer"]) for r in FAQ]
    return Retriever(records, backend)
def reply(engine, query):
    if not query.strip(): return "Please enter a question."
    for r in FAQ:
        if query.strip().casefold()==r["question"].casefold():
            return r["answer"]+" [source: "+r["source"]+"]"
    hits=engine.search(query, k=3)
    if not hits: return "No matching FAQ. Please contact the help desk."
    lines=["Possible matches; choose or rephrase your question:"]
    lines.extend(f"{r['question']} (similarity {score:.3f})" for r,score in hits)
    return "\n".join(lines)
if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser(); p.add_argument("--backend",choices=["tfidf","embedding"],default="tfidf")
    args=p.parse_args(); engine=build_bot(args.backend)
    print("FAQ assistant. Type exit to stop.")
    while True:
        try: query=input("You: ")
        except (EOFError,KeyboardInterrupt): break
        if query.strip().lower()=="exit": break
        print("Bot:",reply(engine,query))
