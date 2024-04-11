import { Component } from "react";
import "./App.scss";
import { TextBoxView } from "./text-box-view/text-box-view";
import { AIService } from "./services/ai-service";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      inputSentences: [""],
      outputSentences: []
    };
  }

  addLine = (line) => {
    let updatedInputSentences = this.state.inputSentences;
    updatedInputSentences.push(line);
    this.setState({
      inputSentences: updatedInputSentences
    });
  };

  updateLine = (newText, itemIndex) => {
    let updatedInputSentences = this.state.inputSentences;
    updatedInputSentences[itemIndex] = newText;
    this.setState({
      inputSentences: updatedInputSentences
    });
  };

  removeLine = (itemIndex) => {
    let updatedInputSentences = this.state.inputSentences;
    updatedInputSentences.splice(itemIndex, 1);
    this.setState({
      inputSentences: updatedInputSentences
    });
  };

  requestProcessing = () => {
    AIService.getPersonalityTypes(this.state.inputSentences).then(
      (response) => {
        response.json().then((result) => {
          this.setState({
            outputSentences: result.prediction
          });
        });
      }
    );
  };

  render() {
    return (
      <div id="home-container">
        <h1>SenTensor</h1>
        <div id="home-sub-header">Enter the lines you want to process:</div>
        <div className="home-text-box-container">
          {this.state.inputSentences.map((line, index) => {
            return (
              <TextBoxView
                key={"inputLine" + index}
                text={line}
                itemIndex={index}
                add={this.addLine}
                remove={this.removeLine}
                update={this.updateLine}
                isDisabled={false}
              ></TextBoxView>
            );
          })}
        </div>
        <div onClick={this.requestProcessing} className="home-process-btn">
          Process
        </div>
        <div className="home-text-box-container">
          {this.state.outputSentences.map((line, index) => {
            return (
              <TextBoxView
                key={"inputLine" + index}
                text={line}
                isDisabled={true}
              ></TextBoxView>
            );
          })}
        </div>
      </div>
    );
  }
}
