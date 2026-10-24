# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T11:37:33.301452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `-0.0435` n `237`; crypto_major avg `-0.0119` n `8`; equity avg `-0.0152` n `152`; fx avg `-0.0142` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.0969` n `1230`
- 1h: commodity avg `0.0568` n `13`; crypto_alt avg `-0.3693` n `237`; crypto_major avg `-0.1252` n `8`; equity avg `-0.0514` n `152`; fx avg `-0.0143` n `6`; index avg `-0.0104` n `26`; metal avg `-0.015` n `20`; unknown avg `0.0955` n `1230`
- 4h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.3664` n `237`; crypto_major avg `-0.6252` n `8`; equity avg `-0.1441` n `152`; fx avg `-0.0107` n `6`; index avg `-0.031` n `26`; metal avg `-0.0383` n `20`; unknown avg `119.0951` n `1196`
- 24h: commodity avg `0.3024` n `13`; crypto_alt avg `-2.6401` n `237`; crypto_major avg `-2.0442` n `8`; equity avg `-0.3677` n `152`; fx avg `-0.0037` n `6`; index avg `0.0087` n `26`; metal avg `-0.2067` n `20`; unknown avg `193.939` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
