# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T01:22:24.821288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1021` n `13`; crypto_alt avg `0.4524` n `239`; crypto_major avg `0.3406` n `8`; equity avg `0.0743` n `166`; fx avg `-0.0088` n `6`; index avg `0.022` n `27`; metal avg `0.0662` n `20`; unknown avg `-0.0847` n `1264`
- 1h: commodity avg `-0.0773` n `13`; crypto_alt avg `0.3582` n `239`; crypto_major avg `0.7319` n `8`; equity avg `0.8819` n `166`; fx avg `0.0906` n `6`; index avg `0.0814` n `27`; metal avg `0.0845` n `20`; unknown avg `160.0428` n `1264`
- 4h: commodity avg `-0.0122` n `13`; crypto_alt avg `0.7008` n `239`; crypto_major avg `0.5523` n `8`; equity avg `1.1495` n `166`; fx avg `0.087` n `6`; index avg `0.2122` n `27`; metal avg `0.197` n `20`; unknown avg `47.947` n `1246`
- 24h: commodity avg `-1.1576` n `13`; crypto_alt avg `1.8501` n `239`; crypto_major avg `1.9495` n `8`; equity avg `6.8044` n `166`; fx avg `-0.1559` n `6`; index avg `0.7143` n `27`; metal avg `0.4685` n `20`; unknown avg `254.7138` n `1049`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
