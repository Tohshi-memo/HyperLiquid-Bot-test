# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T21:07:28.052338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0349` n `12`; crypto_alt avg `0.398` n `228`; crypto_major avg `0.5407` n `8`; equity avg `0.1057` n `74`; fx avg `0.0115` n `6`; index avg `0.082` n `23`; metal avg `0.0426` n `18`; unknown avg `0.1886` n `517`
- 1h: commodity avg `0.1923` n `12`; crypto_alt avg `0.4128` n `228`; crypto_major avg `0.4208` n `8`; equity avg `0.0804` n `74`; fx avg `-0.0031` n `6`; index avg `0.2387` n `23`; metal avg `0.1002` n `18`; unknown avg `0.0777` n `517`
- 4h: commodity avg `0.1259` n `12`; crypto_alt avg `0.504` n `228`; crypto_major avg `0.7513` n `8`; equity avg `-0.2275` n `74`; fx avg `-0.0199` n `6`; index avg `-0.131` n `23`; metal avg `-0.1824` n `18`; unknown avg `-0.113` n `517`
- 24h: commodity avg `-0.6099` n `12`; crypto_alt avg `3.7159` n `228`; crypto_major avg `4.1981` n `8`; equity avg `2.6171` n `74`; fx avg `-0.2892` n `6`; index avg `1.015` n `23`; metal avg `0.2171` n `18`; unknown avg `-1.9927` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
