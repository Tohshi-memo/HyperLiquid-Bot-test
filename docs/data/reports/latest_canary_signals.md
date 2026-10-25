# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T16:22:30.769379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.2774` n `237`; crypto_major avg `-0.1262` n `8`; equity avg `-0.0474` n `152`; fx avg `-0.0032` n `6`; index avg `-0.0052` n `26`; metal avg `0.0013` n `20`; unknown avg `15.5703` n `1240`
- 1h: commodity avg `-0.0361` n `13`; crypto_alt avg `0.0177` n `237`; crypto_major avg `0.0675` n `8`; equity avg `0.0803` n `152`; fx avg `-0.006` n `6`; index avg `0.0062` n `26`; metal avg `0.007` n `20`; unknown avg `0.1689` n `1234`
- 4h: commodity avg `-0.0814` n `13`; crypto_alt avg `0.3929` n `237`; crypto_major avg `0.2441` n `8`; equity avg `0.304` n `152`; fx avg `-0.0158` n `6`; index avg `0.0454` n `26`; metal avg `0.0475` n `20`; unknown avg `-0.1698` n `1225`
- 24h: commodity avg `-0.2208` n `13`; crypto_alt avg `1.1245` n `237`; crypto_major avg `1.8665` n `8`; equity avg `0.9835` n `152`; fx avg `0.0124` n `6`; index avg `0.167` n `26`; metal avg `0.1577` n `20`; unknown avg `19.1262` n `1081`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
