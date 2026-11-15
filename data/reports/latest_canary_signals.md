# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T16:07:24.879609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `0.1677` n `239`; crypto_major avg `0.1127` n `8`; equity avg `0.0609` n `162`; fx avg `0.0041` n `6`; index avg `0.0083` n `27`; metal avg `0.0162` n `20`; unknown avg `1.5341` n `1252`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.2187` n `239`; crypto_major avg `0.2509` n `8`; equity avg `0.1954` n `162`; fx avg `0.0014` n `6`; index avg `0.0337` n `27`; metal avg `0.0464` n `20`; unknown avg `3.9818` n `1254`
- 4h: commodity avg `-0.0541` n `13`; crypto_alt avg `-0.9195` n `239`; crypto_major avg `-0.8051` n `8`; equity avg `-0.1213` n `162`; fx avg `-0.0072` n `6`; index avg `0.021` n `27`; metal avg `-0.0117` n `20`; unknown avg `319.6227` n `1253`
- 24h: commodity avg `0.0177` n `13`; crypto_alt avg `-1.9158` n `239`; crypto_major avg `-1.3647` n `8`; equity avg `-0.1494` n `162`; fx avg `-0.0161` n `6`; index avg `0.0224` n `27`; metal avg `-0.1459` n `20`; unknown avg `0.3162` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
