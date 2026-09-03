# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T21:07:25.243235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0296` n `232`; crypto_major avg `-0.0891` n `8`; equity avg `-0.0126` n `133`; fx avg `-0.0001` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0096` n `20`; unknown avg `-0.0317` n `786`
- 1h: commodity avg `0.052` n `12`; crypto_alt avg `0.0057` n `232`; crypto_major avg `-0.2664` n `8`; equity avg `-0.0951` n `133`; fx avg `0.0045` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.2019` n `774`
- 4h: commodity avg `-0.0535` n `12`; crypto_alt avg `0.4091` n `232`; crypto_major avg `0.4368` n `8`; equity avg `0.0957` n `133`; fx avg `0.0096` n `6`; index avg `0.006` n `26`; metal avg `-0.0799` n `20`; unknown avg `-0.1469` n `774`
- 24h: commodity avg `-0.0537` n `12`; crypto_alt avg `4.5379` n `232`; crypto_major avg `5.37` n `8`; equity avg `1.4933` n `133`; fx avg `-0.2197` n `6`; index avg `0.199` n `26`; metal avg `0.7708` n `20`; unknown avg `28.7353` n `742`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
