import "./text-box-view.scss";
import { Component } from "react";

export class TextBoxView extends Component {
  constructor(props) {
    super(props);
  }

  update = (e) => {
    let newValue = e.target.value;
    this.props.update(newValue, this.props.itemIndex);
  };

  render() {
    return (
      <div className="text-box-view-container">
        {!this.props.isDisabled && (
          <div className="text-box-view-container">
            <input
              type="text"
              className="text-box-view-input"
              onChange={this.update}
              value={this.props.text}
            />
            <span
              onClick={() => {
                this.props.add("");
              }}
              className="text-box-view-btn"
            >
              +
            </span>
            <span
              onClick={() => {
                this.props.remove(this.props.itemIndex);
              }}
              className="text-box-view-btn"
            >
              -
            </span>
          </div>
        )}
        {this.props.isDisabled && (
          <div className="text-box-view-container">
            <input
              type="text"
              className="text-box-view-input"
              value={this.props.text}
            />
          </div>
        )}
      </div>
    );
  }
}
