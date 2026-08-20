# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T03:07:27.211466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.2605` n `230`; crypto_major avg `-0.3939` n `8`; equity avg `0.0527` n `121`; fx avg `0.0179` n `6`; index avg `0.0221` n `25`; metal avg `0.0356` n `20`; unknown avg `-0.0212` n `792`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.5391` n `230`; crypto_major avg `-0.7104` n `8`; equity avg `-0.2183` n `121`; fx avg `0.0017` n `6`; index avg `-0.0384` n `25`; metal avg `0.0072` n `20`; unknown avg `0.1468` n `792`
- 4h: commodity avg `0.0466` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `-0.667` n `8`; equity avg `0.023` n `121`; fx avg `0.1085` n `6`; index avg `0.0658` n `25`; metal avg `-0.1396` n `20`; unknown avg `-0.0362` n `792`
- 24h: commodity avg `-0.1145` n `12`; crypto_alt avg `5.322` n `230`; crypto_major avg `9.3904` n `8`; equity avg `0.9688` n `120`; fx avg `0.0679` n `6`; index avg `0.2862` n `25`; metal avg `1.0536` n `20`; unknown avg `1.6002` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
