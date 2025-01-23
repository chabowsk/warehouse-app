import React from "react";
import { Link } from "react-router-dom";
import Account from "./Account";

export default function Sidebar() {
  return (
    <div className="bg-neutral-700 w-60 p-3 flex flex-col text-white">
      <Account />
      <div className="flex-1 border-b">
        <div className="">
          <Link to="/">Dashboard</Link>
        </div>
        <div className="">
          <Link to="/gabin">Gąbin</Link>
        </div>
      </div>

      <div className="">Settings</div>
    </div>
  );
}
