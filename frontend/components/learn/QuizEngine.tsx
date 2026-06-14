"use client";
import { useState } from "react";
import { CheckCircle, XCircle, ChevronRight, Trophy, RotateCcw } from "lucide-react";
import { clsx } from "clsx";
import { submitQuiz } from "@/lib/api";
import { Spinner } from "@/components/ui/Spinner";
import type { QuizQuestion, QuizResult, QuizSubmitResponse } from "@/types";

interface Props {
  quizId: string;
  topic: string;
  questions: QuizQuestion[];
  onRetry: () => void;
}

export function QuizEngine({ quizId, topic, questions, onRetry }: Props) {
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [current, setCurrent] = useState(0);
  const [submitted, setSubmitted] = useState(false);
  const [results, setResults] = useState<QuizSubmitResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const q = questions[current];
  const totalAnswered = Object.keys(answers).length;

  async function handleSubmit() {
    setLoading(true);
    try {
      const payload = Object.entries(answers).map(([qId, optId]) => ({
        question_id: qId,
        selected_option_id: optId,
      }));
      const res = await submitQuiz(quizId, topic, payload);
      setResults(res);
      setSubmitted(true);
    } finally {
      setLoading(false);
    }
  }

  // Results view
  if (submitted && results) {
    const resultMap: Record<string, QuizResult> = {};
    results.results.forEach((r) => (resultMap[r.question_id] = r));

    return (
      <div className="space-y-6">
        {/* Score card */}
        <div className={clsx(
          "card text-center p-8",
          results.passed ? "border-green-500/20 bg-green-500/5" : "border-amber-500/20 bg-amber-500/5"
        )}>
          <Trophy className={clsx("mx-auto mb-3", results.passed ? "text-green-400" : "text-amber-400")} size={36} />
          <p className="text-4xl font-bold text-white mb-1">{results.score}%</p>
          <p className={clsx("font-medium", results.passed ? "text-green-400" : "text-amber-400")}>
            {results.passed ? "Well done! You passed." : "Keep studying — you'll get it!"}
          </p>
        </div>

        {/* Per-question breakdown */}
        <div className="space-y-4">
          {questions.map((q, i) => {
            const r = resultMap[q.id];
            return (
              <div key={q.id} className="card">
                <div className="flex items-start gap-3 mb-3">
                  {r?.correct ? (
                    <CheckCircle size={18} className="text-green-400 flex-shrink-0 mt-0.5" />
                  ) : (
                    <XCircle size={18} className="text-red-400 flex-shrink-0 mt-0.5" />
                  )}
                  <p className="text-sm font-medium text-white">{i + 1}. {q.question}</p>
                </div>
                <div className="ml-7 space-y-1.5">
                  {q.options.map((opt) => (
                    <div
                      key={opt.id}
                      className={clsx(
                        "text-xs px-3 py-2 rounded-lg border",
                        opt.id === r?.correct_option_id
                          ? "bg-green-500/10 border-green-500/30 text-green-300"
                          : answers[q.id] === opt.id && !r?.correct
                          ? "bg-red-500/10 border-red-500/30 text-red-300"
                          : "bg-white/3 border-white/10 text-gray-500"
                      )}
                    >
                      {opt.text}
                    </div>
                  ))}
                </div>
                <p className="ml-7 mt-3 text-xs text-gray-400 leading-relaxed">
                  💡 {r?.explanation}
                </p>
              </div>
            );
          })}
        </div>

        <button onClick={onRetry} className="btn-ghost flex items-center gap-2">
          <RotateCcw size={14} />
          Try again
        </button>
      </div>
    );
  }

  // Quiz view
  return (
    <div>
      {/* Progress */}
      <div className="flex items-center justify-between mb-6">
        <p className="text-sm text-gray-400">
          Question {current + 1} of {questions.length}
        </p>
        <div className="flex gap-1">
          {questions.map((_, i) => (
            <button
              key={i}
              onClick={() => setCurrent(i)}
              className={clsx(
                "w-2.5 h-2.5 rounded-full transition-colors",
                i === current ? "bg-brand-500" : answers[questions[i].id] ? "bg-brand-500/40" : "bg-white/10"
              )}
            />
          ))}
        </div>
      </div>

      {/* Question */}
      <div className="card mb-4">
        <p className="text-base font-medium text-white leading-relaxed">{q.question}</p>
      </div>

      {/* Options */}
      <div className="space-y-2.5 mb-8">
        {q.options.map((opt) => (
          <button
            key={opt.id}
            onClick={() => setAnswers((prev) => ({ ...prev, [q.id]: opt.id }))}
            className={clsx(
              "w-full text-left text-sm px-4 py-3 rounded-xl border transition-all",
              answers[q.id] === opt.id
                ? "bg-brand-500/10 border-brand-500/40 text-white"
                : "bg-white/3 border-white/10 text-gray-300 hover:border-white/20 hover:bg-white/5"
            )}
          >
            <span className="font-medium text-brand-400 mr-2">{opt.id.toUpperCase()}.</span>
            {opt.text}
          </button>
        ))}
      </div>

      {/* Navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={() => setCurrent((c) => Math.max(0, c - 1))}
          disabled={current === 0}
          className="btn-ghost disabled:opacity-30 text-sm"
        >
          Previous
        </button>

        {current < questions.length - 1 ? (
          <button
            onClick={() => setCurrent((c) => c + 1)}
            disabled={!answers[q.id]}
            className="btn-primary flex items-center gap-2 text-sm disabled:opacity-40"
          >
            Next <ChevronRight size={15} />
          </button>
        ) : (
          <button
            onClick={handleSubmit}
            disabled={totalAnswered < questions.length || loading}
            className="btn-primary flex items-center gap-2 text-sm disabled:opacity-40"
          >
            {loading ? <Spinner className="w-4 h-4" /> : <Trophy size={15} />}
            Submit Quiz
          </button>
        )}
      </div>

      {totalAnswered < questions.length && current === questions.length - 1 && (
        <p className="text-xs text-amber-400 mt-3 text-center">
          Answer all {questions.length} questions before submitting.
        </p>
      )}
    </div>
  );
}
