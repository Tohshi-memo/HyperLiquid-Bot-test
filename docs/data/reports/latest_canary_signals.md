# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T19:41:08.044945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `13`; crypto_alt avg `-0.1667` n `236`; crypto_major avg `-0.1258` n `8`; equity avg `-0.0342` n `151`; fx avg `-0.001` n `6`; index avg `-0.0154` n `26`; metal avg `-0.0617` n `20`; unknown avg `14.6978` n `1128`
- 1h: commodity avg `-0.0514` n `13`; crypto_alt avg `0.1215` n `236`; crypto_major avg `0.2828` n `8`; equity avg `0.1054` n `151`; fx avg `0.0189` n `6`; index avg `0.0064` n `26`; metal avg `-0.0297` n `20`; unknown avg `11.0501` n `1126`
- 4h: commodity avg `0.0782` n `13`; crypto_alt avg `0.0491` n `236`; crypto_major avg `-0.2554` n `8`; equity avg `-0.8107` n `151`; fx avg `0.0286` n `6`; index avg `-0.1374` n `26`; metal avg `-0.0906` n `20`; unknown avg `6.7553` n `1116`
- 24h: commodity avg `-0.175` n `13`; crypto_alt avg `-2.585` n `236`; crypto_major avg `-2.0663` n `8`; equity avg `-3.842` n `151`; fx avg `-0.1525` n `6`; index avg `-0.54` n `26`; metal avg `-0.892` n `20`; unknown avg `1282.7702` n `968`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.062`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0617`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0581`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.055`, n `666`, weak_sample_signal
