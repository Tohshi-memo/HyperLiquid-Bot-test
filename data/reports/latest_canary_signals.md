# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T06:22:26.288112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0495` n `13`; crypto_alt avg `0.0658` n `237`; crypto_major avg `0.068` n `8`; equity avg `0.0214` n `152`; fx avg `0.006` n `6`; index avg `0.0061` n `26`; metal avg `0.0036` n `20`; unknown avg `0.0642` n `1231`
- 1h: commodity avg `0.0714` n `13`; crypto_alt avg `-0.5545` n `237`; crypto_major avg `-0.4994` n `8`; equity avg `-0.1771` n `152`; fx avg `-0.002` n `6`; index avg `-0.0051` n `26`; metal avg `-0.041` n `20`; unknown avg `1.4506` n `1205`
- 4h: commodity avg `0.0001` n `13`; crypto_alt avg `-0.4254` n `237`; crypto_major avg `-0.3243` n `8`; equity avg `-0.0806` n `152`; fx avg `0.0089` n `6`; index avg `0.0138` n `26`; metal avg `-0.0139` n `20`; unknown avg `1.0181` n `1193`
- 24h: commodity avg `0.0877` n `13`; crypto_alt avg `-1.584` n `237`; crypto_major avg `-0.3174` n `8`; equity avg `-0.0888` n `152`; fx avg `-0.0296` n `6`; index avg `0.0009` n `26`; metal avg `-0.0926` n `20`; unknown avg `18.7396` n `1054`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
