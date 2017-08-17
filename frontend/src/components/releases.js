import { connect } from 'react-redux';
import { itemsFetchData } from '../actions/items';
import React, { Component } from 'react';

class Releases extends Component {
    componentDidMount() {
        document.title = 'label | releases'
        this.props.fetchData('http://127.0.0.1:8000/releases.json')
    }

    render() {
        if (this.props.hasErrored) {
            return <p>Error fetching releases.</p>
        }

        if (this.props.isLoading) {
            return <p>Fetching releases...</p>
        }

        return (
            <div>
                {this.props.releases.sort(
                    (a, b) => {
                        return new Date(b.release_date) - new Date(a.release_date)
                    }    
                ).map((release) => (
                    <div className={'release'}>
                        <h5>{release.release_number}</h5>
                        <h5>{release.artist} - {release.name}</h5>
                        <h5><i>{release.medium}</i></h5>
                        <div className={'release-embed'} key={release.id} dangerouslySetInnerHTML={{__html: release.embed}}/>
                    </div>
                ))}
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        releases: state.items,
        hasErrored: state.itemsHasErrored,
        isLoading: state.itemsIsLoading
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        fetchData: (url) => dispatch(itemsFetchData(url))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Releases);