# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T18:47:16.777419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.0401` n `232`; crypto_major avg `0.0394` n `8`; equity avg `0.0142` n `133`; fx avg `-0.0025` n `6`; index avg `-0.007` n `26`; metal avg `-0.0035` n `20`; unknown avg `4.8593` n `792`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `0.1211` n `232`; crypto_major avg `-0.1891` n `8`; equity avg `0.0672` n `133`; fx avg `0.0073` n `6`; index avg `0.0099` n `26`; metal avg `-0.0532` n `20`; unknown avg `3.7121` n `790`
- 4h: commodity avg `-0.243` n `12`; crypto_alt avg `1.444` n `232`; crypto_major avg `1.1514` n `8`; equity avg `1.2607` n `133`; fx avg `0.0371` n `6`; index avg `0.2374` n `26`; metal avg `0.2066` n `20`; unknown avg `5.9724` n `790`
- 24h: commodity avg `-0.103` n `12`; crypto_alt avg `4.5071` n `232`; crypto_major avg `5.1681` n `8`; equity avg `1.6858` n `133`; fx avg `-0.2595` n `6`; index avg `0.2154` n `26`; metal avg `0.8672` n `20`; unknown avg `3.1451` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
