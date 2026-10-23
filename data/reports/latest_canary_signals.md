# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T15:52:27.302212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `13`; crypto_alt avg `0.3099` n `237`; crypto_major avg `0.1279` n `8`; equity avg `0.1539` n `152`; fx avg `-0.0009` n `6`; index avg `0.019` n `26`; metal avg `0.0495` n `20`; unknown avg `0.0343` n `1233`
- 1h: commodity avg `0.0616` n `13`; crypto_alt avg `-0.2956` n `237`; crypto_major avg `-0.2774` n `8`; equity avg `-0.1775` n `152`; fx avg `-0.0136` n `6`; index avg `-0.015` n `26`; metal avg `0.059` n `20`; unknown avg `-0.1841` n `1231`
- 4h: commodity avg `0.1347` n `13`; crypto_alt avg `-0.2536` n `237`; crypto_major avg `-0.1392` n `8`; equity avg `0.2765` n `152`; fx avg `0.0353` n `6`; index avg `0.0836` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.5346` n `1161`
- 24h: commodity avg `0.5089` n `13`; crypto_alt avg `0.8973` n `237`; crypto_major avg `0.4235` n `8`; equity avg `0.7142` n `152`; fx avg `-0.0603` n `6`; index avg `0.0203` n `26`; metal avg `-0.2091` n `20`; unknown avg `-0.7064` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
