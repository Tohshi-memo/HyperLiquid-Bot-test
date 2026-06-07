# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T15:22:22.050674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0736` n `12`; crypto_alt avg `-0.0301` n `228`; crypto_major avg `0.2116` n `8`; equity avg `0.0035` n `74`; fx avg `-0.0005` n `6`; index avg `-0.0321` n `23`; metal avg `0.0214` n `18`; unknown avg `0.0148` n `516`
- 1h: commodity avg `0.1396` n `12`; crypto_alt avg `-0.1085` n `228`; crypto_major avg `-0.1023` n `8`; equity avg `-0.1172` n `74`; fx avg `-0.0057` n `6`; index avg `-0.1868` n `23`; metal avg `-0.0751` n `18`; unknown avg `0.0865` n `516`
- 4h: commodity avg `0.2965` n `12`; crypto_alt avg `-0.0412` n `228`; crypto_major avg `-0.2353` n `8`; equity avg `0.302` n `74`; fx avg `0.0059` n `6`; index avg `0.0951` n `23`; metal avg `-0.1333` n `18`; unknown avg `0.1454` n `516`
- 24h: commodity avg `0.3118` n `12`; crypto_alt avg `3.0546` n `228`; crypto_major avg `3.0097` n `8`; equity avg `1.8804` n `74`; fx avg `0.0227` n `6`; index avg `0.3086` n `23`; metal avg `0.6444` n `18`; unknown avg `-4.7722` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
