import express from 'express'

import {healthRouter} from './routes/health.js'
import {notesRouter} from './routes/notes.js'
import {foldersRouter} from './routes/folders.js'

const app = express()
const PORT = process.env.PORT ?? 3000

app.use(express.json())

app.use('/health', healthRouter)
app.use('/notes', notesRouter)
app.use('/folders', foldersRouter)

app.listen(PORT, () => {
  console.log(`Notes API running on port ${PORT}`)
})

export {app}
