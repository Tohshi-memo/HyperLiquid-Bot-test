# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T10:07:25.976778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `-0.1444` n `8`; equity avg `0.109` n `113`; fx avg `0.0039` n `6`; index avg `0.004` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0021` n `787`
- 1h: commodity avg `0.0871` n `12`; crypto_alt avg `0.1505` n `230`; crypto_major avg `0.0473` n `8`; equity avg `0.1235` n `113`; fx avg `0.0099` n `6`; index avg `0.0168` n `25`; metal avg `0.0947` n `20`; unknown avg `-0.0812` n `787`
- 4h: commodity avg `-0.2361` n `12`; crypto_alt avg `0.0448` n `230`; crypto_major avg `-0.2431` n `8`; equity avg `-0.3887` n `113`; fx avg `0.0797` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0697` n `20`; unknown avg `-0.0805` n `787`
- 24h: commodity avg `-0.2188` n `12`; crypto_alt avg `-0.6312` n `230`; crypto_major avg `-0.3411` n `8`; equity avg `1.3324` n `113`; fx avg `0.0544` n `6`; index avg `0.1479` n `25`; metal avg `-0.5531` n `20`; unknown avg `0.1345` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
