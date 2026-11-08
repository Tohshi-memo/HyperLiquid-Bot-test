# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T10:52:26.458543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0677` n `13`; crypto_alt avg `0.1237` n `239`; crypto_major avg `0.0957` n `8`; equity avg `0.0199` n `158`; fx avg `0.0` n `6`; index avg `0.0074` n `27`; metal avg `0.0053` n `20`; unknown avg `-0.0609` n `1262`
- 1h: commodity avg `-0.0377` n `13`; crypto_alt avg `-0.0661` n `239`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0252` n `158`; fx avg `0.0071` n `6`; index avg `0.0132` n `27`; metal avg `-0.001` n `20`; unknown avg `5.1329` n `1256`
- 4h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.0774` n `239`; crypto_major avg `-0.0362` n `8`; equity avg `0.153` n `158`; fx avg `0.0035` n `6`; index avg `0.0078` n `27`; metal avg `0.0168` n `20`; unknown avg `221.0371` n `1160`
- 24h: commodity avg `0.0598` n `13`; crypto_alt avg `-1.3026` n `239`; crypto_major avg `-0.5229` n `8`; equity avg `0.1425` n `158`; fx avg `0.0612` n `6`; index avg `0.0319` n `27`; metal avg `-0.0324` n `20`; unknown avg `5.6232` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
