import React from 'react'

export default function Account(){
  return (
    <div className="border-b mb-4 mt-2 pb-4 border-stone-300">
        <button className="flex p-0.5 hover:bg-stone-200 roudned transition-colors relative gap-2 w-full items-center">
          <img
            src="https://robohash.org/user1"
            alt="avatar"
            className="size-8 rounded shrink-0 bg-violet-500 shadow"
          />
          <div className="text-start">
            <span className="text-sm font-bold block">Kacper</span>
            <span className="text-xs block text-stone-500">chabowsk@mail.com</span>
          </div>
        </button>
      </div>
  );
};
