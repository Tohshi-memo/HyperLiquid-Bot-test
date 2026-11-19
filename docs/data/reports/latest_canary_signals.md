# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T14:07:42.865597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0879` n `13`; crypto_alt avg `0.0337` n `239`; crypto_major avg `-0.0222` n `8`; equity avg `0.1064` n `165`; fx avg `0.0164` n `6`; index avg `0.0056` n `27`; metal avg `0.0086` n `20`; unknown avg `-0.0947` n `1259`
- 1h: commodity avg `0.1703` n `13`; crypto_alt avg `-0.079` n `239`; crypto_major avg `-0.0248` n `8`; equity avg `-0.3376` n `165`; fx avg `0.0174` n `6`; index avg `-0.0466` n `27`; metal avg `-0.0551` n `20`; unknown avg `0.0538` n `1263`
- 4h: commodity avg `0.1486` n `13`; crypto_alt avg `0.0771` n `239`; crypto_major avg `0.2384` n `8`; equity avg `-0.0851` n `165`; fx avg `0.0071` n `6`; index avg `-0.047` n `27`; metal avg `-0.2055` n `20`; unknown avg `3.9871` n `1257`
- 24h: commodity avg `0.0636` n `13`; crypto_alt avg `0.4937` n `239`; crypto_major avg `0.5642` n `8`; equity avg `1.0406` n `165`; fx avg `0.0354` n `6`; index avg `0.2829` n `27`; metal avg `-0.3638` n `20`; unknown avg `2.0929` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
