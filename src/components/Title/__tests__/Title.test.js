import React from "react";
import "@testing-library/jest-dom";
import Title from "./../Title";
import { render, screen } from "@testing-library/react";

it("renders without crashing", () => {
  render(<Title></Title>);
  const TitleElement = screen.queryByTestId("test-2");
  expect(TitleElement).toBeInTheDocument();
});
