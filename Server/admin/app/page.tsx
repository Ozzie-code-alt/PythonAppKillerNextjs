"use client"

import { useEffect, useState } from "react";

interface Process {
  name: string;
}

export default function Home() {
  const [grabProcess, setGrabProcess] = useState<Process[]>([]);

  useEffect(() => {
    try {
      const GrabData = async () => {
        await fetch("http://127.0.0.1:5000/processes")
          .then((res) => res.json())
          .then((data) => setGrabProcess(data));
      };
        GrabData();
      
    } catch (error) {
      console.log("Fetch Data Error", error);
    }

  }, []);
  return (
    <div className="h-svh w-dvh bg-black">
      <p className="text-white">This is Current Data</p>
      <ul className="text-white">
        {grabProcess.map((processes,index) =>{
          return <li className="text-white" key={index}>{processes.name}</li>
        })}
      </ul>
    </div>
  );
}
