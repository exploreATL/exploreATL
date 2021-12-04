import "./App.css";
import { useState, useEffect } from "react";
import { Radio, Button, PageHeader, Checkbox, Input, Card, Row } from "antd";
import {
  CarOutlined,
  CompassOutlined,
  SearchOutlined,
} from "@ant-design/icons";
import RadioComponent from "./components/Radio/Radio";
import BackButton from "./components/BackButton/BackButton";
import Title from "./components/Title/Title";

function App() {
  // place is the variable that stores the nearby places;
  // atl represents the ATL location user chooses
  // explore is the number of explored places
  const { TextArea } = Input;
  const args = JSON.parse(document.getElementById("data").text);
  const [place, setPlace] = useState([]);
  const [showList, setShowList] = useState(true);
  const [atl, setAtl] = useState("downtown atlanta");
  const [type, setType] = useState("restaurant");
  const [explore, setExplore] = useState(0);
  const [been, setBeen] = useState([false, false, false, false, false]);
  const [note, setNote] = useState("");

  //Set the name of ATL location
  const chooseAtl = (e) => {
    setAtl(e.target.value);
  };

  //Set the type of nearby locations
  const ChooseType = (e) => {
    setType(e.target.value);
  };

  // Show the nearby locations
  const submit_nearby = () => {
    setShowList(false);
  };

  // Fetch data of nearby places after user chooses the location
  useEffect(() => {
    async function fetchData() {
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
          for (let i = 0; i < 3; i++) {
            places_info[i]["visited"] = places_visit[i];
          }
          setPlace(places_info);
          console.log(place);
        });
    }
    fetchData();
  }, [atl, type]);

  // Add the number of explored places
  const clickVisited = (e) => {
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
        review: note,
      }),
    });
  };

  //Go back to the ATL location selection page
  const goback = () => {
    setShowList(true);
    setExplore(0);
  };

  return (
    <>
      <PageHeader
        className="site-page-header"
        title="ExploreATL"
        subTitle={`Explore the Atlanta city, welcome ${args.username}`}
      />
      {showList ? (
        <>
          <div className="chooseAtl">
            <div className="choose_title">
              <CarOutlined />
              <span>Start from choosing a location:</span>
              <div className="underline"></div>
            </div>
            <div className="radio">
              <RadioComponent chooseAtl={chooseAtl} atl={atl}></RadioComponent>
            </div>
          </div>
          <div className="choose_title type">
            <CompassOutlined />
            <span>Choose the type of nearby locations:</span>
            <div className="underline"></div>
          </div>
          <div>
            <Radio.Group
              defaultValue="restaurant"
              size="large"
              onChange={ChooseType}
            >
              <Radio.Button value="restaurant">Restaurant</Radio.Button>
              <Radio.Button value="museum">Museum</Radio.Button>
              <Radio.Button value="park">Park</Radio.Button>
              <Radio.Button value="store">Store</Radio.Button>
              <Radio.Button value="library">Library</Radio.Button>
            </Radio.Group>
          </div>
          <Button
            onClick={submit_nearby}
            type="primary"
            className="submit_button"
            icon={<SearchOutlined />}
          >
            Submit!
          </Button>
        </>
      ) : (
        <>
          <div className="nearby_list">
            <Title type={type} atl={atl}></Title>
            <div className="checklist">
              {place.map(function (item, i) {
                return (
                  <div className="neaby_item">
                    <Card
                      hoverable
                      style={{ width: 500 }}
                      cover={<img src={item["photo_reference"]} />}
                    >
                      <Checkbox
                        onChange={clickVisited}
                        value={i}
                        defaultChecked={item["visited"]}
                      >
                        {item["name"]}
                      </Checkbox>
                    </Card>
                  </div>
                );
              })}
            </div>
            <div className="note">
              <div className="choose_title nearby_title">
                <span>Write your review here:</span>
                <div className="underline"></div>
              </div>
              <TextArea
                size="large"
                placeholder="Write down your experience in the place..."
                allowClear
                autoSize={{ minRows: 3, maxRows: 6 }}
                onChange={getNote}
              />
            </div>
            <Row>
              <Button
                onClick={submit_visit}
                type="primary"
                className="nearby_submit"
              >
                Submit!
              </Button>
            </Row>
            <Row>
              <BackButton goback={goback}></BackButton>
            </Row>
          </div>
        </>
      )}
    </>
  );
}

export default App;
