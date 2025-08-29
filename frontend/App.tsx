import React, { useState } from 'react';

// Note: This is a template. You'll need to set up a React project
// (e.g., with Create React App) and install TailwindCSS.

const App = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);

  const handleModerate = async () => {
    // Replace with your actual API endpoint
    const response = await fetch('http://127.0.0.1:8000/moderate/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4 text-center">SafeLens Dashboard</h1>
        <textarea
          className="w-full p-2 border rounded mb-4"
          rows="4"
          placeholder="Enter text to moderate..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        <button
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          onClick={handleModerate}
        >
          Moderate Content
        </button>
        {result && (
          <div className="mt-4 p-4 border rounded bg-gray-50">
            <h2 className="font-bold">Moderation Result:</h2>
            <p>Harmful: <span className={result.is_harmful ? 'text-red-500' : 'text-green-500'}>{result.is_harmful ? 'Yes' : 'No'}</span></p>
            <p>Confidence: {Math.round(result.confidence_score * 100)}%</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
