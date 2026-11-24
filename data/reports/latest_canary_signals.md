# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T04:37:28.423463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `13`; crypto_alt avg `0.1665` n `239`; crypto_major avg `0.1944` n `8`; equity avg `0.0162` n `166`; fx avg `-0.0044` n `6`; index avg `-0.004` n `27`; metal avg `-0.0572` n `20`; unknown avg `1.4707` n `1264`
- 1h: commodity avg `-0.0614` n `13`; crypto_alt avg `0.8207` n `239`; crypto_major avg `0.7827` n `8`; equity avg `0.0453` n `166`; fx avg `-0.0056` n `6`; index avg `0.0188` n `27`; metal avg `-0.0986` n `20`; unknown avg `1.7434` n `1250`
- 4h: commodity avg `-0.1828` n `13`; crypto_alt avg `0.2959` n `239`; crypto_major avg `0.112` n `8`; equity avg `-0.2747` n `166`; fx avg `0.0094` n `6`; index avg `0.0639` n `27`; metal avg `-0.4921` n `20`; unknown avg `161.4907` n `1246`
- 24h: commodity avg `-1.2954` n `13`; crypto_alt avg `0.937` n `239`; crypto_major avg `0.6452` n `8`; equity avg `4.8805` n `166`; fx avg `-0.2875` n `6`; index avg `0.6735` n `27`; metal avg `-0.0256` n `20`; unknown avg `361.3561` n `1038`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
