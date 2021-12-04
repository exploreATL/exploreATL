export default function Title({ type, atl }) {
  return (
    <div className="choose_title nearby_title" data-testid="test-2">
      <span>
        Nearby {type} of {atl}:
      </span>
      <div className="underline"></div>
    </div>
  );
}
