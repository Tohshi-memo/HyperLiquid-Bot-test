# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T09:37:39.984795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `-0.1049` n `228`; crypto_major avg `-0.1031` n `8`; equity avg `-0.0665` n `77`; fx avg `-0.0101` n `6`; index avg `-0.0211` n `23`; metal avg `0.1083` n `18`; unknown avg `0.3763` n `687`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `0.121` n `228`; crypto_major avg `0.1044` n `8`; equity avg `0.0348` n `77`; fx avg `0.0252` n `6`; index avg `0.0505` n `23`; metal avg `0.2346` n `18`; unknown avg `0.3104` n `687`
- 4h: commodity avg `-0.4136` n `12`; crypto_alt avg `1.0858` n `228`; crypto_major avg `1.0827` n `8`; equity avg `0.6219` n `77`; fx avg `0.0302` n `6`; index avg `0.1581` n `23`; metal avg `1.1532` n `18`; unknown avg `0.5248` n `647`
- 24h: commodity avg `0.2323` n `12`; crypto_alt avg `1.5808` n `228`; crypto_major avg `3.5663` n `8`; equity avg `1.7753` n `76`; fx avg `-0.0776` n `6`; index avg `0.5321` n `23`; metal avg `0.2569` n `18`; unknown avg `0.6425` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
