# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T14:37:28.415580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.245` n `230`; crypto_major avg `0.3646` n `8`; equity avg `0.0644` n `121`; fx avg `-0.0116` n `6`; index avg `-0.006` n `25`; metal avg `-0.1318` n `20`; unknown avg `0.0094` n `793`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `0.8674` n `230`; crypto_major avg `0.623` n `8`; equity avg `-0.4043` n `121`; fx avg `0.0027` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0762` n `20`; unknown avg `-0.0289` n `793`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `1.7836` n `230`; crypto_major avg `0.6342` n `8`; equity avg `-0.7996` n `121`; fx avg `-0.0307` n `6`; index avg `-0.1041` n `25`; metal avg `-0.0514` n `20`; unknown avg `0.2741` n `793`
- 24h: commodity avg `0.304` n `12`; crypto_alt avg `8.4052` n `230`; crypto_major avg `6.5489` n `8`; equity avg `0.6363` n `121`; fx avg `-0.0917` n `6`; index avg `-0.0176` n `25`; metal avg `0.6912` n `20`; unknown avg `3.1586` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
