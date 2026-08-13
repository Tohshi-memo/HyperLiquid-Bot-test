# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T03:07:26.135953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1093` n `230`; crypto_major avg `0.118` n `8`; equity avg `0.0168` n `113`; fx avg `-0.0002` n `6`; index avg `0.0051` n `25`; metal avg `0.012` n `20`; unknown avg `1.2427` n `786`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.1867` n `230`; crypto_major avg `0.2844` n `8`; equity avg `0.011` n `113`; fx avg `0.0072` n `6`; index avg `0.0057` n `25`; metal avg `-0.0234` n `20`; unknown avg `0.6829` n `786`
- 4h: commodity avg `-0.1328` n `12`; crypto_alt avg `0.6161` n `230`; crypto_major avg `0.5733` n `8`; equity avg `0.5247` n `113`; fx avg `-0.0293` n `6`; index avg `0.0704` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.0237` n `786`
- 24h: commodity avg `-0.2934` n `12`; crypto_alt avg `-1.5524` n `230`; crypto_major avg `-0.2184` n `8`; equity avg `2.495` n `113`; fx avg `-0.0675` n `6`; index avg `0.2899` n `25`; metal avg `-0.1667` n `20`; unknown avg `0.0052` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2396`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
