# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T21:07:48.994317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0727` n `12`; crypto_alt avg `-0.1442` n `230`; crypto_major avg `-0.2536` n `8`; equity avg `0.0409` n `108`; fx avg `0.0058` n `6`; index avg `0.022` n `25`; metal avg `0.031` n `20`; unknown avg `0.1656` n `782`
- 1h: commodity avg `0.0908` n `12`; crypto_alt avg `0.0758` n `230`; crypto_major avg `-0.1455` n `8`; equity avg `0.0527` n `108`; fx avg `-0.0072` n `6`; index avg `0.0337` n `25`; metal avg `0.0136` n `20`; unknown avg `0.1229` n `782`
- 4h: commodity avg `0.0761` n `12`; crypto_alt avg `0.0171` n `230`; crypto_major avg `0.0085` n `8`; equity avg `-0.8675` n `108`; fx avg `0.0089` n `6`; index avg `-0.0802` n `25`; metal avg `0.0343` n `20`; unknown avg `-0.1025` n `782`
- 24h: commodity avg `0.0202` n `12`; crypto_alt avg `0.4944` n `230`; crypto_major avg `0.6446` n `8`; equity avg `-0.6381` n `108`; fx avg `-0.0556` n `6`; index avg `-0.0869` n `25`; metal avg `0.8022` n `20`; unknown avg `0.7225` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
