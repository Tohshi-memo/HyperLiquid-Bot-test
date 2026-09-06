# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T16:37:31.132732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.1535` n `232`; crypto_major avg `0.0797` n `8`; equity avg `-0.0069` n `134`; fx avg `-0.0092` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0067` n `20`; unknown avg `2.9798` n `787`
- 1h: commodity avg `0.019` n `12`; crypto_alt avg `0.5945` n `232`; crypto_major avg `0.078` n `8`; equity avg `0.0141` n `134`; fx avg `-0.007` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0122` n `20`; unknown avg `0.4881` n `784`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.2278` n `232`; crypto_major avg `-0.7361` n `8`; equity avg `-0.2929` n `134`; fx avg `-0.0129` n `6`; index avg `-0.0413` n `26`; metal avg `-0.033` n `20`; unknown avg `0.9705` n `720`
- 24h: commodity avg `0.1124` n `12`; crypto_alt avg `1.766` n `232`; crypto_major avg `0.5763` n `8`; equity avg `0.2095` n `134`; fx avg `-0.0219` n `6`; index avg `0.0239` n `26`; metal avg `-0.0339` n `20`; unknown avg `1.6345` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
