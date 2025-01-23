import React from "react";
import { Link } from "react-router-dom";

export default function Client() {
  return (
    <div>
      <h1>This is Gabin page</h1> <Link to="/" className="underline">go to dashboard page</Link>
    </div>
  );
}
