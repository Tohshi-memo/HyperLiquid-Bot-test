# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T12:07:25.276242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.1308` n `230`; crypto_major avg `0.0921` n `8`; equity avg `-0.1744` n `113`; fx avg `-0.0052` n `6`; index avg `-0.0199` n `25`; metal avg `0.0579` n `20`; unknown avg `-0.001` n `787`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.0614` n `230`; crypto_major avg `-0.1502` n `8`; equity avg `-0.1064` n `113`; fx avg `-0.0145` n `6`; index avg `-0.0089` n `25`; metal avg `0.0074` n `20`; unknown avg `0.4911` n `787`
- 4h: commodity avg `-0.2012` n `12`; crypto_alt avg `-0.0676` n `230`; crypto_major avg `-0.6114` n `8`; equity avg `-0.012` n `113`; fx avg `-0.0124` n `6`; index avg `0.0123` n `25`; metal avg `0.2361` n `20`; unknown avg `0.5194` n `787`
- 24h: commodity avg `-0.4856` n `12`; crypto_alt avg `-0.9082` n `230`; crypto_major avg `-0.9313` n `8`; equity avg `0.9509` n `113`; fx avg `0.0007` n `6`; index avg `0.1224` n `25`; metal avg `-0.4564` n `20`; unknown avg `0.6451` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
