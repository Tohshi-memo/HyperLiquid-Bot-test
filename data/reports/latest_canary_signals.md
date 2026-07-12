# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T09:07:33.234154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `0.0187` n `8`; equity avg `0.0121` n `92`; fx avg `-0.0037` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.6878` n `765`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.0237` n `230`; crypto_major avg `0.0456` n `8`; equity avg `0.0493` n `92`; fx avg `0.0016` n `6`; index avg `0.0126` n `25`; metal avg `-0.0053` n `20`; unknown avg `4.9434` n `765`
- 4h: commodity avg `0.0941` n `12`; crypto_alt avg `-0.3212` n `230`; crypto_major avg `-0.0722` n `8`; equity avg `-0.0512` n `92`; fx avg `0.0041` n `6`; index avg `0.0026` n `25`; metal avg `-0.0287` n `20`; unknown avg `2.7223` n `747`
- 24h: commodity avg `0.5027` n `12`; crypto_alt avg `-0.8496` n `230`; crypto_major avg `-0.6952` n `8`; equity avg `-0.1136` n `92`; fx avg `0.0062` n `6`; index avg `-0.1045` n `25`; metal avg `-0.1161` n `20`; unknown avg `0.8749` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
