# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T23:07:27.406194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0761` n `230`; crypto_major avg `-0.1678` n `8`; equity avg `-0.0195` n `94`; fx avg `-0.0004` n `6`; index avg `0.0024` n `25`; metal avg `0.0245` n `20`; unknown avg `0.0939` n `768`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.8298` n `230`; crypto_major avg `-0.754` n `8`; equity avg `-0.5119` n `94`; fx avg `0.0019` n `6`; index avg `-0.0679` n `25`; metal avg `-0.0334` n `20`; unknown avg `-0.2067` n `768`
- 4h: commodity avg `0.1173` n `12`; crypto_alt avg `-0.5892` n `230`; crypto_major avg `-0.636` n `8`; equity avg `-0.4419` n `94`; fx avg `-0.0158` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0663` n `20`; unknown avg `-0.2974` n `768`
- 24h: commodity avg `-0.1889` n `12`; crypto_alt avg `-1.6974` n `230`; crypto_major avg `-2.756` n `8`; equity avg `-4.1115` n `94`; fx avg `-0.1628` n `6`; index avg `-0.5394` n `25`; metal avg `-0.8571` n `20`; unknown avg `-0.5415` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
