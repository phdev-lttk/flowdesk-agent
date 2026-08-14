import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
    {
      type: "ai",
      text: "Olá! Como posso ajudar ?",
    },
  ]);

  async function handleSubmit(e) {
    e.preventDefault();

    if (!question.trim()) return;

    const currentQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        text: currentQuestion,
      },
    ]);

    setQuestion("");

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: currentQuestion,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          type: "ai",
          text: data.answer,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          type: "ai",
          text: "Erro ao consultar o servidor.",
        },
      ]);
    }
  }

  return (
    <div className="flex h-screen bg-slate-950 text-white">
      <aside className="w-72 border-r border-slate-800 bg-slate-900 p-5">
        <h1 className="text-xl font-bold">
          FlowDesk Agent
        </h1>

        <p className="mt-1 text-sm text-slate-400">
          Seus documentos
        </p>

        <div className="mt-6 space-y-3">
          <div className="rounded-xl border border-slate-700 bg-slate-800 p-4">
            <div className="font-medium">
              📄 flow_TOS.pdf
            </div>

            <div className="mt-1 text-xs text-emerald-400">
              Documento disponível
            </div>
          </div>
        </div>
      </aside>

      <main className="flex flex-1 flex-col">
        <header className="border-b border-slate-800 px-8 py-5">
          <h2 className="text-lg font-semibold">
            Chat
          </h2>

          <p className="text-sm text-slate-400">
            Retire suas dúvidas.
          </p>
        </header>

        <section className="flex-1 overflow-y-auto px-8 py-8">
          <div className="mx-auto max-w-3xl space-y-6">
            {messages.map((message, index) => (
              <div
                key={index}
                className={
                  message.type === "user"
                    ? "flex justify-end"
                    : "flex justify-start"
                }
              >
                <div
                  className={
                    message.type === "user"
                      ? "max-w-xl rounded-2xl bg-indigo-600 px-5 py-3"
                      : "max-w-xl rounded-2xl border border-slate-800 bg-slate-900 px-5 py-3"
                  }
                >
                  {message.text}
                </div>
              </div>
            ))}
          </div>
        </section>

        <form
          onSubmit={handleSubmit}
          className="border-t border-slate-800 p-6"
        >
          <div className="mx-auto flex max-w-3xl gap-3">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Faça uma pergunta sobre seus documentos..."
              className="flex-1 rounded-xl border border-slate-700 bg-slate-900 px-5 py-4 outline-none transition focus:border-indigo-500"
            />

            <button
              type="submit"
              className="rounded-xl bg-indigo-600 px-6 font-medium transition hover:bg-indigo-500"
            >
              Enviar
            </button>
          </div>
        </form>
      </main>
    </div>
  );
}

export default App;