# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T00:37:38.232474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `0.1529` n `234`; crypto_major avg `-0.1803` n `8`; equity avg `0.0566` n `140`; fx avg `-0.0319` n `6`; index avg `0.0043` n `26`; metal avg `-0.0407` n `20`; unknown avg `0.678` n `944`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `0.5784` n `234`; crypto_major avg `0.1893` n `8`; equity avg `0.2819` n `140`; fx avg `-0.1176` n `6`; index avg `0.0426` n `26`; metal avg `-0.0313` n `20`; unknown avg `0.8166` n `936`
- 4h: commodity avg `0.1355` n `12`; crypto_alt avg `0.6386` n `234`; crypto_major avg `0.0003` n `8`; equity avg `0.6432` n `140`; fx avg `-0.127` n `6`; index avg `0.0911` n `26`; metal avg `0.1026` n `20`; unknown avg `0.3323` n `936`
- 24h: commodity avg `-0.4294` n `12`; crypto_alt avg `3.5557` n `234`; crypto_major avg `4.6925` n `8`; equity avg `2.6113` n `140`; fx avg `-0.2224` n `6`; index avg `0.5606` n `26`; metal avg `0.0764` n `20`; unknown avg `12.5756` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
