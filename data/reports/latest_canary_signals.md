# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T20:52:33.319875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.1263` n `230`; crypto_major avg `0.0582` n `8`; equity avg `0.2336` n `107`; fx avg `0.0014` n `6`; index avg `0.0192` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.0012` n `782`
- 1h: commodity avg `-0.112` n `12`; crypto_alt avg `0.0867` n `230`; crypto_major avg `0.0391` n `8`; equity avg `-0.5679` n `107`; fx avg `0.003` n `6`; index avg `-0.0696` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.0423` n `782`
- 4h: commodity avg `-0.1715` n `12`; crypto_alt avg `0.5491` n `230`; crypto_major avg `0.4117` n `8`; equity avg `-0.3058` n `107`; fx avg `0.052` n `6`; index avg `0.0708` n `25`; metal avg `-0.1398` n `20`; unknown avg `-0.1111` n `782`
- 24h: commodity avg `-1.233` n `12`; crypto_alt avg `0.1181` n `230`; crypto_major avg `0.5547` n `8`; equity avg `3.037` n `107`; fx avg `0.1236` n `6`; index avg `0.7072` n `25`; metal avg `0.851` n `20`; unknown avg `0.4548` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
