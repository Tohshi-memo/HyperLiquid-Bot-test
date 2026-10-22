# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T20:06:07.006722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `0.0633` n `237`; crypto_major avg `-0.0306` n `8`; equity avg `0.121` n `151`; fx avg `-0.0043` n `6`; index avg `0.0304` n `26`; metal avg `0.0034` n `20`; unknown avg `44.048` n `1217`
- 1h: commodity avg `-0.0143` n `13`; crypto_alt avg `0.0673` n `237`; crypto_major avg `0.1236` n `8`; equity avg `0.4914` n `151`; fx avg `-0.0127` n `6`; index avg `0.0671` n `26`; metal avg `0.0191` n `20`; unknown avg `76.0818` n `1209`
- 4h: commodity avg `0.2061` n `13`; crypto_alt avg `-0.4025` n `237`; crypto_major avg `-0.6202` n `8`; equity avg `-0.733` n `151`; fx avg `-0.015` n `6`; index avg `-0.0738` n `26`; metal avg `-0.142` n `20`; unknown avg `3.671` n `1207`
- 24h: commodity avg `0.5585` n `13`; crypto_alt avg `-5.2938` n `237`; crypto_major avg `-3.9291` n `8`; equity avg `-5.4933` n `151`; fx avg `-0.1729` n `6`; index avg `-0.649` n `26`; metal avg `-0.9744` n `20`; unknown avg `2.7638` n `926`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
