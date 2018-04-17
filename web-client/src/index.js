import React from 'react'
import {render} from 'react-dom'

import {Provider} from 'react-redux'
import {createStore} from 'redux'
import reducer from './reducer'

import {BrowserRouter as Router} from 'react-router-dom'
import Base from './Base'
import registerServiceWorker from './registerServiceWorker'

render(<Provider store={createStore(reducer)}><Router><Base/></Router></Provider>,
    document.getElementById('root'))
registerServiceWorker()
