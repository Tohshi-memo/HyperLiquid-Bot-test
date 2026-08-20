# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:07:26.269206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `0.1031` n `8`; equity avg `0.104` n `121`; fx avg `0.0062` n `6`; index avg `0.0202` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.4888` n `792`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `0.0891` n `230`; crypto_major avg `0.2675` n `8`; equity avg `0.1834` n `121`; fx avg `-0.0062` n `6`; index avg `0.0231` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.0818` n `792`
- 4h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.1554` n `230`; crypto_major avg `-0.2619` n `8`; equity avg `0.5882` n `121`; fx avg `0.1017` n `6`; index avg `0.2071` n `25`; metal avg `-0.0966` n `20`; unknown avg `-0.0107` n `792`
- 24h: commodity avg `-0.0467` n `12`; crypto_alt avg `5.1843` n `230`; crypto_major avg `9.5383` n `8`; equity avg `1.3873` n `120`; fx avg `0.0555` n `6`; index avg `0.3531` n `25`; metal avg `1.0674` n `20`; unknown avg `1.6658` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
