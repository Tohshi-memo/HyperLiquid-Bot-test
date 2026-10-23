# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T11:07:31.546050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `-0.2319` n `237`; crypto_major avg `-0.19` n `8`; equity avg `0.0064` n `152`; fx avg `0.0062` n `6`; index avg `0.0339` n `26`; metal avg `0.0689` n `20`; unknown avg `0.8086` n `1231`
- 1h: commodity avg `-0.0208` n `13`; crypto_alt avg `-0.1982` n `237`; crypto_major avg `-0.2357` n `8`; equity avg `-0.2261` n `152`; fx avg `0.0173` n `6`; index avg `0.001` n `26`; metal avg `0.0868` n `20`; unknown avg `0.0534` n `1231`
- 4h: commodity avg `0.1043` n `13`; crypto_alt avg `-0.3684` n `237`; crypto_major avg `-0.3602` n `8`; equity avg `-0.585` n `152`; fx avg `-0.0539` n `6`; index avg `-0.0814` n `26`; metal avg `0.0668` n `20`; unknown avg `0.7081` n `1151`
- 24h: commodity avg `0.3795` n `13`; crypto_alt avg `-0.2293` n `237`; crypto_major avg `-0.1054` n `8`; equity avg `-1.5853` n `152`; fx avg `0.0019` n `6`; index avg `-0.1685` n `26`; metal avg `-0.3047` n `20`; unknown avg `49.5559` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
