# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T00:22:28.272676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `13`; crypto_alt avg `0.2436` n `239`; crypto_major avg `0.2189` n `8`; equity avg `0.0859` n `161`; fx avg `-0.0119` n `6`; index avg `-0.0088` n `27`; metal avg `0.0552` n `20`; unknown avg `1.7423` n `1262`
- 1h: commodity avg `0.0104` n `13`; crypto_alt avg `1.1707` n `239`; crypto_major avg `0.9351` n `8`; equity avg `0.323` n `161`; fx avg `-0.0731` n `6`; index avg `0.0072` n `27`; metal avg `-0.0257` n `20`; unknown avg `1.3643` n `1250`
- 4h: commodity avg `0.037` n `13`; crypto_alt avg `-0.9225` n `239`; crypto_major avg `-0.7927` n `8`; equity avg `-1.5037` n `161`; fx avg `-0.0982` n `6`; index avg `-0.1488` n `27`; metal avg `-0.1336` n `20`; unknown avg `2.6453` n `1206`
- 24h: commodity avg `0.2092` n `13`; crypto_alt avg `-0.9899` n `239`; crypto_major avg `0.0967` n `8`; equity avg `2.6069` n `161`; fx avg `-0.1962` n `6`; index avg `0.2718` n `27`; metal avg `-0.2236` n `20`; unknown avg `2.8532` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
