import {Router} from 'express'
import {z} from 'zod'

import {db} from '../database.js'

const foldersRouter = Router()

const CreateFolder = z.object({
  name: z.string().min(1),
})

foldersRouter.get('/', (_req, res) => {
  const folders = db.prepare('SELECT * FROM folders ORDER BY name').all()
  res.json(folders)
})

foldersRouter.post('/', (req, res) => {
  const parsed = CreateFolder.safeParse(req.body)
  if (!parsed.success) {
    res.status(400).json({error: parsed.error.flatten()})
    return
  }

  try {
    const result = db
      .prepare('INSERT INTO folders (name) VALUES (?)')
      .run(parsed.data.name)
    const folder = db.prepare('SELECT * FROM folders WHERE id = ?').get(result.lastInsertRowid)
    res.status(201).json(folder)
  } catch {
    res.status(409).json({error: 'Folder already exists'})
  }
})

export {foldersRouter}
