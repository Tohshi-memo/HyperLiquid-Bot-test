# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T12:22:28.719948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.1622` n `238`; crypto_major avg `0.1038` n `8`; equity avg `-0.0245` n `156`; fx avg `-0.007` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0056` n `20`; unknown avg `0.0805` n `1260`
- 1h: commodity avg `-0.0146` n `13`; crypto_alt avg `0.0868` n `238`; crypto_major avg `0.1725` n `8`; equity avg `0.0004` n `156`; fx avg `-0.0027` n `6`; index avg `0.0009` n `27`; metal avg `-0.0039` n `20`; unknown avg `19.5532` n `1248`
- 4h: commodity avg `0.0322` n `13`; crypto_alt avg `0.4364` n `238`; crypto_major avg `0.4009` n `8`; equity avg `-0.0011` n `156`; fx avg `-0.0012` n `6`; index avg `-0.0072` n `27`; metal avg `0.0274` n `20`; unknown avg `20.0957` n `1218`
- 24h: commodity avg `-0.1661` n `13`; crypto_alt avg `0.6488` n `238`; crypto_major avg `-0.4666` n `8`; equity avg `-1.106` n `156`; fx avg `-0.0511` n `6`; index avg `-0.0972` n `27`; metal avg `-0.2019` n `20`; unknown avg `3.5043` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
