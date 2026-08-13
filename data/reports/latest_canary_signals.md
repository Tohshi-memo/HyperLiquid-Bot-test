# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T01:52:33.564867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0668` n `230`; crypto_major avg `-0.0585` n `8`; equity avg `0.066` n `113`; fx avg `0.0037` n `6`; index avg `0.0079` n `25`; metal avg `-0.1515` n `20`; unknown avg `0.1678` n `786`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.1663` n `230`; crypto_major avg `-0.0793` n `8`; equity avg `0.0845` n `113`; fx avg `0.0214` n `6`; index avg `0.0032` n `25`; metal avg `-0.2094` n `20`; unknown avg `0.0471` n `786`
- 4h: commodity avg `-0.1217` n `12`; crypto_alt avg `0.3943` n `230`; crypto_major avg `0.1078` n `8`; equity avg `0.3795` n `113`; fx avg `-0.0468` n `6`; index avg `0.0314` n `25`; metal avg `-0.0369` n `20`; unknown avg `-0.0488` n `786`
- 24h: commodity avg `-0.197` n `12`; crypto_alt avg `-1.5126` n `230`; crypto_major avg `-0.7473` n `8`; equity avg `2.7327` n `113`; fx avg `-0.0583` n `6`; index avg `0.3375` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.0234` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
