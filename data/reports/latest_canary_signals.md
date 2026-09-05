# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T03:52:27.531410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.0268` n `232`; crypto_major avg `-0.0085` n `8`; equity avg `0.0113` n `134`; fx avg `0.0027` n `6`; index avg `-0.0238` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.1686` n `790`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.1013` n `232`; crypto_major avg `0.1438` n `8`; equity avg `-0.0236` n `134`; fx avg `0.0116` n `6`; index avg `0.0091` n `26`; metal avg `0.016` n `20`; unknown avg `-0.1027` n `788`
- 4h: commodity avg `0.0128` n `12`; crypto_alt avg `0.6405` n `232`; crypto_major avg `-0.0272` n `8`; equity avg `-0.117` n `134`; fx avg `0.0093` n `6`; index avg `-0.0114` n `26`; metal avg `0.0294` n `20`; unknown avg `0.5188` n `758`
- 24h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0264` n `232`; crypto_major avg `-1.96` n `8`; equity avg `1.1502` n `134`; fx avg `-0.1418` n `6`; index avg `0.1065` n `26`; metal avg `-0.1006` n `20`; unknown avg `0.9157` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
