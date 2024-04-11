import { Component } from "react";

export class TextBoxView extends Component {
    constructor(props) {
        super(props)
    }
    
    render() {
        return (
            <div className="text-box-view-container">
                <input type="text" value={this.props.text} />
                <span onClick={this.props.add} className="text-box-view-btn">+</span>
                <span onClick={this.props.remove} className="text-box-view-btn">-</span>
            </div>
        )
    }
}