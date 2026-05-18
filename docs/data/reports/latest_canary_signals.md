# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T04:07:15.897176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `0.108` n `228`; crypto_major avg `0.0147` n `8`; equity avg `0.0687` n `66`; fx avg `0.0054` n `5`; index avg `0.0465` n `23`; metal avg `0.2677` n `18`; unknown avg `-0.2575` n `383`
- 1h: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.4412` n `228`; crypto_major avg `-0.3235` n `8`; equity avg `0.0049` n `66`; fx avg `0.0125` n `5`; index avg `0.0981` n `23`; metal avg `0.3758` n `18`; unknown avg `-0.4161` n `383`
- 4h: commodity avg `0.4457` n `12`; crypto_alt avg `0.5684` n `228`; crypto_major avg `-0.4415` n `8`; equity avg `0.6485` n `66`; fx avg `0.0664` n `5`; index avg `0.3737` n `23`; metal avg `-0.4168` n `18`; unknown avg `-0.6946` n `383`
- 24h: commodity avg `2.653` n `12`; crypto_alt avg `-10.9382` n `228`; crypto_major avg `-3.4573` n `8`; equity avg `-2.993` n `65`; fx avg `-0.0642` n `5`; index avg `-1.7319` n `23`; metal avg `-6.0501` n `18`; unknown avg `550.0448` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
