# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T14:22:29.509037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.6334` n `232`; crypto_major avg `-0.5196` n `8`; equity avg `-0.0771` n `134`; fx avg `-0.0167` n `6`; index avg `-0.0103` n `26`; metal avg `-0.01` n `20`; unknown avg `145.8216` n `792`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.5128` n `232`; crypto_major avg `-0.4321` n `8`; equity avg `-0.1675` n `134`; fx avg `0.0031` n `6`; index avg `-0.0408` n `26`; metal avg `-0.0179` n `20`; unknown avg `149.4394` n `774`
- 4h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.5347` n `232`; crypto_major avg `-0.5602` n `8`; equity avg `-0.2085` n `134`; fx avg `-0.0115` n `6`; index avg `-0.0542` n `26`; metal avg `-0.0245` n `20`; unknown avg `226.6408` n `720`
- 24h: commodity avg `0.1153` n `12`; crypto_alt avg `1.3009` n `232`; crypto_major avg `0.8488` n `8`; equity avg `0.2622` n `134`; fx avg `-0.0356` n `6`; index avg `0.0447` n `26`; metal avg `-0.0096` n `20`; unknown avg `1.3576` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
