import { useState } from 'react';
import ModerationResult from './components/ModerationResult';

// Define the structure of the API response
interface ModerationResponse {
  label: 'POSITIVE' | 'NEGATIVE';
  score: number;
}

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState<ModerationResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleModerate = async () => {
    if (!text.trim()) {
      setError('Please enter some text to analyze.');
      return;
    }

    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/moderate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Failed to connect to the moderation service.');
      }

      const data: ModerationResponse = await response.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-4">
      <div className="w-full max-w-2xl">
        <header className="text-center mb-8">
          <h1 className="text-5xl font-bold text-cyan-400">SafeLens</h1>
          <p className="text-gray-400 mt-2">Real-time content moderation powered by AI.</p>
        </header>

        <main className="bg-gray-800 p-6 rounded-xl shadow-lg">
          <textarea
            className="w-full p-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-cyan-500 focus:outline-none transition"
            rows={5}
            placeholder="Enter text for analysis..."
            value={text}
            onChange={(e) => setText(e.target.value)}
            disabled={isLoading}
          />
          <button
            className={`w-full mt-4 p-3 rounded-lg font-semibold transition ${
              isLoading
                ? 'bg-gray-600 cursor-not-allowed'
                : 'bg-cyan-600 hover:bg-cyan-700'
            }`}
            onClick={handleModerate}
            disabled={isLoading}
          >
            {isLoading ? 'Analyzing...' : 'Analyze Content'}
          </button>
        </main>

        <footer className="mt-6">
          {error && <p className="text-center text-red-400">{error}</p>}
          {result && <ModerationResult result={result} />}
        </footer>
      </div>
    </div>
  );
}

export default App;
