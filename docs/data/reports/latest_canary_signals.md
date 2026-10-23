# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T11:52:40.930052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `13`; crypto_alt avg `0.1999` n `237`; crypto_major avg `0.2206` n `8`; equity avg `0.2099` n `152`; fx avg `-0.0074` n `6`; index avg `0.0385` n `26`; metal avg `0.0265` n `20`; unknown avg `0.061` n `1233`
- 1h: commodity avg `-0.1388` n `13`; crypto_alt avg `0.1744` n `237`; crypto_major avg `0.1741` n `8`; equity avg `0.0495` n `152`; fx avg `-0.0204` n `6`; index avg `0.0413` n `26`; metal avg `0.0615` n `20`; unknown avg `1.0088` n `1231`
- 4h: commodity avg `-0.0585` n `13`; crypto_alt avg `0.0102` n `237`; crypto_major avg `0.137` n `8`; equity avg `-0.3303` n `152`; fx avg `-0.0506` n `6`; index avg `-0.0466` n `26`; metal avg `0.0717` n `20`; unknown avg `0.7562` n `1151`
- 24h: commodity avg `0.2136` n `13`; crypto_alt avg `0.107` n `237`; crypto_major avg `0.3169` n `8`; equity avg `-1.5552` n `152`; fx avg `-0.0385` n `6`; index avg `-0.1838` n `26`; metal avg `-0.2543` n `20`; unknown avg `49.7313` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.211`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
