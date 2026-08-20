# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T20:52:26.750111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1188` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.0061` n `230`; crypto_major avg `-0.2304` n `8`; equity avg `0.0129` n `121`; fx avg `-0.0012` n `6`; index avg `0.0017` n `25`; metal avg `0.0021` n `20`; unknown avg `0.1542` n `792`
- 1h: commodity avg `-0.0372` n `12`; crypto_alt avg `0.4575` n `230`; crypto_major avg `0.3187` n `8`; equity avg `0.1158` n `121`; fx avg `-0.0083` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0534` n `20`; unknown avg `-0.1044` n `792`
- 4h: commodity avg `0.1369` n `12`; crypto_alt avg `-0.3858` n `230`; crypto_major avg `-1.1878` n `8`; equity avg `0.1762` n `121`; fx avg `0.0041` n `6`; index avg `-0.069` n `25`; metal avg `0.0263` n `20`; unknown avg `0.5914` n `792`
- 24h: commodity avg `0.3688` n `12`; crypto_alt avg `4.1616` n `230`; crypto_major avg `5.4038` n `8`; equity avg `-0.6974` n `121`; fx avg `0.1993` n `6`; index avg `-0.056` n `25`; metal avg `0.0981` n `20`; unknown avg `2.905` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
