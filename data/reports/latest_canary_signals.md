# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T03:52:24.199065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1004` n `13`; crypto_alt avg `0.1314` n `239`; crypto_major avg `0.3303` n `8`; equity avg `0.4868` n `165`; fx avg `0.0042` n `6`; index avg `0.0165` n `27`; metal avg `0.1562` n `20`; unknown avg `0.958` n `1262`
- 1h: commodity avg `0.0388` n `13`; crypto_alt avg `0.1694` n `239`; crypto_major avg `0.6476` n `8`; equity avg `0.617` n `165`; fx avg `0.0125` n `6`; index avg `0.0372` n `27`; metal avg `-0.0532` n `20`; unknown avg `57.4286` n `1258`
- 4h: commodity avg `0.0187` n `13`; crypto_alt avg `-1.228` n `239`; crypto_major avg `-0.3083` n `8`; equity avg `-0.4465` n `165`; fx avg `0.0193` n `6`; index avg `-0.0643` n `27`; metal avg `-0.4626` n `20`; unknown avg `1.4095` n `1252`
- 24h: commodity avg `0.0602` n `13`; crypto_alt avg `-2.7904` n `239`; crypto_major avg `-1.2842` n `8`; equity avg `-5.191` n `165`; fx avg `0.0523` n `6`; index avg `-0.4379` n `27`; metal avg `-1.4144` n `20`; unknown avg `5.7292` n `1173`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
