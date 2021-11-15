import "./App.css";
import { useState } from "react";
import { Radio, Button, Space, PageHeader, Checkbox } from "antd";
import { CarOutlined } from "@ant-design/icons";

function App() {
  // TODO: Implement your main page as a React component.
  const [place, setPlace] = useState([]);
  const [atlLocation, setAtlLocation] = useState("");
  const [value, setValue] = useState("downtown atlanta");
  const [showList, setShowList] = useState(false);

  const onChange = (e) => {
    setValue(e.target.value);
  };

  const visited = (e) => {
    console.log(e.target.checked);
    console.log(e.target.value);
  };

  const submit = () => {
    setAtlLocation(value);
    nearPlace();
  };

  const submit_visit = () => {};

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
                <Radio value={"buckhead atlanta"}>Buckhead</Radio>
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
