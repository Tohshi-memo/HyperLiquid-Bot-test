# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T16:22:26.202958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `13`; crypto_alt avg `0.0428` n `239`; crypto_major avg `-0.2225` n `8`; equity avg `-0.1371` n `168`; fx avg `-0.0066` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0443` n `20`; unknown avg `-0.0359` n `1257`
- 1h: commodity avg `0.0623` n `13`; crypto_alt avg `0.584` n `239`; crypto_major avg `0.5408` n `8`; equity avg `0.0916` n `168`; fx avg `0.0044` n `6`; index avg `0.0024` n `27`; metal avg `-0.0151` n `20`; unknown avg `0.4626` n `1245`
- 4h: commodity avg `0.2037` n `13`; crypto_alt avg `-0.2775` n `239`; crypto_major avg `-0.2143` n `8`; equity avg `-0.1546` n `168`; fx avg `0.0044` n `6`; index avg `-0.0316` n `27`; metal avg `0.016` n `20`; unknown avg `-0.4183` n `1241`
- 24h: commodity avg `0.2762` n `13`; crypto_alt avg `4.5416` n `239`; crypto_major avg `3.1164` n `8`; equity avg `6.4664` n `168`; fx avg `0.059` n `6`; index avg `0.5923` n `27`; metal avg `1.3189` n `20`; unknown avg `15.2097` n `1058`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
