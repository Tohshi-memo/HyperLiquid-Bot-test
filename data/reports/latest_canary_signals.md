# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T06:37:28.409672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `13`; crypto_alt avg `0.0564` n `239`; crypto_major avg `0.147` n `8`; equity avg `0.1998` n `162`; fx avg `0.015` n `6`; index avg `0.019` n `27`; metal avg `-0.1085` n `20`; unknown avg `0.2453` n `1261`
- 1h: commodity avg `0.1994` n `13`; crypto_alt avg `-0.1908` n `239`; crypto_major avg `-0.1757` n `8`; equity avg `-0.1857` n `162`; fx avg `0.0263` n `6`; index avg `-0.0115` n `27`; metal avg `-0.1271` n `20`; unknown avg `0.209` n `1241`
- 4h: commodity avg `0.2768` n `13`; crypto_alt avg `-1.1877` n `239`; crypto_major avg `-1.0638` n `8`; equity avg `-1.397` n `162`; fx avg `-0.0354` n `6`; index avg `-0.1552` n `27`; metal avg `-0.1719` n `20`; unknown avg `0.1349` n `1225`
- 24h: commodity avg `-0.1519` n `13`; crypto_alt avg `-0.3454` n `239`; crypto_major avg `0.601` n `8`; equity avg `-0.4173` n `162`; fx avg `-0.0506` n `6`; index avg `-0.0416` n `27`; metal avg `0.0968` n `20`; unknown avg `0.8006` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
