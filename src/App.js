import "./App.css";
import { useState, useEffect } from "react";
import {
  Radio,
  Button,
  Space,
  PageHeader,
  Checkbox,
  Select,
  Input,
} from "antd";
import { CarOutlined } from "@ant-design/icons";

function App() {
  // place is the variable that stores the nearby places;
  // atl represents the ATL location user chooses
  // explore is the number of explored places
  const { Option } = Select;
  const { TextArea } = Input;
  const [place, setPlace] = useState([]);
  const [showList, setShowList] = useState(true);
  const [atl, setAtl] = useState("downtown atlanta");
  const [type, setType] = useState("restaurant");
  const [explore, setExplore] = useState(0);
  const [been, setBeen] = useState([false, false, false, false, false]);
  const [note, setNote] = useState("");

  const chooseAtl = (e) => {
    setAtl(e.target.value);
  };

  function chooseType(value) {
    setType(value);
    console.log(type);
  }

  // Fetch data of nearby places after user chooses the location
  const submit_nearby = () => {
    fetch("/nearby", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        location: atl,
        type: type,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        var places_info = data["nearby_places"];
        var places_visit = data["visited"];
        console.log(places_info);
        console.log(places_visit);
        for (let i = 0; i < 5; i++) {
          places_info[i]["visited"] = places_visit[i];
        }
        console.log(places_info);
        setPlace(places_info);
        console.log(place);
        if (place.length > 0) {
          setShowList(false);
        }
      });
  };

  // Add the number of explored places
  const clickVisited = (e) => {
    console.log(e.target.value);
    var set_been = been;
    set_been[e.target.value] = e.target.checked;
    setBeen(set_been);
    if (e.target.checked) {
      setExplore((prevExplore) => prevExplore + 1);
    } else {
      setExplore((prevExplore) => prevExplore - 1);
    }
  };

  //Get the user input note
  const getNote = (e) => {
    setNote(e.target.value);
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
    place.forEach(function (item) {
      delete item.visited;
    });
    console.log(place);
    fetch("/explore", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        places: place,
        been: been,
        review: note
      }),
    });
  };

  const goback = () => {
    setShowList(true);
    setExplore(0);
    setPlace([]);
    setBeen([false, false, false, false, false]);
  };

  return (
    <>
      <PageHeader
        className="site-page-header"
        title="ExploreATL"
        subTitle="Explore the Atlanta city"
      />
      {showList ? (
        <>
          <div className="chooseAtl">
            <div>
              <CarOutlined style={{ margin: "5px" }} />
              <span className="choose_title">
                Start from choosing one location:
              </span>
            </div>
            <div className="radio">
              <Radio.Group onChange={chooseAtl} value={atl}>
                <Space direction="vertical">
                  <Radio value={"downtown atlanta"}>Downtown</Radio>
                  <Radio value={"midtown atlanta"}>Midtown</Radio>
                  <Radio value={"sandy springs"}>Sandy Springs</Radio>
                  <Radio value={"johns creek"}>Johns Creek</Radio>
                  <Radio value={"norcross atlanta"}>Norcross</Radio>
                </Space>
              </Radio.Group>
            </div>
          </div>
          <div className="choose_title">
            Choose the type of nearby locations:
          </div>
          <div>
            <Select
              defaultValue="restaurant"
              style={{ width: 120 }}
              onChange={chooseType}
            >
              <Option value="restaurant">Restaurant</Option>
              <Option value="museum">Museum</Option>
              <Option value="park">Park</Option>
              <Option value="store">Store</Option>
              <Option value="library">Library</Option>
            </Select>
          </div>
          <Button
            onClick={submit_nearby}
            type="primary"
            className="submit_button"
          >
            Submit!
          </Button>
        </>
      ) : (
        <>
          <div className="nearby_list">
            <div className="nearby_title">
              Nearby {type} of {atl}:
            </div>
            <div className="checklist">
              {place.map(function (item, i) {
                return (
                  <div>
                    <Checkbox
                      onChange={clickVisited}
                      value={i}
                      defaultChecked={item["visited"]}
                    >
                      {item["name"]}
                    </Checkbox>
                  </div>
                );
              })}
            </div>
            <div className="note">
              <div className="nearby_title">Write your note about {atl}</div>
              <TextArea
                placeholder="Write down your experience in the place..."
                allowClear
                onChange={getNote}
              />
            </div>
            <Button
              onClick={submit_visit}
              type="primary"
              className="submit_button"
            >
              Submit!
            </Button>
            <Button onClick={goback}>Go back to choose ATL locations</Button>
          </div>
        </>
      )}
    </>
  );
}

export default App;
