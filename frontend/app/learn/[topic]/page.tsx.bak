"use client";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { ArrowLeft, Brain, Loader } from "lucide-react";
import { getTopic, generateQuiz } from "@/lib/api";
import { QuizEngine } from "@/components/learn/QuizEngine";
import { Spinner } from "@/components/ui/Spinner";
import type { Topic, QuizQuestion } from "@/types";
import { clsx } from "clsx";

const DIFFICULTIES = ["beginner", "intermediate", "advanced"] as const;

export default function TopicPage() {
  const { topic: topicId } = useParams<{ topic: string }>();
  const router = useRouter();

  const [topic, setTopic] = useState<Topic | null>(null);
  const [difficulty, setDifficulty] = useState<string>("intermediate");
  const [numQuestions, setNumQuestions] = useState(5);

  const [quizId, setQuizId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<QuizQuestion[]>([]);
  const [generating, setGenerating] = useState(false);

  useEffect(() => {
    getTopic(topicId).then(setTopic).catch(() => router.push("/learn"));
  }, [topicId, router]);

  async function startQuiz() {
    setGenerating(true);
    try {
      const res = await generateQuiz(topic!.title, difficulty, numQuestions);
      setQuizId(res.quiz_id);
      setQuestions(res.questions);
    } finally {
      setGenerating(false);
    }
  }

  function resetQuiz() {
    setQuizId(null);
    setQuestions([]);
  }

  if (!topic) {
    return <div className="flex justify-center py-20"><Spinner className="w-7 h-7" /></div>;
  }

  return (
    <div className="max-w-2xl">
      <button
        onClick={() => router.push("/learn")}
        className="flex items-center gap-2 text-gray-400 hover:text-white mb-8 transition-colors text-sm"
      >
        <ArrowLeft size={15} />
        Back to topics
      </button>

      {!quizId ? (
        <>
          {/* Topic header */}
          <div className="card mb-8">
            <div className="flex items-center gap-3 mb-4">
              <span className="text-4xl">{topic.icon}</span>
              <div>
                <h1 className="text-2xl font-bold text-white">{topic.title}</h1>
                <p className="text-gray-400 text-sm mt-1">{topic.description}</p>
              </div>
            </div>
          </div>

          {/* Quiz configuration */}
          <div className="card">
            <div className="flex items-center gap-2 text-brand-400 mb-5">
              <Brain size={16} />
              <span className="text-sm font-medium">Configure your quiz</span>
            </div>

            <div className="mb-5">
              <label className="block text-sm font-medium text-gray-300 mb-2">Difficulty</label>
              <div className="flex gap-2">
                {DIFFICULTIES.map((d) => (
                  <button
                    key={d}
                    onClick={() => setDifficulty(d)}
                    className={clsx(
                      "flex-1 py-2 rounded-lg text-sm font-medium transition-colors border",
                      difficulty === d
                        ? "bg-brand-500/10 border-brand-500/40 text-brand-300"
                        : "bg-white/3 border-white/10 text-gray-400 hover:text-white hover:border-white/20"
                    )}
                  >
                    {d.charAt(0).toUpperCase() + d.slice(1)}
                  </button>
                ))}
              </div>
            </div>

            <div className="mb-6">
              <label className="block text-sm font-medium text-gray-300 mb-2">
                Number of questions: <span className="text-brand-400">{numQuestions}</span>
              </label>
              <input
                type="range"
                min={3}
                max={10}
                value={numQuestions}
                onChange={(e) => setNumQuestions(Number(e.target.value))}
                className="w-full accent-brand-500"
              />
              <div className="flex justify-between text-xs text-gray-600 mt-1">
                <span>3</span><span>10</span>
              </div>
            </div>

            <button
              onClick={startQuiz}
              disabled={generating}
              className="btn-primary w-full flex items-center justify-center gap-2"
            >
              {generating ? (
                <><Spinner className="w-4 h-4" /> Generating quiz…</>
              ) : (
                <><Brain size={15} /> Start Quiz</>
              )}
            </button>
          </div>
        </>
      ) : (
        <>
          <div className="mb-6">
            <h1 className="text-xl font-bold text-white">{topic.title} Quiz</h1>
            <p className="text-gray-500 text-sm mt-1">{difficulty} · {questions.length} questions</p>
          </div>
          <QuizEngine
            quizId={quizId}
            topic={topic.title}
            questions={questions}
            onRetry={resetQuiz}
          />
        </>
      )}
    </div>
  );
}
