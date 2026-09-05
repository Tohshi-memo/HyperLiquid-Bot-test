# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T13:07:27.183441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.1045` n `232`; crypto_major avg `0.1023` n `8`; equity avg `0.0056` n `134`; fx avg `-0.0056` n `6`; index avg `0.0059` n `26`; metal avg `-0.0029` n `20`; unknown avg `16.9154` n `790`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `0.4447` n `232`; crypto_major avg `0.652` n `8`; equity avg `0.0209` n `134`; fx avg `-0.0016` n `6`; index avg `0.0161` n `26`; metal avg `-0.0134` n `20`; unknown avg `-0.1169` n `783`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.481` n `232`; crypto_major avg `0.6804` n `8`; equity avg `0.0803` n `134`; fx avg `-0.0095` n `6`; index avg `0.0465` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.1992` n `780`
- 24h: commodity avg `0.1861` n `12`; crypto_alt avg `3.2725` n `232`; crypto_major avg `1.7249` n `8`; equity avg `1.8129` n `134`; fx avg `0.0062` n `6`; index avg `0.22` n `26`; metal avg `0.2521` n `20`; unknown avg `16.773` n `664`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
