// Sends http:// and www. requests to https://beemik.com, then serves the static site from dist/.
const HOST = 'beemik.com';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const isLocal = url.hostname === 'localhost' || url.hostname === '127.0.0.1';
    if (!isLocal && (url.protocol === 'http:' || url.hostname !== HOST)) {
      url.protocol = 'https:';
      url.hostname = HOST;
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
