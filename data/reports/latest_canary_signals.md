# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T04:47:25.416650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.0211` n `230`; crypto_major avg `0.0987` n `8`; equity avg `0.0091` n `102`; fx avg `0.0129` n `6`; index avg `0.0033` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0276` n `781`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.1493` n `230`; crypto_major avg `0.1867` n `8`; equity avg `0.0369` n `102`; fx avg `0.007` n `6`; index avg `0.0386` n `25`; metal avg `-0.0139` n `20`; unknown avg `0.4061` n `781`
- 4h: commodity avg `-0.0705` n `12`; crypto_alt avg `0.1766` n `230`; crypto_major avg `0.1731` n `8`; equity avg `0.0172` n `102`; fx avg `0.0272` n `6`; index avg `0.0565` n `25`; metal avg `-0.0135` n `20`; unknown avg `0.2316` n `781`
- 24h: commodity avg `0.9971` n `12`; crypto_alt avg `0.5939` n `230`; crypto_major avg `-1.2633` n `8`; equity avg `-2.5904` n `102`; fx avg `-0.1361` n `6`; index avg `-0.2683` n `25`; metal avg `-0.2605` n `20`; unknown avg `4.8209` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
