# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T20:52:30.417960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.1004` n `230`; crypto_major avg `-0.092` n `8`; equity avg `0.0275` n `102`; fx avg `-0.0244` n `6`; index avg `-0.0312` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0466` n `780`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.003` n `230`; crypto_major avg `-0.02` n `8`; equity avg `-0.3283` n `102`; fx avg `-0.1221` n `6`; index avg `-0.0825` n `25`; metal avg `-0.0375` n `20`; unknown avg `3.5048` n `780`
- 4h: commodity avg `0.1226` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `-0.2162` n `8`; equity avg `-0.2481` n `102`; fx avg `-0.0596` n `6`; index avg `-0.018` n `25`; metal avg `0.1368` n `20`; unknown avg `7.3119` n `780`
- 24h: commodity avg `0.2022` n `12`; crypto_alt avg `-0.6261` n `230`; crypto_major avg `-2.0975` n `8`; equity avg `-0.7868` n `102`; fx avg `0.0899` n `6`; index avg `0.1277` n `25`; metal avg `-0.3366` n `20`; unknown avg `0.2357` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
