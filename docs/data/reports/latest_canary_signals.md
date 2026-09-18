# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T04:07:34.096964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.2239` n `234`; crypto_major avg `-0.2866` n `8`; equity avg `0.0126` n `140`; fx avg `-0.0068` n `6`; index avg `0.0019` n `26`; metal avg `0.0141` n `20`; unknown avg `0.0227` n `917`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.8568` n `234`; crypto_major avg `0.5697` n `8`; equity avg `0.3267` n `140`; fx avg `0.0514` n `6`; index avg `0.0531` n `26`; metal avg `0.0789` n `20`; unknown avg `69.1025` n `913`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `2.5685` n `234`; crypto_major avg `1.665` n `8`; equity avg `0.5895` n `140`; fx avg `0.1581` n `6`; index avg `0.1041` n `26`; metal avg `0.2348` n `20`; unknown avg `3.9999` n `897`
- 24h: commodity avg `-0.3099` n `12`; crypto_alt avg `5.5968` n `234`; crypto_major avg `3.2684` n `8`; equity avg `1.887` n `140`; fx avg `0.1821` n `6`; index avg `0.2656` n `26`; metal avg `0.4936` n `20`; unknown avg `1.7919` n `753`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
