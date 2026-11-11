# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T10:22:37.720309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `13`; crypto_alt avg `0.3416` n `239`; crypto_major avg `0.3268` n `8`; equity avg `-0.0212` n `161`; fx avg `0.0141` n `6`; index avg `-0.0205` n `27`; metal avg `-0.0452` n `20`; unknown avg `0.5737` n `1261`
- 1h: commodity avg `0.1179` n `13`; crypto_alt avg `0.5645` n `239`; crypto_major avg `0.4055` n `8`; equity avg `0.1462` n `161`; fx avg `0.024` n `6`; index avg `0.0015` n `27`; metal avg `0.1` n `20`; unknown avg `13.8597` n `1255`
- 4h: commodity avg `0.2341` n `13`; crypto_alt avg `0.2979` n `239`; crypto_major avg `0.1698` n `8`; equity avg `0.3778` n `161`; fx avg `-0.0249` n `6`; index avg `-0.0408` n `27`; metal avg `0.0803` n `20`; unknown avg `0.6624` n `1221`
- 24h: commodity avg `0.9663` n `13`; crypto_alt avg `-0.4503` n `239`; crypto_major avg `-1.2917` n `8`; equity avg `2.0515` n `161`; fx avg `-0.1976` n `6`; index avg `0.1949` n `27`; metal avg `0.2426` n `20`; unknown avg `1.6577` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
