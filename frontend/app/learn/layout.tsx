import { NavBar } from "@/components/ui/NavBar";

export default function LearnLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen" style={{ background: "#F8F9FB" }}>
      <NavBar />
      <main className="flex-1 ml-60 p-10">{children}</main>
    </div>
  );
}
