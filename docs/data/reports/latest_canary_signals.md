# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T05:07:33.449894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `0.1048` n `232`; crypto_major avg `-0.0384` n `8`; equity avg `-0.1867` n `134`; fx avg `-0.0151` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0141` n `20`; unknown avg `3.6145` n `795`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `0.233` n `232`; crypto_major avg `0.0589` n `8`; equity avg `-0.2951` n `134`; fx avg `0.016` n `6`; index avg `-0.069` n `26`; metal avg `-0.0436` n `20`; unknown avg `2.5365` n `773`
- 4h: commodity avg `0.0826` n `12`; crypto_alt avg `-0.2668` n `232`; crypto_major avg `-0.5347` n `8`; equity avg `0.0457` n `134`; fx avg `-0.03` n `6`; index avg `0.0253` n `26`; metal avg `0.0915` n `20`; unknown avg `0.316` n `767`
- 24h: commodity avg `0.1104` n `12`; crypto_alt avg `0.5474` n `232`; crypto_major avg `-0.9923` n `8`; equity avg `0.4623` n `134`; fx avg `-0.2813` n `6`; index avg `0.1439` n `26`; metal avg `0.385` n `20`; unknown avg `7464.1371` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
