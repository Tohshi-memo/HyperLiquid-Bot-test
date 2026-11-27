# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T10:52:28.669035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0896` n `13`; crypto_alt avg `0.0975` n `239`; crypto_major avg `0.0796` n `8`; equity avg `0.1557` n `168`; fx avg `-0.0149` n `6`; index avg `0.0114` n `27`; metal avg `0.0171` n `20`; unknown avg `0.4493` n `1261`
- 1h: commodity avg `-0.1042` n `13`; crypto_alt avg `-0.0234` n `239`; crypto_major avg `0.0026` n `8`; equity avg `0.179` n `168`; fx avg `-0.0137` n `6`; index avg `0.0349` n `27`; metal avg `-0.0366` n `20`; unknown avg `160.0898` n `1255`
- 4h: commodity avg `-0.2425` n `13`; crypto_alt avg `0.0652` n `239`; crypto_major avg `0.2973` n `8`; equity avg `0.3979` n `168`; fx avg `-0.0566` n `6`; index avg `-0.0011` n `27`; metal avg `0.0856` n `20`; unknown avg `410.275` n `1123`
- 24h: commodity avg `0.15` n `13`; crypto_alt avg `2.2305` n `239`; crypto_major avg `3.3959` n `8`; equity avg `4.5319` n `168`; fx avg `-0.1071` n `6`; index avg `0.3686` n `27`; metal avg `1.3389` n `20`; unknown avg `66.8084` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
