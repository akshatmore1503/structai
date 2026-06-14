import { NavBar } from "@/components/ui/NavBar";

export default function BuilderLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen" style={{ background: "#F8F9FB" }}>
      <NavBar />
      <main className="flex-1 ml-60">{children}</main>
    </div>
  );
}
