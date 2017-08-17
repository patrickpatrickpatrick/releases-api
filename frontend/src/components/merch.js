import { connect } from 'react-redux';
import { itemsFetchData } from '../actions/items';
import React, { Component } from 'react';

class Merch extends Component {
    componentDidMount() {
        document.title = 'label | merch'
        this.props.fetchData('http://127.0.0.1:8000/merch.json')
    }

    render() {
        if (this.props.hasErrored) {
            return <p>Error fetching merch.</p>
        }

        if (this.props.isLoading) {
            return <p>Fetching merch...</p>
        }

        return (
            <ul>
                {this.props.merch.map((merch) => (
                    <li key={merch.id}>
                        {merch.name}
                    </li>
                ))}
            </ul>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        merch: state.items,
        hasErrored: state.itemsHasErrored,
        isLoading: state.itemsIsLoading
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        fetchData: (url) => dispatch(itemsFetchData(url))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Merch);