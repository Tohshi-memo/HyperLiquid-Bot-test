# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T02:07:26.013477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0323` n `230`; crypto_major avg `-0.0091` n `8`; equity avg `0.0511` n `121`; fx avg `0.0094` n `6`; index avg `0.0091` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.0147` n `792`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `0.3199` n `230`; crypto_major avg `0.3675` n `8`; equity avg `-0.1026` n `121`; fx avg `0.0268` n `6`; index avg `0.0313` n `25`; metal avg `0.0704` n `20`; unknown avg `-0.0085` n `792`
- 4h: commodity avg `0.0866` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `-0.7749` n `8`; equity avg `0.4792` n `121`; fx avg `0.1327` n `6`; index avg `0.1542` n `25`; metal avg `-0.1479` n `20`; unknown avg `-0.0842` n `792`
- 24h: commodity avg `-0.1115` n `12`; crypto_alt avg `5.652` n `230`; crypto_major avg `10.0662` n `8`; equity avg `0.9261` n `120`; fx avg `-0.0104` n `6`; index avg `0.3157` n `25`; metal avg `1.038` n `20`; unknown avg `1.5765` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
