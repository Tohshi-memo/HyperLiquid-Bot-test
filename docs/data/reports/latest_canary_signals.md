# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T21:22:26.338267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.0951` n `230`; crypto_major avg `0.0577` n `8`; equity avg `0.0017` n `114`; fx avg `0.0031` n `6`; index avg `0.0019` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0942` n `791`
- 1h: commodity avg `-0.0311` n `12`; crypto_alt avg `0.049` n `230`; crypto_major avg `0.0314` n `8`; equity avg `-0.0052` n `114`; fx avg `0.003` n `6`; index avg `-0.0026` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0162` n `791`
- 4h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.1181` n `230`; crypto_major avg `0.0511` n `8`; equity avg `0.1035` n `114`; fx avg `0.007` n `6`; index avg `-0.0062` n `25`; metal avg `0.0062` n `20`; unknown avg `0.8893` n `791`
- 24h: commodity avg `-0.0274` n `12`; crypto_alt avg `1.0246` n `230`; crypto_major avg `0.6565` n `8`; equity avg `0.206` n `114`; fx avg `0.0196` n `6`; index avg `-0.008` n `25`; metal avg `0.0162` n `20`; unknown avg `0.16` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
