# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T22:37:24.619166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.0666` n `230`; crypto_major avg `-0.0799` n `8`; equity avg `0.0247` n `103`; fx avg `-0.0057` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0176` n `784`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.315` n `230`; crypto_major avg `-0.378` n `8`; equity avg `0.168` n `103`; fx avg `0.011` n `6`; index avg `0.0236` n `25`; metal avg `-0.0341` n `20`; unknown avg `0.252` n `784`
- 4h: commodity avg `-0.06` n `12`; crypto_alt avg `-0.3401` n `230`; crypto_major avg `-0.5523` n `8`; equity avg `0.5521` n `103`; fx avg `0.0536` n `6`; index avg `0.1042` n `25`; metal avg `0.1203` n `20`; unknown avg `0.1007` n `784`
- 24h: commodity avg `0.0157` n `12`; crypto_alt avg `0.0984` n `230`; crypto_major avg `-0.2088` n `8`; equity avg `2.1831` n `103`; fx avg `-0.26` n `6`; index avg `0.1299` n `25`; metal avg `-0.2856` n `20`; unknown avg `0.003` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
