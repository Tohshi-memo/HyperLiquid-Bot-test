# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T15:07:53.178288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6797` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6727` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `0.0158` n `239`; crypto_major avg `-0.0974` n `8`; equity avg `0.4412` n `165`; fx avg `-0.0155` n `6`; index avg `0.0632` n `27`; metal avg `0.0739` n `20`; unknown avg `20.5396` n `1252`
- 1h: commodity avg `-0.206` n `13`; crypto_alt avg `-0.5556` n `239`; crypto_major avg `-0.8709` n `8`; equity avg `0.2482` n `165`; fx avg `-0.0137` n `6`; index avg `0.0701` n `27`; metal avg `0.043` n `20`; unknown avg `1.2913` n `1258`
- 4h: commodity avg `0.0325` n `13`; crypto_alt avg `-1.3686` n `239`; crypto_major avg `-1.6016` n `8`; equity avg `0.0781` n `165`; fx avg `0.0219` n `6`; index avg `0.0711` n `27`; metal avg `-0.1196` n `20`; unknown avg `360.1386` n `1254`
- 24h: commodity avg `-0.5516` n `13`; crypto_alt avg `-4.8566` n `239`; crypto_major avg `-5.0277` n `8`; equity avg `-7.8612` n `165`; fx avg `-0.0374` n `6`; index avg `-0.6956` n `27`; metal avg `-1.248` n `20`; unknown avg `28.6434` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
