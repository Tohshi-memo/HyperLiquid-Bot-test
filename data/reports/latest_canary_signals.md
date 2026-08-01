# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T05:37:33.064774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `0.0577` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `-0.0907` n `102`; fx avg `0.0046` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.1028` n `781`
- 1h: commodity avg `-0.0768` n `12`; crypto_alt avg `0.0612` n `230`; crypto_major avg `-0.0278` n `8`; equity avg `-0.0668` n `102`; fx avg `0.0127` n `6`; index avg `-0.0425` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0884` n `781`
- 4h: commodity avg `-0.0647` n `12`; crypto_alt avg `0.1062` n `230`; crypto_major avg `-0.0134` n `8`; equity avg `-0.0133` n `102`; fx avg `0.0285` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.57` n `781`
- 24h: commodity avg `1.0174` n `12`; crypto_alt avg `0.4104` n `230`; crypto_major avg `-1.5125` n `8`; equity avg `-2.8281` n `102`; fx avg `-0.1043` n `6`; index avg `-0.3717` n `25`; metal avg `-0.2384` n `20`; unknown avg `4.7747` n `747`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
