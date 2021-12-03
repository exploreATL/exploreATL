import "./App.css";
import { useState, useEffect } from "react";
import {
  Radio,
  Button,
  Space,
  PageHeader,
  Checkbox,
  Input,
  Card,
  Row,
  Col,
} from "antd";
import {
  CarOutlined,
  CompassOutlined,
  SearchOutlined,
} from "@ant-design/icons";

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
              <Radio.Group onChange={chooseAtl} value={atl}>
                <Space direction="vertical">
                  <Row>
                    <Col span={16}>
                      <img
                        className="atl_img l"
                        alt="Downtown"
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Atlanta_Downtown_July_2010.JPG/1280px-Atlanta_Downtown_July_2010.JPG"
                      />
                    </Col>
                    <Col span={8}>
                      <div className="atl_info r">
                        <div className="atl_option">
                          <Radio value={"downtown atlanta"}>Downtown</Radio>
                        </div>
                        <div className="atl_intro">
                          Downtown Atlanta is the central business district of
                          Atlanta, Georgia, United States. The largest of the
                          city's three commercial districts, it is the location
                          of many corporate or regional headquarters; city,
                          county, state and federal government facilities;
                          Georgia State University; sporting venues; and most of
                          Atlanta's tourist attractions.{" "}
                        </div>
                      </div>
                    </Col>
                  </Row>
                  <Row>
                    <Col span={8}>
                      <div className="atl_info l">
                        <div className="atl_option">
                          <Radio value={"midtown atlanta"}>Midtown</Radio>
                        </div>
                        <div className="atl_intro">
                          Midtown is a busy commercial area and a vibrant arts
                          hub. The High Museum of Art shows world-renowned works
                          in a striking modern building, while Margaret Mitchell
                          House offers tours of the former home of the “Gone
                          With the Wind” author. Peachtree Street is a hotspot
                          for comedy, bars and big-name shops, with eating
                          options ranging from street food to fine dining.
                          Large, leafy Piedmont Park offers walking trails.{" "}
                        </div>
                      </div>
                    </Col>
                    <Col span={16}>
                      <img
                        className="atl_img r"
                        src="https://2486634c787a971a3554-d983ce57e4c84901daded0f67d5a004f.ssl.cf1.rackcdn.com/twelve-hotel-residence/media/cache/Twelve-Midtown-Atlanta-Outdoor-Centennial-Olympic-Park-5b76fc70bff88-914x543.jpg"
                      />
                    </Col>
                  </Row>
                  <Row>
                    <Col span={16}>
                      <img
                        className="atl_img l"
                        alt="Sandy Springs"
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/The_King_and_Queen_towers.jpg/1280px-The_King_and_Queen_towers.jpg"
                      />
                    </Col>
                    <Col span={8}>
                      <div className="atl_info r">
                        <div className="atl_option">
                          <Radio value={"sandy springs"}>Sandy Springs</Radio>
                        </div>
                        <div className="atl_intro">
                          Sandy Springs is a city in northern Fulton County,
                          Georgia and an inner ring suburb of Atlanta. The
                          city’s population was 108,080 at the 2020 census,
                          making it Georgia's seventh-largest city. It is the
                          site of several corporate headquarters, including UPS,
                          Newell Brands, Inspire Brands, Cox Communications, and
                          Mercedes-Benz USA's corporate offices.{" "}
                        </div>
                      </div>
                    </Col>
                  </Row>
                  <Row>
                    <Col span={8}>
                      <div className="atl_info l">
                        <div className="atl_option">
                          <Radio value={"johns creek"}>Johns Creek</Radio>
                        </div>
                        <div className="atl_intro">
                          Johns Creek is a city in Fulton County, Georgia,
                          United States. According to the 2010 U.S. Census, the
                          population was 76,728. The city is a northeastern
                          suburb of Atlanta.{" "}
                        </div>
                      </div>
                    </Col>
                    <Col span={16}>
                      <img
                        className="atl_img r"
                        src="https://i.ytimg.com/vi/8BL908WHz8o/hqdefault.jpg"
                      />
                    </Col>
                  </Row>
                  <Row>
                    <Col span={16}>
                      <img
                        className="atl_img l"
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Holcomb_Bridge_Road%2C_Norcross%2C_GA%2C_March_2017.jpg/1920px-Holcomb_Bridge_Road%2C_Norcross%2C_GA%2C_March_2017.jpg"
                      />
                    </Col>
                    <Col span={8}>
                      <div className="atl_info r">
                        <div className="atl_option">
                          <Radio value={"norcross atlanta"}>Norcross</Radio>
                        </div>
                        <div className="atl_intro">
                          Norcross is a city in Gwinnett County, Georgia, United
                          States. The population as of the 2010 census was
                          9,116, while in 2018 the estimated population was
                          16,563. It is included in the Atlanta-Sandy
                          Springs-Marietta metropolitan statistical area.{" "}
                        </div>
                      </div>
                    </Col>
                  </Row>
                </Space>
              </Radio.Group>
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
            <div className="choose_title nearby_title">
              <span>
                Nearby {type} of {atl}:
              </span>
              <div className="underline"></div>
            </div>
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
              <div onClick={goback} className="submit_div">
                Go back to choose ATL locations
              </div>
            </Row>
          </div>
        </>
      )}
    </>
  );
}

export default App;
