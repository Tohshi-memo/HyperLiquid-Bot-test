# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T12:52:26.655355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0302` n `230`; crypto_major avg `0.0379` n `8`; equity avg `0.0115` n `102`; fx avg `0.0007` n `6`; index avg `0.0036` n `25`; metal avg `-0.0409` n `20`; unknown avg `0.0066` n `785`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.0203` n `8`; equity avg `0.1489` n `102`; fx avg `0.013` n `6`; index avg `0.0102` n `25`; metal avg `-0.2665` n `20`; unknown avg `-0.0029` n `785`
- 4h: commodity avg `-0.2412` n `12`; crypto_alt avg `0.2127` n `230`; crypto_major avg `0.349` n `8`; equity avg `-1.0917` n `102`; fx avg `-0.0335` n `6`; index avg `-0.1729` n `25`; metal avg `-0.3527` n `20`; unknown avg `0.2984` n `784`
- 24h: commodity avg `-0.3099` n `12`; crypto_alt avg `-0.7001` n `230`; crypto_major avg `-0.0112` n `8`; equity avg `-0.8184` n `102`; fx avg `-0.2124` n `6`; index avg `-0.1826` n `25`; metal avg `-0.432` n `20`; unknown avg `1.3063` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
