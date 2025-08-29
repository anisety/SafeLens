interface ModerationResultProps {
  result: {
    label: 'POSITIVE' | 'NEGATIVE';
    score: number;
  };
}

const ModerationResult = ({ result }: ModerationResultProps) => {
  const isHarmful = result.label === 'NEGATIVE';
  const confidence = (result.score * 100).toFixed(1);
  const colorClass = isHarmful ? 'bg-red-900 border-red-700' : 'bg-green-900 border-green-700';
  const textColor = isHarmful ? 'text-red-300' : 'text-green-300';

  return (
    <div className={`mt-6 p-4 border rounded-lg ${colorClass} transition-all duration-300`}>
      <h3 className="font-bold text-lg mb-2">Analysis Complete</h3>
      <div className="flex justify-between items-center">
        <span className={`font-semibold ${textColor}`}>
          {isHarmful ? 'Potentially Harmful' : 'Looks Safe'}
        </span>
        <span className="text-sm font-mono bg-gray-700 px-2 py-1 rounded">{confidence}% Confidence</span>
      </div>
    </div>
  );
};

export default ModerationResult;
