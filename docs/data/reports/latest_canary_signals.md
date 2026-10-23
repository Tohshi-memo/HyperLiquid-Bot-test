# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T16:52:34.975100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0943` n `13`; crypto_alt avg `0.0195` n `237`; crypto_major avg `-0.0411` n `8`; equity avg `-0.0908` n `152`; fx avg `-0.0051` n `6`; index avg `-0.0196` n `26`; metal avg `0.0072` n `20`; unknown avg `0.2636` n `1225`
- 1h: commodity avg `0.0009` n `13`; crypto_alt avg `0.2922` n `237`; crypto_major avg `0.1014` n `8`; equity avg `-0.1695` n `152`; fx avg `-0.0018` n `6`; index avg `-0.0471` n `26`; metal avg `-0.0433` n `20`; unknown avg `-0.1038` n `1199`
- 4h: commodity avg `0.1054` n `13`; crypto_alt avg `0.1994` n `237`; crypto_major avg `0.2126` n `8`; equity avg `0.6339` n `152`; fx avg `0.0355` n `6`; index avg `0.1241` n `26`; metal avg `-0.0113` n `20`; unknown avg `-0.2045` n `1151`
- 24h: commodity avg `0.3915` n `13`; crypto_alt avg `2.083` n `237`; crypto_major avg `1.5894` n `8`; equity avg `1.4505` n `152`; fx avg `-0.0823` n `6`; index avg `0.0991` n `26`; metal avg `-0.0906` n `20`; unknown avg `-0.5079` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
