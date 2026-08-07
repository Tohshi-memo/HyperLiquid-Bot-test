# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T07:22:28.655947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0684` n `12`; crypto_alt avg `0.0497` n `230`; crypto_major avg `0.0207` n `8`; equity avg `0.0514` n `112`; fx avg `0.0157` n `6`; index avg `0.0158` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0072` n `782`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.1146` n `230`; crypto_major avg `-0.028` n `8`; equity avg `0.1793` n `112`; fx avg `-0.0218` n `6`; index avg `0.0431` n `25`; metal avg `0.0281` n `20`; unknown avg `-0.0227` n `782`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.1872` n `230`; crypto_major avg `-0.0435` n `8`; equity avg `0.4618` n `112`; fx avg `-0.0413` n `6`; index avg `0.1204` n `25`; metal avg `0.3263` n `20`; unknown avg `-0.0494` n `766`
- 24h: commodity avg `0.5493` n `12`; crypto_alt avg `0.1216` n `230`; crypto_major avg `-1.0288` n `8`; equity avg `1.3063` n `109`; fx avg `-0.075` n `6`; index avg `-0.021` n `25`; metal avg `0.2774` n `20`; unknown avg `110.7392` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
