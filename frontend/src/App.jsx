import { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [roll, setRoll] = useState("");
  const [clas, setClas] = useState("");
  const [pos, setPos] = useState("");
  const [searchName, setSearchName] = useState("");
  const [result, setResult] = useState(null);

  const API_BASE = "http://127.0.0.1:8000"; // FastAPI backend

  // Add new detail
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_BASE}/details`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          roll: parseInt(roll),
          clas,
          pos,
        }),
      });

      if (!res.ok) throw new Error("Failed to add");

      alert("✅ Added successfully!");
      setName("");
      setRoll("");
      setClas("");
      setPos("");
    } catch (err) {
      console.error(err);
      alert("❌ Error adding details");
    }
  };

  // Search by name
  const handleSearch = async () => {
    try {
      const res = await fetch(`${API_BASE}/${searchName}`);
      if (!res.ok) throw new Error("Not found");
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert("❌ Not found or server error");
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "20px" }}>
      <h1>📘 Student Details App</h1>

      {/* Add form */}
      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <h2>Add Student</h2>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <br />
        <input
          type="number"
          placeholder="Roll No"
          value={roll}
          onChange={(e) => setRoll(e.target.value)}
          required
        />
        <br />
        <input
          type="text"
          placeholder="Class"
          value={clas}
          onChange={(e) => setClas(e.target.value)}
          required
        />
        <br />
        <input
          type="text"
          placeholder="Position"
          value={pos}
          onChange={(e) => setPos(e.target.value)}
          required
        />
        <br />
        <button type="submit">Add</button>
      </form>

      {/* Search form */}
      <div>
        <h2>Search Student</h2>
        <input
          type="text"
          placeholder="Enter name"
          value={searchName}
          onChange={(e) => setSearchName(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {/* Search result */}
      {result && (
        <div style={{ marginTop: "20px", padding: "10px", border: "1px solid black" }}>
          <h3>🔎 Search Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
