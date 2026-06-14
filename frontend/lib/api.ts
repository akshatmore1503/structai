import axios from "axios";
import { getSession } from "next-auth/react";
import type {
  GenerateResponse,
  Design,
  DesignListItem,
  ComponentExplanation,
  Topic,
  UserStats,
  AdminStats,
  QuizSubmitResponse,
} from "@/types";

const BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

const api = axios.create({ baseURL: `${BASE}/api/v1` });

// Attach the NextAuth JWT to every request
api.interceptors.request.use(async (config) => {
  const session = await getSession();
  const token = (session as Record<string, unknown> | null)?.accessToken;
  if (token && typeof token === "string") {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// ── Auth ──────────────────────────────────────────────────────────────────────
export const upsertUser = (data: { name: string; email: string; image?: string }) =>
  api.post("/auth/upsert-user", data).then((r) => r.data);

export const getMe = () => api.get("/auth/me").then((r) => r.data);

// ── Designs ───────────────────────────────────────────────────────────────────
export const generateDesign = (problem_statement: string): Promise<GenerateResponse> =>
  api.post("/designs/generate", { problem_statement }).then((r) => r.data);

export const submitClarifications = (
  designId: string,
  clarifications: Record<string, string>
): Promise<GenerateResponse> =>
  api.post(`/designs/${designId}/clarify`, { clarifications }).then((r) => r.data);

export const getDesign = (designId: string): Promise<Design> =>
  api.get(`/designs/${designId}`).then((r) => r.data);

export const listDesigns = (): Promise<DesignListItem[]> =>
  api.get("/designs/").then((r) => r.data);

export const deleteDesign = (designId: string) =>
  api.delete(`/designs/${designId}`).then((r) => r.data);

// ── Explainability ────────────────────────────────────────────────────────────
export const explainComponent = (
  designId: string,
  componentId: string
): Promise<ComponentExplanation> =>
  api
    .post("/explain/component", { design_id: designId, component_id: componentId })
    .then((r) => r.data);

// ── Learn Mode ────────────────────────────────────────────────────────────────
export const getTopics = (): Promise<Topic[]> =>
  api.get("/learn/topics").then((r) => r.data);

export const getTopic = (topicId: string): Promise<Topic> =>
  api.get(`/learn/topics/${topicId}`).then((r) => r.data);

export const generateQuiz = (topic: string, difficulty: string, num_questions = 5) =>
  api.post("/learn/quiz/generate", { topic, difficulty, num_questions }).then((r) => r.data);

export const submitQuiz = (
  quizId: string,
  topic: string,
  answers: { question_id: string; selected_option_id: string }[]
): Promise<QuizSubmitResponse> =>
  api.post("/learn/quiz/submit", { quiz_id: quizId, topic, answers }).then((r) => r.data);

// ── Export ────────────────────────────────────────────────────────────────────
export const downloadPdf = async (designId: string) => {
  const res = await api.get(`/export/${designId}/pdf`, { responseType: "blob" });
  const url = URL.createObjectURL(res.data);
  const a = document.createElement("a");
  a.href = url;
  a.download = `structai-${designId.slice(0, 8)}.pdf`;
  a.click();
  URL.revokeObjectURL(url);
};

export const downloadMarkdown = async (designId: string) => {
  const res = await api.get(`/export/${designId}/markdown`, { responseType: "blob" });
  const url = URL.createObjectURL(res.data);
  const a = document.createElement("a");
  a.href = url;
  a.download = `structai-${designId.slice(0, 8)}.md`;
  a.click();
  URL.revokeObjectURL(url);
};

// ── Analytics ─────────────────────────────────────────────────────────────────
export const getMyStats = (): Promise<UserStats> =>
  api.get("/analytics/me").then((r) => r.data);

export const getAdminStats = (): Promise<AdminStats> =>
  api.get("/analytics/admin").then((r) => r.data);

// ── Admin ─────────────────────────────────────────────────────────────────────
export const getAdminHealth = () => api.get("/admin/health").then((r) => r.data);
export const listUsers = () => api.get("/admin/users").then((r) => r.data);
export const updateUserRole = (userId: string, role: string) =>
  api.patch(`/admin/users/${userId}/role`, null, { params: { role } }).then((r) => r.data);
export const rebuildIndex = () =>
  api.post("/admin/rebuild-index", { confirm: true }).then((r) => r.data);
