import "./App.scss";
import { TextBoxView } from "./text-box-view/text-box-view";

input_sentences = [""];
output_sentences = [];

function append

function App() {
  return (
    <div id="home-container">
      <h1>Welcome to the Sentencer</h1>
      <div id="home-sub-header">Enter the lines you want to process:</div>
      <div id="home-role-buttons-container">
        <TextBoxView></TextBoxView>
      </div>
    </div>
  );
}

export default App;
