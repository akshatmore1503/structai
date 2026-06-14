"use client";
import { useEffect, useState } from "react";
import { Shield, RefreshCw, Users, Activity, Database } from "lucide-react";
import { getAdminStats, getAdminHealth, listUsers, updateUserRole, rebuildIndex } from "@/lib/api";
import { Spinner } from "@/components/ui/Spinner";
import type { AdminStats } from "@/types";

export default function AdminPage() {
  const [stats, setStats] = useState<AdminStats | null>(null);
  const [health, setHealth] = useState<{ mongodb: string; faiss_index: string } | null>(null);
  const [users, setUsers] = useState<{ id: string; name: string; email: string; role: string; design_count: number; quiz_count: number }[]>([]);
  const [loading, setLoading] = useState(true);
  const [rebuildLoading, setRebuildLoading] = useState(false);
  const [rebuildMsg, setRebuildMsg] = useState("");

  useEffect(() => {
    Promise.all([getAdminStats(), getAdminHealth(), listUsers()])
      .then(([s, h, u]) => { setStats(s); setHealth(h); setUsers(u); })
      .finally(() => setLoading(false));
  }, []);

  async function handleRebuild() {
    setRebuildLoading(true);
    try {
      const res = await rebuildIndex();
      setRebuildMsg(res.status);
    } finally {
      setRebuildLoading(false);
    }
  }

  async function handleRoleToggle(userId: string, currentRole: string) {
    const newRole = currentRole === "admin" ? "student" : "admin";
    await updateUserRole(userId, newRole);
    setUsers((prev) => prev.map((u) => u.id === userId ? { ...u, role: newRole } : u));
  }

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-7 h-7" /></div>;

  return (
    <div className="max-w-5xl">
      <div className="flex items-center gap-2 text-brand-400 mb-6">
        <Shield size={18} />
        <span className="text-sm font-medium">Admin Control Panel</span>
      </div>
      <h1 className="text-2xl font-bold text-white mb-8">System Administration</h1>

      {/* Stats */}
      {stats && (
        <div className="grid grid-cols-4 gap-4 mb-8">
          {[
            { label: "Total Users", value: stats.total_users, icon: Users },
            { label: "Total Designs", value: stats.total_designs, icon: Activity },
            { label: "Quiz Attempts", value: stats.total_quiz_attempts, icon: Database },
            { label: "Active (7d)", value: stats.active_users_7d, icon: RefreshCw },
          ].map(({ label, value, icon: Icon }) => (
            <div key={label} className="card">
              <Icon size={16} className="text-brand-400 mb-2" />
              <p className="text-2xl font-bold text-white">{value}</p>
              <p className="text-xs text-gray-500">{label}</p>
            </div>
          ))}
        </div>
      )}

      {/* Health */}
      {health && (
        <div className="card mb-8">
          <h2 className="font-semibold text-white mb-4 flex items-center gap-2">
            <Activity size={16} className="text-brand-400" />
            System Health
          </h2>
          <div className="flex gap-4">
            {Object.entries(health).map(([key, status]) => (
              <div key={key} className="flex items-center gap-2">
                <div className={`w-2 h-2 rounded-full ${status === "ok" || status === "ready" ? "bg-green-400" : "bg-amber-400"}`} />
                <span className="text-sm text-gray-400">{key}: <span className="text-white">{status}</span></span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* FAISS rebuild */}
      <div className="card mb-8">
        <h2 className="font-semibold text-white mb-2 flex items-center gap-2">
          <Database size={16} className="text-brand-400" />
          Vector Index
        </h2>
        <p className="text-sm text-gray-400 mb-4">Rebuild the FAISS index from seed architecture patterns.</p>
        {rebuildMsg && <p className="text-sm text-amber-400 mb-3">{rebuildMsg}</p>}
        <button onClick={handleRebuild} disabled={rebuildLoading} className="btn-primary text-sm flex items-center gap-2">
          {rebuildLoading ? <Spinner className="w-4 h-4" /> : <RefreshCw size={14} />}
          Rebuild Index
        </button>
      </div>

      {/* Users */}
      <div className="card">
        <h2 className="font-semibold text-white mb-4 flex items-center gap-2">
          <Users size={16} className="text-brand-400" />
          Users ({users.length})
        </h2>
        <div className="space-y-2 max-h-96 overflow-y-auto">
          {users.map((u) => (
            <div key={u.id} className="flex items-center gap-3 py-2 border-b border-white/5 last:border-0">
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-white truncate">{u.name}</p>
                <p className="text-xs text-gray-500 truncate">{u.email}</p>
              </div>
              <div className="text-xs text-gray-600 text-right">
                <p>{u.design_count} designs</p>
                <p>{u.quiz_count} quizzes</p>
              </div>
              <button
                onClick={() => handleRoleToggle(u.id, u.role)}
                className={`badge border cursor-pointer hover:opacity-80 transition-opacity ${
                  u.role === "admin"
                    ? "bg-brand-500/10 text-brand-400 border-brand-500/20"
                    : "bg-white/5 text-gray-400 border-white/10"
                }`}
              >
                {u.role}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
