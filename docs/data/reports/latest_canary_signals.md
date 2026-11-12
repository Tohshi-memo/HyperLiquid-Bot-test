# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T00:07:32.736976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `0.1411` n `239`; crypto_major avg `0.0277` n `8`; equity avg `-0.0166` n `161`; fx avg `-0.0497` n `6`; index avg `0.0203` n `27`; metal avg `-0.0483` n `20`; unknown avg `0.1423` n `1252`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.3295` n `239`; crypto_major avg `0.2501` n `8`; equity avg `-0.0144` n `161`; fx avg `-0.0618` n `6`; index avg `-0.007` n `27`; metal avg `-0.1108` n `20`; unknown avg `1.6015` n `1250`
- 4h: commodity avg `0.0557` n `13`; crypto_alt avg `-1.1621` n `239`; crypto_major avg `-1.0089` n `8`; equity avg `-1.5873` n `161`; fx avg `-0.0863` n `6`; index avg `-0.14` n `27`; metal avg `-0.1884` n `20`; unknown avg `2.5477` n `1206`
- 24h: commodity avg `0.2399` n `13`; crypto_alt avg `-1.2173` n `239`; crypto_major avg `-0.2067` n `8`; equity avg `2.4154` n `161`; fx avg `-0.1939` n `6`; index avg `0.2656` n `27`; metal avg `-0.2832` n `20`; unknown avg `2.7882` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
