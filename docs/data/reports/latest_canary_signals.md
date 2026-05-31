# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T22:07:19.638752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.7351` n `12`; crypto_alt avg `-0.134` n `228`; crypto_major avg `-0.1375` n `8`; equity avg `-0.0108` n `69`; fx avg `-0.001` n `6`; index avg `-0.0852` n `23`; metal avg `-0.3275` n `18`; unknown avg `0.0038` n `421`
- 1h: commodity avg `0.7788` n `12`; crypto_alt avg `0.5161` n `228`; crypto_major avg `0.2623` n `8`; equity avg `-0.0234` n `69`; fx avg `0.0009` n `6`; index avg `0.1172` n `23`; metal avg `-0.2713` n `18`; unknown avg `-0.0203` n `421`
- 4h: commodity avg `0.5721` n `12`; crypto_alt avg `1.1761` n `228`; crypto_major avg `0.6254` n `8`; equity avg `0.0646` n `69`; fx avg `-0.0236` n `6`; index avg `0.1411` n `23`; metal avg `-0.2994` n `18`; unknown avg `0.7302` n `421`
- 24h: commodity avg `1.1592` n `12`; crypto_alt avg `0.3963` n `228`; crypto_major avg `0.4446` n `8`; equity avg `0.8265` n `69`; fx avg `-0.04` n `6`; index avg `0.3038` n `23`; metal avg `-0.4325` n `18`; unknown avg `0.9917` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3017`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
