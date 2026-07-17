(function () {
  const search = document.getElementById('search');
  const diffFilter = document.getElementById('diff-filter');
  const cards = Array.from(document.querySelectorAll('.card'));
  const sections = Array.from(document.querySelectorAll('.section'));
  const navLinks = Array.from(document.querySelectorAll('.nav-link'));
  const noResult = document.getElementById('no-result');
  const problems = window.__PROBLEMS__ || {};

  function esc(text) {
    return String(text == null ? '' : text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderStatement(statement) {
    if (!statement) return '<p class="muted">（暂无详细描述）</p>';
    const paras = statement.split(/\n\n+/).map((p) => p.trim()).filter(Boolean);
    if (paras.length > 1) return paras.map((p) => `<p>${esc(p)}</p>`).join('');
    return `<p>${esc(statement)}</p>`;
  }

  function renderList(items, ordered) {
    if (!items || !items.length) return '';
    const tag = ordered ? 'ol' : 'ul';
    const cls = ordered ? 'step-list' : 'example-list';
    const lis = items.map((x) => `<li>${esc(x)}</li>`).join('');
    return `<${tag} class="${cls}">${lis}</${tag}>`;
  }

  function renderNotes(notes) {
    if (!notes || !notes.length) return '';
    const lis = notes.map((note, i) =>
      `<li><span class="note-idx">${i + 1}</span>${esc(note)}</li>`
    ).join('');
    return `<div class="code-notes"><div class="code-notes-head">代码说明</div><ol class="note-list">${lis}</ol></div>`;
  }

  function renderBody(id, data) {
    const examples = data.examples && data.examples.length
      ? `<div class="panel panel-examples"><div class="panel-head"><span class="panel-icon">📋</span><h4>示例</h4></div><div class="panel-body">${renderList(data.examples, false)}</div></div>`
      : '';
    const steps = data.steps && data.steps.length
      ? `<div class="panel panel-approach"><div class="panel-head"><span class="panel-icon">💡</span><h4>解题思路</h4></div><div class="panel-body">${renderList(data.steps, true)}</div></div>`
      : '';
    const complexity = data.complexity
      ? `<div class="complexity">复杂度：${esc(data.complexity)}</div>`
      : '';
    return `
      <div class="panel panel-problem">
        <div class="panel-head"><span class="panel-icon">📖</span><h4>题目描述</h4></div>
        <div class="panel-body problem-body">${renderStatement(data.statement)}</div>
      </div>
      ${examples}
      ${steps}
      <details class="panel panel-code">
        <summary class="panel-head"><span class="panel-icon">🐍</span><h4>Python 实现</h4><span class="toggle-hint">点击展开</span></summary>
        <div class="panel-body">
          <div class="code-toolbar">
            <button type="button" class="copy-btn" data-copy-id="${esc(id)}">复制代码</button>
          </div>
          <div class="code-mount" data-code-id="${esc(id)}"><p class="muted">展开后加载代码…</p></div>
          ${renderNotes(data.codeNotes)}
          ${complexity}
        </div>
      </details>`;
  }

  function ensureBody(card) {
    const body = card.querySelector('.card-body');
    if (!body || body.dataset.loaded === '1') return;
    const id = card.dataset.id;
    const data = problems[id];
    if (!data) {
      body.innerHTML = '<p class="muted">（暂无详情）</p>';
    } else {
      body.innerHTML = renderBody(id, data);
    }
    body.dataset.loaded = '1';
  }

  function loadCode(id, mount) {
    if (!mount || mount.dataset.loaded === '1') return;
    const data = problems[id];
    if (!data || !data.codeHtml) {
      mount.innerHTML = '<p class="muted">（暂无代码）</p>';
    } else {
      mount.innerHTML = data.codeHtml;
    }
    mount.dataset.loaded = '1';
  }

  function applyFilters() {
    const q = (search.value || '').trim().toLowerCase();
    const diff = diffFilter.value;
    let visible = 0;

    cards.forEach((card) => {
      const hay = [
        card.dataset.title || '',
        card.dataset.lc || '',
        card.dataset.fn || '',
      ].join(' ');
      const matchQ = !q || hay.includes(q);
      const cardDiff = card.dataset.difficulty || 'unset';
      const matchDiff =
        diff === 'all' ||
        (diff === 'unset' ? cardDiff === 'unset' || cardDiff === '' : cardDiff === diff);
      const show = matchQ && matchDiff;
      card.classList.toggle('hidden', !show);
      if (show) visible++;
    });

    sections.forEach((section) => {
      const count = section.querySelectorAll('.card:not(.hidden)').length;
      section.classList.toggle('hidden', count === 0);
      const countEl = section.querySelector('.section-count');
      if (countEl) countEl.textContent = count + ' 题';
      const nav = navLinks.find((a) => a.getAttribute('href') === '#' + section.id);
      if (nav) {
        nav.classList.toggle('hidden', count === 0);
        const badge = nav.querySelector('span');
        if (badge) badge.textContent = String(count);
      }
    });

    noResult.style.display = visible === 0 ? 'block' : 'none';
  }

  document.addEventListener('toggle', (ev) => {
    const t = ev.target;
    if (!(t instanceof HTMLDetailsElement) || !t.open) return;
    if (t.classList.contains('card')) {
      ensureBody(t);
    }
    if (t.classList.contains('panel-code')) {
      const mount = t.querySelector('.code-mount');
      if (mount) loadCode(mount.dataset.codeId, mount);
    }
  }, true);

  document.addEventListener('click', async (ev) => {
    const btn = ev.target.closest('.copy-btn');
    if (!btn) return;
    const id = btn.dataset.copyId;
    const data = problems[id];
    const text = data && data.codeText ? data.codeText : '';
    try {
      await navigator.clipboard.writeText(text);
      btn.textContent = '已复制';
      setTimeout(() => { btn.textContent = '复制代码'; }, 1200);
    } catch (e) {
      btn.textContent = '复制失败';
      setTimeout(() => { btn.textContent = '复制代码'; }, 1200);
    }
  });

  search.addEventListener('input', applyFilters);
  diffFilter.addEventListener('change', applyFilters);
})();
