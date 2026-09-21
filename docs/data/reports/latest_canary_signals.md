# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T17:22:30.464183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.4979` n `234`; crypto_major avg `-0.248` n `8`; equity avg `-0.0683` n `140`; fx avg `-0.0034` n `6`; index avg `0.0075` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.1362` n `942`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.9906` n `234`; crypto_major avg `-0.1888` n `8`; equity avg `-0.0553` n `140`; fx avg `-0.0016` n `6`; index avg `0.0102` n `26`; metal avg `-0.1052` n `20`; unknown avg `0.2996` n `940`
- 4h: commodity avg `-0.1751` n `12`; crypto_alt avg `-0.7655` n `234`; crypto_major avg `0.2592` n `8`; equity avg `0.7908` n `140`; fx avg `-0.0213` n `6`; index avg `0.2497` n `26`; metal avg `-0.2988` n `20`; unknown avg `11.5585` n `870`
- 24h: commodity avg `-1.0714` n `12`; crypto_alt avg `3.6745` n `234`; crypto_major avg `4.9002` n `8`; equity avg `2.5548` n `140`; fx avg `-0.1096` n `6`; index avg `0.5792` n `26`; metal avg `-0.0332` n `20`; unknown avg `7.4873` n `739`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
