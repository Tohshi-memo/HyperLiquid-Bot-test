# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T00:22:25.250589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.213` n `230`; crypto_major avg `-0.1585` n `8`; equity avg `-0.41` n `107`; fx avg `-0.0102` n `6`; index avg `-0.0679` n `25`; metal avg `-0.0281` n `20`; unknown avg `0.1204` n `780`
- 1h: commodity avg `0.1939` n `12`; crypto_alt avg `-0.0921` n `230`; crypto_major avg `-0.1305` n `8`; equity avg `-0.3103` n `107`; fx avg `0.0239` n `6`; index avg `-0.0325` n `25`; metal avg `0.0486` n `20`; unknown avg `-0.0321` n `780`
- 4h: commodity avg `0.1559` n `12`; crypto_alt avg `-0.4179` n `230`; crypto_major avg `-0.7426` n `8`; equity avg `0.005` n `107`; fx avg `0.0605` n `6`; index avg `0.0266` n `25`; metal avg `0.0743` n `20`; unknown avg `0.2995` n `780`
- 24h: commodity avg `0.1112` n `12`; crypto_alt avg `0.2565` n `230`; crypto_major avg `0.0926` n `8`; equity avg `1.6639` n `107`; fx avg `-0.1906` n `6`; index avg `0.1923` n `25`; metal avg `-0.1505` n `20`; unknown avg `0.0509` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
