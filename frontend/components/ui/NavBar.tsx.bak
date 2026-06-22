"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useSession, signOut } from "next-auth/react";
import { Cpu, LayoutDashboard, Zap, BookOpen, BarChart3, LogOut } from "lucide-react";
import { clsx } from "clsx";
import Image from "next/image";

const NAV = [
  { href: "/dashboard", label: "Dashboard",      icon: LayoutDashboard },
  { href: "/builder",   label: "Design Builder", icon: Zap             },
  { href: "/learn",     label: "Learn Mode",     icon: BookOpen        },
  { href: "/analytics", label: "Analytics",      icon: BarChart3       },
];

export function NavBar() {
  const { data: session } = useSession();
  const pathname = usePathname();

  return (
    <aside
      className="w-60 min-h-screen flex flex-col py-6 px-4 fixed top-0 left-0 z-30"
      style={{
        background: "#0A0E2E",
        borderRight: "1px solid rgba(255,255,255,0.06)",
      }}
    >
      {/* Logo */}
      <Link href="/dashboard" className="flex items-center gap-3 px-2 mb-8 group">
        <div
          className="w-8 h-8 rounded-[10px] flex items-center justify-center flex-shrink-0"
          style={{
            background: "linear-gradient(135deg,#6366F1,#4F46E5)",
            boxShadow: "0 4px 12px rgba(99,102,241,0.4)",
          }}
        >
          <Cpu size={15} className="text-white" />
        </div>
        <div>
          <span
            className="text-[15px] font-bold tracking-tight"
            style={{ color: "#F9FAFB", fontFamily: "'Space Grotesk', system-ui" }}
          >
            StructAI
          </span>
          <div className="text-[10px] font-medium" style={{ color: "#4B5570" }}>
            AI System Design
          </div>
        </div>
      </Link>

      {/* Label */}
      <div className="px-2 mb-2">
        <span style={{ fontSize: 10, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "#2E3560" }}>
          Navigation
        </span>
      </div>

      {/* Nav */}
      <nav className="flex-1 space-y-0.5">
        {NAV.map(({ href, label, icon: Icon }) => {
          const active = href === "/dashboard"
            ? pathname === href
            : pathname.startsWith(href);
          return (
            <Link
              key={href}
              href={href}
              className={clsx(
                "relative flex items-center gap-3 px-3 py-2.5 rounded-xl text-[13px] font-medium transition-all duration-150",
                active ? "" : "hover:bg-white/[0.04]"
              )}
              style={active ? {
                background: "rgba(99,102,241,0.18)",
                color: "#A5B4FC",
              } : { color: "#4B5570" }}
            >
              {active && (
                <span
                  className="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-[18px] rounded-r-full"
                  style={{ background: "#6366F1" }}
                />
              )}
              <div
                className="w-6 h-6 rounded-lg flex items-center justify-center flex-shrink-0"
                style={active ? { background: "rgba(99,102,241,0.25)" } : {}}
              >
                <Icon
                  size={13}
                  strokeWidth={active ? 2.5 : 2}
                  style={{ color: active ? "#818CF8" : "#374175" }}
                />
              </div>
              <span style={{ color: active ? "#C7D2FE" : "#6B7A9F" }}>{label}</span>
            </Link>
          );
        })}
      </nav>

      {/* User */}
      {session?.user && (
        <div className="mt-4 pt-4" style={{ borderTop: "1px solid rgba(255,255,255,0.05)" }}>
          <div
            className="flex items-center gap-3 px-3 py-2.5 mb-1 rounded-xl"
            style={{ background: "rgba(255,255,255,0.03)" }}
          >
            {session.user.image ? (
              <Image
                src={session.user.image}
                alt="avatar"
                width={28}
                height={28}
                className="rounded-full flex-shrink-0"
                style={{ border: "2px solid rgba(99,102,241,0.4)" }}
              />
            ) : (
              <div
                className="w-7 h-7 rounded-full flex items-center justify-center text-white text-[11px] font-bold flex-shrink-0"
                style={{ background: "linear-gradient(135deg,#6366F1,#4F46E5)" }}
              >
                {session.user.name?.[0]}
              </div>
            )}
            <div className="flex-1 min-w-0">
              <p className="text-[12px] font-semibold truncate" style={{ color: "#E8EAFF" }}>
                {session.user.name}
              </p>
              <p className="text-[10px] truncate" style={{ color: "#374175" }}>
                {session.user.email}
              </p>
            </div>
          </div>
          <button
            onClick={() => signOut({ callbackUrl: "/" })}
            className="flex items-center gap-2.5 w-full px-3 py-2 text-[12px] font-medium rounded-xl transition-all duration-150 hover:bg-white/[0.04]"
            style={{ color: "#374175" }}
          >
            <LogOut size={12} style={{ color: "#374175" }} />
            Sign out
          </button>
        </div>
      )}
    </aside>
  );
}
