# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:37:31.989163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.018` n `230`; crypto_major avg `0.0015` n `8`; equity avg `-0.1333` n `121`; fx avg `0.0078` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0613` n `20`; unknown avg `0.1885` n `792`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `0.1884` n `230`; crypto_major avg `0.2398` n `8`; equity avg `0.1948` n `121`; fx avg `0.0053` n `6`; index avg `0.0466` n `25`; metal avg `-0.0323` n `20`; unknown avg `0.2598` n `792`
- 4h: commodity avg `0.017` n `12`; crypto_alt avg `-0.5145` n `230`; crypto_major avg `-0.7296` n `8`; equity avg `0.0445` n `121`; fx avg `0.111` n `6`; index avg `0.0667` n `25`; metal avg `-0.1534` n `20`; unknown avg `0.0573` n `792`
- 24h: commodity avg `-0.0562` n `12`; crypto_alt avg `5.3414` n `230`; crypto_major avg `9.4196` n `8`; equity avg `1.3401` n `120`; fx avg `0.0686` n `6`; index avg `0.3391` n `25`; metal avg `1.0411` n `20`; unknown avg `1.6931` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
