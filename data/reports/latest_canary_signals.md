# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T13:22:33.029531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0959` n `230`; crypto_major avg `0.0868` n `8`; equity avg `-0.047` n `121`; fx avg `-0.0178` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.008` n `792`
- 1h: commodity avg `-0.1374` n `12`; crypto_alt avg `0.1034` n `230`; crypto_major avg `0.6641` n `8`; equity avg `0.3472` n `121`; fx avg `-0.0338` n `6`; index avg `0.0462` n `25`; metal avg `0.121` n `20`; unknown avg `0.1291` n `792`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `0.3149` n `230`; crypto_major avg `0.2285` n `8`; equity avg `-0.9748` n `121`; fx avg `0.0025` n `6`; index avg `-0.1595` n `25`; metal avg `-0.0656` n `20`; unknown avg `0.6278` n `792`
- 24h: commodity avg `0.1671` n `12`; crypto_alt avg `7.3077` n `230`; crypto_major avg `12.0598` n `8`; equity avg `-1.3704` n `121`; fx avg `0.1988` n `6`; index avg `-0.2607` n `25`; metal avg `0.2413` n `20`; unknown avg `2.7611` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
