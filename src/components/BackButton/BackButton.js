export default function BackButton({ goback }) {
  return (
    <div onClick={goback} className="submit_div" data-testid="test-1">
      Go back to choose ATL locations
    </div>
  );
}
