# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T08:37:28.178475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `-0.0318` n `239`; crypto_major avg `-0.0812` n `8`; equity avg `-0.0694` n `161`; fx avg `0.0036` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0177` n `20`; unknown avg `0.0603` n `1262`
- 1h: commodity avg `0.1065` n `13`; crypto_alt avg `-0.149` n `239`; crypto_major avg `-0.1177` n `8`; equity avg `-0.0214` n `161`; fx avg `0.0304` n `6`; index avg `0.0038` n `27`; metal avg `0.0276` n `20`; unknown avg `15.3648` n `1238`
- 4h: commodity avg `0.4008` n `13`; crypto_alt avg `-0.2166` n `239`; crypto_major avg `-0.2882` n `8`; equity avg `-0.4799` n `161`; fx avg `0.08` n `6`; index avg `-0.0764` n `27`; metal avg `-0.0628` n `20`; unknown avg `60.7468` n `1204`
- 24h: commodity avg `0.4353` n `13`; crypto_alt avg `-1.4819` n `239`; crypto_major avg `-0.6376` n `8`; equity avg `-0.9035` n `161`; fx avg `-0.0658` n `6`; index avg `-0.1094` n `27`; metal avg `-0.6972` n `20`; unknown avg `17.8869` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
