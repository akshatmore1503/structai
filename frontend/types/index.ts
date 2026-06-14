// ── Auth ─────────────────────────────────────────────────────────────────────
export interface AppUser {
  id: string;
  name: string;
  email: string;
  image?: string;
  role: "student" | "admin";
  design_count: number;
  quiz_count: number;
}

// ── Design Builder ────────────────────────────────────────────────────────────
export type NodeType =
  | "client"
  | "api_gateway"
  | "load_balancer"
  | "web_server"
  | "database"
  | "nosql_database"
  | "cache"
  | "message_queue"
  | "cdn"
  | "object_storage"
  | "auth_service"
  | "monitoring"
  | "ml_service";

export interface ArchNode {
  id: string;
  type: NodeType;
  label: string;
  description: string;
  tech: string;
}

export interface ArchEdge {
  id: string;
  source: string;
  target: string;
  label: string;
  animated: boolean;
}

export interface Architecture {
  nodes: ArchNode[];
  edges: ArchEdge[];
  tech_stack: string[];
  summary: string;
}

export interface Design {
  id: string;
  problem_statement: string;
  architecture: Architecture | null;
  explanations: Record<string, ComponentExplanation>;
  status: "pending" | "awaiting_clarification" | "complete";
  created_at: string;
}

export interface DesignListItem {
  id: string;
  problem_statement: string;
  status: string;
  created_at: string;
}

export interface GenerateResponse {
  design_id: string;
  status: "complete" | "awaiting_clarification";
  architecture?: Architecture;
  clarifying_questions?: string[];
}

// ── Explainability ────────────────────────────────────────────────────────────
export interface ComponentExplanation {
  what: string;
  why: string;
  alternatives: string[];
  trade_offs: string;
  learn_more: string;
}

// ── Learn Mode ────────────────────────────────────────────────────────────────
export interface Topic {
  id: string;
  title: string;
  description: string;
  icon: string;
  difficulty: "beginner" | "intermediate" | "advanced";
  estimated_minutes: number;
}

export interface QuizOption {
  id: string;
  text: string;
}

export interface QuizQuestion {
  id: string;
  question: string;
  options: QuizOption[];
  correct_option_id: string;
  explanation: string;
}

export interface QuizResult {
  question_id: string;
  correct: boolean;
  correct_option_id: string;
  explanation: string;
}

export interface QuizSubmitResponse {
  score: number;
  results: QuizResult[];
  passed: boolean;
}

// ── Analytics ─────────────────────────────────────────────────────────────────
export interface UserStats {
  total_designs: number;
  total_quizzes: number;
  avg_quiz_score: number;
  recent_designs: DesignListItem[];
  quiz_history: { topic: string; score: number; completed_at: string }[];
}

export interface AdminStats {
  total_users: number;
  total_designs: number;
  total_quiz_attempts: number;
  active_users_7d: number;
  daily_designs_7d: { date: string; count: number }[];
}
