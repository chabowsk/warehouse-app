import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div>
      <h1>This is Dashboard</h1>
      <Link to="/gabin" className="underline">go to gabin page</Link>
    </div>
  );
}
