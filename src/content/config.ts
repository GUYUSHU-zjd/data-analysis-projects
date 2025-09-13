import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date().optional(),
    pubDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string().default('朱捷登'),
  }),
});

const projectsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date().optional(),
    pubDate: z.coerce.date().optional(),
    tools: z.array(z.string()).default([]),
    category: z.string().optional(),
    github_url: z.string().url().or(z.literal('')).optional(),
    githubUrl: z.string().url().or(z.literal('')).optional(),
    demo_url: z.string().url().or(z.literal('')).optional(),
    demoUrl: z.string().url().or(z.literal('')).optional(),
    image: z.string().optional(),
    featured: z.boolean().optional().default(false),
    author: z.string().optional(),
  }),
});

export const collections = {
  'blog': blogCollection,
  'projects': projectsCollection,
};