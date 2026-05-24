# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T23:52:16.372614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `12`; crypto_alt avg `0.1275` n `228`; crypto_major avg `0.0975` n `8`; equity avg `0.0318` n `67`; fx avg `-0.0451` n `6`; index avg `-0.0099` n `23`; metal avg `-0.2075` n `18`; unknown avg `0.0349` n `396`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `0.3993` n `228`; crypto_major avg `0.4813` n `8`; equity avg `0.0896` n `67`; fx avg `-0.0465` n `6`; index avg `-0.0491` n `23`; metal avg `0.2872` n `18`; unknown avg `0.1298` n `396`
- 4h: commodity avg `-0.7971` n `12`; crypto_alt avg `-0.205` n `228`; crypto_major avg `0.1324` n `8`; equity avg `-0.0128` n `67`; fx avg `0.0194` n `6`; index avg `-0.1178` n `23`; metal avg `1.3286` n `18`; unknown avg `-0.1325` n `396`
- 24h: commodity avg `0.6087` n `12`; crypto_alt avg `-1.4995` n `228`; crypto_major avg `0.7603` n `8`; equity avg `0.3519` n `67`; fx avg `0.0428` n `6`; index avg `-0.1643` n `23`; metal avg `1.0829` n `18`; unknown avg `-0.1782` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
