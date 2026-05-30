# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T16:37:23.250688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2508` n `12`; crypto_alt avg `0.2161` n `228`; crypto_major avg `0.2671` n `8`; equity avg `-0.0481` n `69`; fx avg `0.0` n `6`; index avg `0.0437` n `23`; metal avg `-0.0023` n `18`; unknown avg `0.1261` n `421`
- 1h: commodity avg `-0.4526` n `12`; crypto_alt avg `0.4122` n `228`; crypto_major avg `0.5169` n `8`; equity avg `-0.1397` n `69`; fx avg `-0.0122` n `6`; index avg `-0.0396` n `23`; metal avg `0.012` n `18`; unknown avg `1.1525` n `421`
- 4h: commodity avg `-0.308` n `12`; crypto_alt avg `0.3815` n `228`; crypto_major avg `0.8925` n `8`; equity avg `-0.011` n `69`; fx avg `-0.0019` n `6`; index avg `0.0072` n `23`; metal avg `-0.0069` n `18`; unknown avg `0.3742` n `421`
- 24h: commodity avg `0.1656` n `12`; crypto_alt avg `0.6039` n `228`; crypto_major avg `1.6214` n `8`; equity avg `0.7119` n `69`; fx avg `0.0123` n `6`; index avg `0.1285` n `23`; metal avg `-0.2902` n `18`; unknown avg `1.1326` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
