# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T19:37:33.789693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.0754` n `228`; crypto_major avg `-0.2058` n `8`; equity avg `-0.0825` n `88`; fx avg `0.0013` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0385` n `20`; unknown avg `0.2334` n `763`
- 1h: commodity avg `-0.1092` n `12`; crypto_alt avg `-0.206` n `228`; crypto_major avg `-0.2668` n `8`; equity avg `-0.0758` n `88`; fx avg `0.0038` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0491` n `20`; unknown avg `0.1864` n `763`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.8059` n `228`; crypto_major avg `-0.2231` n `8`; equity avg `-0.6488` n `88`; fx avg `0.0105` n `6`; index avg `-0.1327` n `25`; metal avg `-0.1807` n `20`; unknown avg `0.1723` n `761`
- 24h: commodity avg `-0.6014` n `12`; crypto_alt avg `1.3229` n `228`; crypto_major avg `1.3178` n `8`; equity avg `-1.0652` n `88`; fx avg `-0.0055` n `6`; index avg `-0.4595` n `25`; metal avg `0.1807` n `20`; unknown avg `0.6362` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
