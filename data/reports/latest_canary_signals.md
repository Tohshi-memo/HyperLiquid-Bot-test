# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T18:22:29.162223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `0.1595` n `237`; crypto_major avg `0.0353` n `8`; equity avg `-0.024` n `152`; fx avg `0.0026` n `6`; index avg `-0.005` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.2361` n `1229`
- 1h: commodity avg `0.0577` n `13`; crypto_alt avg `0.0419` n `237`; crypto_major avg `-0.2173` n `8`; equity avg `-0.0592` n `152`; fx avg `0.002` n `6`; index avg `0.0215` n `26`; metal avg `0.0371` n `20`; unknown avg `-0.3151` n `1229`
- 4h: commodity avg `0.0676` n `13`; crypto_alt avg `0.7687` n `237`; crypto_major avg `0.2722` n `8`; equity avg `0.276` n `152`; fx avg `-0.0208` n `6`; index avg `0.0953` n `26`; metal avg `0.113` n `20`; unknown avg `-0.56` n `1195`
- 24h: commodity avg `0.3908` n `13`; crypto_alt avg `1.4649` n `237`; crypto_major avg `0.9733` n `8`; equity avg `1.3261` n `152`; fx avg `-0.1156` n `6`; index avg `0.0303` n `26`; metal avg `-0.2046` n `20`; unknown avg `-0.4414` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
