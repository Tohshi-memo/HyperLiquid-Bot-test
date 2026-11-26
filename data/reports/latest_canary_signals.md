# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T04:37:22.512084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `0.0079` n `239`; crypto_major avg `-0.0037` n `8`; equity avg `0.1327` n `168`; fx avg `0.0028` n `6`; index avg `0.0106` n `27`; metal avg `0.0822` n `20`; unknown avg `0.1223` n `1267`
- 1h: commodity avg `0.0211` n `13`; crypto_alt avg `0.1004` n `239`; crypto_major avg `0.3018` n `8`; equity avg `0.3519` n `168`; fx avg `-0.0232` n `6`; index avg `0.039` n `27`; metal avg `0.1391` n `20`; unknown avg `2.9449` n `1251`
- 4h: commodity avg `0.0916` n `13`; crypto_alt avg `0.354` n `239`; crypto_major avg `0.5355` n `8`; equity avg `0.3335` n `168`; fx avg `-0.0393` n `6`; index avg `0.0287` n `27`; metal avg `0.2669` n `20`; unknown avg `161.9447` n `1245`
- 24h: commodity avg `0.7235` n `13`; crypto_alt avg `3.6308` n `239`; crypto_major avg `3.2855` n `8`; equity avg `2.6949` n `168`; fx avg `0.0082` n `6`; index avg `0.2116` n `27`; metal avg `0.7125` n `20`; unknown avg `771.9808` n `1015`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2066`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
