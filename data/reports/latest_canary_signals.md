# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:52:29.374034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `0.1623` n `230`; crypto_major avg `0.2793` n `8`; equity avg `0.0536` n `121`; fx avg `-0.0038` n `6`; index avg `0.0044` n `25`; metal avg `0.0412` n `20`; unknown avg `-0.0052` n `792`
- 1h: commodity avg `-0.019` n `12`; crypto_alt avg `0.226` n `230`; crypto_major avg `0.3291` n `8`; equity avg `0.0445` n `121`; fx avg `0.015` n `6`; index avg `0.0123` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.273` n `792`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1988` n `230`; crypto_major avg `-0.3227` n `8`; equity avg `0.0214` n `121`; fx avg `0.0417` n `6`; index avg `0.0513` n `25`; metal avg `-0.0807` n `20`; unknown avg `-0.1127` n `792`
- 24h: commodity avg `-0.0908` n `12`; crypto_alt avg `5.5578` n `230`; crypto_major avg `9.7939` n `8`; equity avg `1.6127` n `120`; fx avg `0.0761` n `6`; index avg `0.4024` n `25`; metal avg `1.1277` n `20`; unknown avg `1.8048` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
