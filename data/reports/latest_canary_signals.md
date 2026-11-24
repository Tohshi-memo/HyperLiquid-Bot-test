# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T09:52:27.316604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2132` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.033` n `13`; crypto_alt avg `-0.1449` n `239`; crypto_major avg `-0.0429` n `8`; equity avg `-0.0551` n `166`; fx avg `0.0218` n `6`; index avg `-0.0111` n `27`; metal avg `0.0513` n `20`; unknown avg `-0.1126` n `1264`
- 1h: commodity avg `0.1596` n `13`; crypto_alt avg `-0.9172` n `239`; crypto_major avg `-0.6859` n `8`; equity avg `-0.9873` n `166`; fx avg `0.0635` n `6`; index avg `-0.0993` n `27`; metal avg `-0.062` n `20`; unknown avg `158.5591` n `1260`
- 4h: commodity avg `0.2162` n `13`; crypto_alt avg `-1.9143` n `239`; crypto_major avg `-1.4425` n `8`; equity avg `-1.9508` n `166`; fx avg `0.0872` n `6`; index avg `-0.2293` n `27`; metal avg `-0.2146` n `20`; unknown avg `332.9076` n `1200`
- 24h: commodity avg `-0.6762` n `13`; crypto_alt avg `-0.7741` n `239`; crypto_major avg `-0.921` n `8`; equity avg `1.6602` n `166`; fx avg `-0.1409` n `6`; index avg `0.3993` n `27`; metal avg `-0.3599` n `20`; unknown avg `329.6941` n `1144`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
