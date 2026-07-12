# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T06:44:41.178199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0579` n `12`; crypto_alt avg `0.0461` n `230`; crypto_major avg `0.0771` n `8`; equity avg `-0.0187` n `92`; fx avg `-0.0021` n `6`; index avg `-0.004` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0213` n `765`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.3842` n `230`; crypto_major avg `-0.3216` n `8`; equity avg `-0.1403` n `92`; fx avg `-0.0043` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.1553` n `749`
- 4h: commodity avg `-0.1015` n `12`; crypto_alt avg `-0.3374` n `230`; crypto_major avg `-0.5284` n `8`; equity avg `-0.1569` n `92`; fx avg `-0.0032` n `6`; index avg `-0.0204` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.2787` n `749`
- 24h: commodity avg `0.4512` n `12`; crypto_alt avg `-0.964` n `230`; crypto_major avg `-0.9909` n `8`; equity avg `-0.1121` n `92`; fx avg `-0.0125` n `6`; index avg `-0.1164` n `25`; metal avg `-0.1023` n `20`; unknown avg `-0.1072` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
