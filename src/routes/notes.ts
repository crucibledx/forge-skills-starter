import {Router} from 'express'
import {z} from 'zod'

import {db} from '../database.js'

const notesRouter = Router()

const CreateNote = z.object({
  title: z.string().min(1),
  content: z.string().default(''),
  folder_id: z.number().int().optional(),
})

const UpdateNote = z.object({
  title: z.string().min(1).optional(),
  content: z.string().optional(),
  folder_id: z.number().int().nullable().optional(),
})

notesRouter.get('/', (_req, res) => {
  const notes = db.prepare('SELECT * FROM notes ORDER BY updated_at DESC').all()
  res.json(notes)
})

notesRouter.post('/', (req, res) => {
  const parsed = CreateNote.safeParse(req.body)
  if (!parsed.success) {
    res.status(400).json({error: parsed.error.flatten()})
    return
  }

  const {title, content, folder_id} = parsed.data
  const result = db
    .prepare('INSERT INTO notes (title, content, folder_id) VALUES (?, ?, ?)')
    .run(title, content, folder_id ?? null)

  const note = db.prepare('SELECT * FROM notes WHERE id = ?').get(result.lastInsertRowid)
  res.status(201).json(note)
})

notesRouter.get('/:id', (req, res) => {
  const note = db.prepare('SELECT * FROM notes WHERE id = ?').get(req.params.id)
  if (!note) {
    res.status(404).json({error: 'Note not found'})
    return
  }
  res.json(note)
})

notesRouter.put('/:id', (req, res) => {
  const existing = db.prepare('SELECT * FROM notes WHERE id = ?').get(req.params.id)
  if (!existing) {
    res.status(404).json({error: 'Note not found'})
    return
  }

  const parsed = UpdateNote.safeParse(req.body)
  if (!parsed.success) {
    res.status(400).json({error: parsed.error.flatten()})
    return
  }

  const {title, content, folder_id} = parsed.data
  db.prepare(`
    UPDATE notes
    SET title = COALESCE(?, title),
        content = COALESCE(?, content),
        folder_id = COALESCE(?, folder_id),
        updated_at = datetime('now')
    WHERE id = ?
  `).run(title ?? null, content ?? null, folder_id ?? null, req.params.id)

  const note = db.prepare('SELECT * FROM notes WHERE id = ?').get(req.params.id)
  res.json(note)
})

notesRouter.delete('/:id', (req, res) => {
  const result = db.prepare('DELETE FROM notes WHERE id = ?').run(req.params.id)
  if (result.changes === 0) {
    res.status(404).json({error: 'Note not found'})
    return
  }
  res.status(204).end()
})

export {notesRouter}
