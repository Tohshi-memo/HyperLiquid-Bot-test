# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T08:22:34.625450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1137` n `13`; crypto_alt avg `0.0656` n `239`; crypto_major avg `-0.0263` n `8`; equity avg `0.1673` n `165`; fx avg `-0.0226` n `6`; index avg `0.0245` n `27`; metal avg `0.0226` n `20`; unknown avg `2.8889` n `1256`
- 1h: commodity avg `-0.1983` n `13`; crypto_alt avg `0.322` n `239`; crypto_major avg `0.1545` n `8`; equity avg `0.6501` n `165`; fx avg `-0.0298` n `6`; index avg `0.1064` n `27`; metal avg `0.2535` n `20`; unknown avg `4.2512` n `1204`
- 4h: commodity avg `-0.2943` n `13`; crypto_alt avg `0.6568` n `239`; crypto_major avg `0.4351` n `8`; equity avg `0.0253` n `165`; fx avg `-0.0332` n `6`; index avg `0.0881` n `27`; metal avg `0.3671` n `20`; unknown avg `-0.015` n `1182`
- 24h: commodity avg `-0.2884` n `13`; crypto_alt avg `-2.902` n `239`; crypto_major avg `-2.472` n `8`; equity avg `-6.6183` n `165`; fx avg `-0.0695` n `6`; index avg `-0.5854` n `27`; metal avg `-1.3799` n `20`; unknown avg `15.2432` n `1159`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
