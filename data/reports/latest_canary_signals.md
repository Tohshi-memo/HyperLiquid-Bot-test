# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T05:22:27.491041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `13`; crypto_alt avg `0.1741` n `238`; crypto_major avg `0.0584` n `8`; equity avg `0.1387` n `155`; fx avg `0.0019` n `6`; index avg `0.06` n `27`; metal avg `0.032` n `20`; unknown avg `-0.1659` n `1236`
- 1h: commodity avg `-0.0544` n `13`; crypto_alt avg `0.9602` n `238`; crypto_major avg `0.8278` n `8`; equity avg `0.6157` n `155`; fx avg `0.0011` n `6`; index avg `0.153` n `27`; metal avg `0.1047` n `20`; unknown avg `0.7398` n `1218`
- 4h: commodity avg `-0.1172` n `13`; crypto_alt avg `-1.2253` n `238`; crypto_major avg `-0.5394` n `8`; equity avg `0.0055` n `155`; fx avg `0.0074` n `6`; index avg `0.1049` n `27`; metal avg `-0.213` n `20`; unknown avg `1.2801` n `1196`
- 24h: commodity avg `-0.1209` n `13`; crypto_alt avg `-1.5838` n `238`; crypto_major avg `-0.8874` n `8`; equity avg `-0.6837` n `154`; fx avg `0.0168` n `6`; index avg `0.0646` n `27`; metal avg `-0.1129` n `20`; unknown avg `33.9635` n `974`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
