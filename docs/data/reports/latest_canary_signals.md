# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T03:37:21.077310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1286` n `12`; crypto_alt avg `-0.3368` n `228`; crypto_major avg `-0.2936` n `8`; equity avg `-0.0076` n `74`; fx avg `0.0005` n `6`; index avg `0.1571` n `23`; metal avg `0.0123` n `18`; unknown avg `0.0092` n `516`
- 1h: commodity avg `0.1168` n `12`; crypto_alt avg `0.2118` n `228`; crypto_major avg `0.5027` n `8`; equity avg `0.2111` n `74`; fx avg `-0.0` n `6`; index avg `0.3261` n `23`; metal avg `0.1627` n `18`; unknown avg `0.1009` n `516`
- 4h: commodity avg `0.0575` n `12`; crypto_alt avg `1.6906` n `228`; crypto_major avg `1.7312` n `8`; equity avg `0.5775` n `74`; fx avg `0.0007` n `6`; index avg `0.3811` n `23`; metal avg `0.4929` n `18`; unknown avg `0.9895` n `515`
- 24h: commodity avg `0.2141` n `12`; crypto_alt avg `1.8771` n `228`; crypto_major avg `1.129` n `8`; equity avg `1.6003` n `74`; fx avg `0.0556` n `6`; index avg `1.1485` n `23`; metal avg `0.4473` n `18`; unknown avg `0.4741` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
