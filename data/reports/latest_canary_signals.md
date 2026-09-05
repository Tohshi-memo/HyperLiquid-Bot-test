# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T22:52:25.089572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0651` n `232`; crypto_major avg `-0.0414` n `8`; equity avg `0.0073` n `134`; fx avg `0.0018` n `6`; index avg `-0.0174` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.0686` n `794`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.1606` n `232`; crypto_major avg `-0.2736` n `8`; equity avg `0.0338` n `134`; fx avg `-0.0027` n `6`; index avg `-0.0025` n `26`; metal avg `0.002` n `20`; unknown avg `0.8594` n `792`
- 4h: commodity avg `0.0619` n `12`; crypto_alt avg `0.4704` n `232`; crypto_major avg `-0.4969` n `8`; equity avg `0.0478` n `134`; fx avg `-0.0167` n `6`; index avg `0.011` n `26`; metal avg `-0.0012` n `20`; unknown avg `1.9282` n `770`
- 24h: commodity avg `0.183` n `12`; crypto_alt avg `3.379` n `232`; crypto_major avg `2.4751` n `8`; equity avg `0.2712` n `134`; fx avg `-0.0539` n `6`; index avg `0.0538` n `26`; metal avg `0.0613` n `20`; unknown avg `1281.1452` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
