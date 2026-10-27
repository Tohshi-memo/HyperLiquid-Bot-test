# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T07:07:27.784721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0724` n `13`; crypto_alt avg `0.0841` n `238`; crypto_major avg `0.0316` n `8`; equity avg `-0.1672` n `154`; fx avg `-0.025` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0147` n `20`; unknown avg `0.0338` n `1226`
- 1h: commodity avg `0.1635` n `13`; crypto_alt avg `-0.2295` n `237`; crypto_major avg `-0.3137` n `8`; equity avg `-0.4576` n `154`; fx avg `-0.0262` n `6`; index avg `-0.071` n `27`; metal avg `-0.1663` n `20`; unknown avg `0.3675` n `1224`
- 4h: commodity avg `0.2743` n `13`; crypto_alt avg `0.1811` n `237`; crypto_major avg `-0.2046` n `8`; equity avg `-1.2667` n `154`; fx avg `-0.0527` n `6`; index avg `-0.0613` n `27`; metal avg `-0.2469` n `20`; unknown avg `1.6951` n `1192`
- 24h: commodity avg `0.2308` n `13`; crypto_alt avg `-0.0023` n `237`; crypto_major avg `-0.1278` n `8`; equity avg `0.3547` n `153`; fx avg `-0.0474` n `6`; index avg `0.0491` n `27`; metal avg `-0.3096` n `20`; unknown avg `1119.6172` n `982`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
