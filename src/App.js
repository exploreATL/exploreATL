import "./App.css";
import { useState } from "react";
import { Radio, Button, Space, PageHeader, Checkbox } from "antd";
import { CarOutlined } from "@ant-design/icons";

function App() {
  // place is the variable that stores the nearby places;
  // value represents the ATL location user chooses
  // explore is the number of explored places
  const [place, setPlace] = useState([]);
  const [value, setValue] = useState("downtown atlanta");
  const [showList, setShowList] = useState(false);
  const [explore, setExplore] = useState(0);

  const onChange = (e) => {
    setValue(e.target.value);
  };

  // Add the number of explored places
  const visited = (e) => {
    console.log(e.target.value);
    if (e.target.checked) {
      setExplore((prevExplore) => prevExplore + 1);
    } else {
      setExplore((prevExplore) => prevExplore - 1);
    }
  };

  // Fetch data of nearby places after user chooses the location
  const submit = () => {
    nearPlace();
  };

  // Function called after user chooses their visted places
  const submit_visit = () => {
    const not_visted = place.length - explore;
    if (not_visted === 0) {
      alert("Congratulations! You've explored the location!");
    } else if (not_visted === 1) {
      alert(`You still have ${not_visted} nearby place to explore!`);
    } else {
      alert(`You still have ${not_visted} nearby places to explore!`);
    }
  };

  // The function to fetch nearby places from back-end
  const nearPlace = () => {
    fetch("/nearby", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        location: value,
        type: "restaurant",
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setPlace(data["nearby_places"]);
        console.log(place);
        if (place.length > 0) {
          setShowList(true);
        }
      });
  };

  return (
    <>
      <PageHeader className="page_header" title="ExploreATL" />
      {showList ? (
        <>
          <div className="nearby_list">
            <div className="nearby_title">Nearby Restaurants of {value}:</div>
            {place.map(function (item, i) {
              return (
                <div>
                  <Checkbox onChange={visited} value={item["name"]}>
                    {item["name"]}
                  </Checkbox>
                </div>
              );
            })}
            <Button
              onClick={submit_visit}
              type="primary"
              className="submit_button"
            >
              Submit!
            </Button>
          </div>
        </>
      ) : (
        <div className="chooseAtl">
          <div>
            <CarOutlined style={{ margin: "5px" }} />
            <span className="chooseLoc">Start from choosing one location:</span>
          </div>
          <div className="radio">
            <Radio.Group onChange={onChange} value={value}>
              <Space direction="vertical">
                <Radio value={"downtown atlanta"}>Downtown</Radio>
                <Radio value={"midtown atlanta"}>Midtown</Radio>
                <Radio value={"sandy springs"}>Sandy Springs</Radio>
                <Radio value={"johns creek"}>Johns Creek</Radio>
                <Radio value={"norcross atlanta"}>Norcross</Radio>
              </Space>
            </Radio.Group>
          </div>
          <Button onClick={submit} type="primary" className="submit_button">
            Submit!
          </Button>
        </div>
      )}
    </>
  );
}

export default App;
