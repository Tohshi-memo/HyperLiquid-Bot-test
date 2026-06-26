# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T12:37:30.321498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0988` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0521` n `228`; crypto_major avg `-0.0327` n `8`; equity avg `-0.0364` n `86`; fx avg `-0.0034` n `6`; index avg `-0.0091` n `23`; metal avg `0.0041` n `20`; unknown avg `0.0374` n `765`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.2302` n `228`; crypto_major avg `0.0952` n `8`; equity avg `-0.1473` n `86`; fx avg `-0.0067` n `6`; index avg `-0.0196` n `23`; metal avg `-0.049` n `20`; unknown avg `0.0077` n `765`
- 4h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.7644` n `228`; crypto_major avg `-1.1655` n `8`; equity avg `-0.407` n `86`; fx avg `-0.0179` n `6`; index avg `-0.0667` n `23`; metal avg `0.1981` n `20`; unknown avg `-0.1642` n `765`
- 24h: commodity avg `0.08` n `12`; crypto_alt avg `-1.7616` n `228`; crypto_major avg `-2.0797` n `8`; equity avg `-4.3944` n `86`; fx avg `0.0405` n `6`; index avg `-0.6637` n `23`; metal avg `0.4237` n `20`; unknown avg `0.7564` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2938`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
