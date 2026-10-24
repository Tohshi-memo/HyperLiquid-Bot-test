# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T12:37:28.635758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `-0.0498` n `237`; crypto_major avg `0.0637` n `8`; equity avg `-0.011` n `152`; fx avg `-0.0037` n `6`; index avg `0.0033` n `26`; metal avg `0.0038` n `20`; unknown avg `0.1823` n `1230`
- 1h: commodity avg `0.0838` n `13`; crypto_alt avg `0.1122` n `237`; crypto_major avg `0.1928` n `8`; equity avg `0.1609` n `152`; fx avg `0.005` n `6`; index avg `0.0282` n `26`; metal avg `0.0204` n `20`; unknown avg `1.0457` n `1224`
- 4h: commodity avg `0.1282` n `13`; crypto_alt avg `-0.0537` n `237`; crypto_major avg `-0.1253` n `8`; equity avg `0.0975` n `152`; fx avg `-0.0003` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0158` n `20`; unknown avg `118.202` n `1206`
- 24h: commodity avg `0.4052` n `13`; crypto_alt avg `-2.6546` n `237`; crypto_major avg `-1.9705` n `8`; equity avg `-0.0285` n `152`; fx avg `0.0248` n `6`; index avg `0.0721` n `26`; metal avg `-0.1703` n `20`; unknown avg `193.7804` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
