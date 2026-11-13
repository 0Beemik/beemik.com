/**
 * Every project on the site. The home page tiles and each project page header read from here,
 * so adding a project starts with one entry in this list.
 */
export type Status = 'live' | 'soon' | 'building';

export type Project = {
  slug: string;
  name: string;
  tagline: string;
  blurb: string;
  status: Status;
  statusLabel: string;
  /** Accent color for the tile glow and the project page. */
  accent: string;
  icon?: string;
  emoji?: string;
  image?: string;
  /** Where the tile goes. Omit for a tile that isn't clickable yet. */
  href?: string;
  external?: boolean;
  tags: string[];
};

export const projects: Project[] = [
  {
    slug: 'familychores',
    name: 'Family Chores',
    tagline: 'Do chores. Earn coins. Win the week.',
    blurb: 'A chore board for the whole family, with coins, a sibling marketplace and badges. Syncs over home Wi-Fi.',
    status: 'soon',
    statusLabel: 'Coming soon · Google Play',
    accent: '#6c5ce7',
    icon: '/img/familychores/icon.png',
    image: '/img/familychores/board.webp',
    href: '/familychores/',
    tags: ['Android', 'Family', 'Free'],
  },
  {
    slug: 'bobblob',
    name: 'BobBlob',
    tagline: 'Run. Jump. Squish. SPLAT!',
    blurb: 'A one-tap runner starring a little jelly blob. 14 worlds, 10,000 metres, and new looks to unlock the farther you go.',
    status: 'soon',
    statusLabel: 'Coming soon · Google Play',
    accent: '#e0468f',
    icon: '/img/bobblob/icon.png',
    image: '/img/bobblob/tile.webp',
    href: '/bobblob/',
    tags: ['Game', 'Android', 'Free'],
  },
  {
    slug: 'careerdna',
    name: 'CareerDNA',
    tagline: 'AI career intelligence.',
    blurb: "Career intelligence for people who'd rather build than guess. A few minutes a week, a clear path forward.",
    status: 'live',
    statusLabel: 'Live',
    accent: '#3b82f6',
    emoji: '🧬',
    image: '/img/careerdna/dashboard.webp',
    href: '/careerdna/',
    tags: ['Web', 'AI', 'Careers'],
  },
  {
    slug: 'grumps',
    name: 'Grumps!',
    tagline: 'A grumpy old man vs. the weather.',
    blurb: "A 16-bit dodge game. It's raining cats and dogs (then pianos), and Grumps just wants to get to the market.",
    status: 'soon',
    statusLabel: 'Coming soon · Google Play',
    accent: '#f59e0b',
    icon: '/img/grumps/icon.png',
    image: '/img/grumps/tile.webp',
    href: '/grumps/',
    tags: ['Game', 'Android', 'Free'],
  },
  {
    slug: 'flyers',
    name: 'Better Flip',
    tagline: 'Grocery flyers, meal plans, savings.',
    blurb: 'Every Canadian grocery flyer in one place, with shopping lists and meal ideas built from the deals.',
    status: 'building',
    statusLabel: 'Working title',
    accent: '#10b981',
    emoji: '🛒',
    tags: ['Mobile', 'Canada'],
  },
];

export const bySlug = (slug: string) => projects.find((p) => p.slug === slug)!;
