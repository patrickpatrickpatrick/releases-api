import { connect } from 'react-redux';
import { itemsFetchData } from '../actions/items';
import React, { Component } from 'react';

class Videos extends Component {
    componentDidMount() {
        document.title = 'label | videos'
        this.props.fetchData('http://127.0.0.1:8000/videos.json')
    }

    render() {
        if (this.props.hasErrored) {
            return <p>Error fetching videos.</p>
        }

        if (this.props.isLoading) {
            return <p>Fetching videos...</p>
        }

        return (
            <ul>
                {this.props.videos.map((video) => (
                    <li key={video.id}>
                        {video.name}
                    </li>
                ))}
            </ul>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        videos: state.items,
        hasErrored: state.itemsHasErrored,
        isLoading: state.itemsIsLoading
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        fetchData: (url) => dispatch(itemsFetchData(url))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Videos);