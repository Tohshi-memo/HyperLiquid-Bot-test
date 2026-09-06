# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T21:52:24.333913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0408` n `232`; crypto_major avg `-0.0959` n `8`; equity avg `0.0186` n `134`; fx avg `0.0065` n `6`; index avg `0.0019` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.0105` n `793`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.4397` n `232`; crypto_major avg `0.1172` n `8`; equity avg `0.0426` n `134`; fx avg `0.0179` n `6`; index avg `0.003` n `26`; metal avg `-0.0366` n `20`; unknown avg `5.8921` n `787`
- 4h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.8498` n `232`; crypto_major avg `0.4671` n `8`; equity avg `0.1331` n `134`; fx avg `0.0234` n `6`; index avg `0.0241` n `26`; metal avg `-0.0082` n `20`; unknown avg `151.9045` n `755`
- 24h: commodity avg `-0.0287` n `12`; crypto_alt avg `1.3065` n `232`; crypto_major avg `0.4148` n `8`; equity avg `0.3582` n `134`; fx avg `0.0205` n `6`; index avg `0.0191` n `26`; metal avg `-0.0502` n `20`; unknown avg `151.1539` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
