# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T14:11:07.623353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3815` n `12`; crypto_alt avg `-0.6296` n `228`; crypto_major avg `-0.7502` n `8`; equity avg `-1.1023` n `74`; fx avg `0.0042` n `6`; index avg `-0.4311` n `23`; metal avg `-0.391` n `18`; unknown avg `-0.2232` n `547`
- 1h: commodity avg `-0.2274` n `12`; crypto_alt avg `-0.7753` n `228`; crypto_major avg `-1.1231` n `8`; equity avg `-0.918` n `74`; fx avg `-0.0194` n `6`; index avg `-0.4644` n `23`; metal avg `-0.6379` n `18`; unknown avg `-0.3182` n `547`
- 4h: commodity avg `-0.2837` n `12`; crypto_alt avg `0.2257` n `228`; crypto_major avg `-0.8935` n `8`; equity avg `-0.7501` n `74`; fx avg `0.0676` n `6`; index avg `-0.3894` n `23`; metal avg `-0.0734` n `18`; unknown avg `-0.2278` n `547`
- 24h: commodity avg `-0.6134` n `12`; crypto_alt avg `-1.4319` n `228`; crypto_major avg `-1.9215` n `8`; equity avg `0.4473` n `74`; fx avg `0.1053` n `6`; index avg `0.1999` n `23`; metal avg `0.5761` n `18`; unknown avg `-1.3827` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
