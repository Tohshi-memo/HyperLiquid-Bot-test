# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T19:07:32.385288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `13`; crypto_alt avg `-0.1123` n `235`; crypto_major avg `-0.1473` n `8`; equity avg `-0.052` n `150`; fx avg `-0.0037` n `6`; index avg `-0.0097` n `26`; metal avg `0.0394` n `20`; unknown avg `2.2745` n `1074`
- 1h: commodity avg `0.2632` n `13`; crypto_alt avg `-0.2368` n `235`; crypto_major avg `-0.361` n `8`; equity avg `-0.2973` n `150`; fx avg `-0.0139` n `6`; index avg `-0.0399` n `26`; metal avg `0.0761` n `20`; unknown avg `2.5187` n `1074`
- 4h: commodity avg `0.5781` n `13`; crypto_alt avg `-0.8403` n `235`; crypto_major avg `-1.0813` n `8`; equity avg `-0.4827` n `150`; fx avg `0.0051` n `6`; index avg `-0.106` n `26`; metal avg `0.1943` n `20`; unknown avg `3.3296` n `1068`
- 24h: commodity avg `0.2745` n `13`; crypto_alt avg `-0.4089` n `235`; crypto_major avg `-0.3531` n `8`; equity avg `0.5675` n `149`; fx avg `0.1004` n `6`; index avg `0.0001` n `26`; metal avg `0.099` n `20`; unknown avg `382.7517` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
