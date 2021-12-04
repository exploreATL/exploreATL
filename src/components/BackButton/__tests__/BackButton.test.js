import React from "react";
import "@testing-library/jest-dom";
import BackButton from "../BackButton";
import { render, screen } from "@testing-library/react";

it("renders without crashing", () => {
  render(<BackButton></BackButton>);
  const ButtonElement = screen.queryByTestId("test-1");
  expect(ButtonElement).toBeInTheDocument();
});
