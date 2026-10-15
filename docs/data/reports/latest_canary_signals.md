# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T19:07:31.021265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.2459` n `236`; crypto_major avg `0.1143` n `8`; equity avg `0.3823` n `151`; fx avg `-0.0056` n `6`; index avg `0.065` n `26`; metal avg `-0.0013` n `20`; unknown avg `8.6368` n `1134`
- 1h: commodity avg `-0.1042` n `13`; crypto_alt avg `0.3693` n `236`; crypto_major avg `0.2558` n `8`; equity avg `0.5469` n `151`; fx avg `-0.0159` n `6`; index avg `0.0661` n `26`; metal avg `0.0009` n `20`; unknown avg `0.9887` n `1134`
- 4h: commodity avg `-0.0041` n `13`; crypto_alt avg `1.5404` n `236`; crypto_major avg `0.8275` n `8`; equity avg `1.034` n `151`; fx avg `0.0193` n `6`; index avg `0.0926` n `26`; metal avg `0.0442` n `20`; unknown avg `-0.2649` n `1128`
- 24h: commodity avg `-0.0389` n `13`; crypto_alt avg `1.3537` n `236`; crypto_major avg `0.9965` n `8`; equity avg `-0.4179` n `151`; fx avg `0.2039` n `6`; index avg `-0.0985` n `26`; metal avg `0.465` n `20`; unknown avg `0.385` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.083`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0816`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
