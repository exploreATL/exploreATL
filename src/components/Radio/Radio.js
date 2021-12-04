import { Radio, Space, Row, Col } from "antd";

function RadioComponent({ chooseAtl, atl }) {
  return (
    <>
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
                  Downtown Atlanta is the central business district of Atlanta,
                  Georgia, United States. The largest of the city's three
                  commercial districts, it is the location of many corporate or
                  regional headquarters; city, county, state and federal
                  government facilities; Georgia State University; sporting
                  venues; and most of Atlanta's tourist attractions.{" "}
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
                  Midtown is a busy commercial area and a vibrant arts hub. The
                  High Museum of Art shows world-renowned works in a striking
                  modern building, while Margaret Mitchell House offers tours of
                  the former home of the “Gone With the Wind” author. Peachtree
                  Street is a hotspot for comedy, bars and big-name shops, with
                  eating options ranging from street food to fine dining. Large,
                  leafy Piedmont Park offers walking trails.{" "}
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
                  Sandy Springs is a city in northern Fulton County, Georgia and
                  an inner ring suburb of Atlanta. The city’s population was
                  108,080 at the 2020 census, making it Georgia's
                  seventh-largest city. It is the site of several corporate
                  headquarters, including UPS, Newell Brands, Inspire Brands,
                  Cox Communications, and Mercedes-Benz USA's corporate offices.{" "}
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
                  Johns Creek is a city in Fulton County, Georgia, United
                  States. According to the 2010 U.S. Census, the population was
                  76,728. The city is a northeastern suburb of Atlanta.{" "}
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
                  Norcross is a city in Gwinnett County, Georgia, United States.
                  The population as of the 2010 census was 9,116, while in 2018
                  the estimated population was 16,563. It is included in the
                  Atlanta-Sandy Springs-Marietta metropolitan statistical area.{" "}
                </div>
              </div>
            </Col>
          </Row>
        </Space>
      </Radio.Group>
    </>
  );
}

export default RadioComponent;
