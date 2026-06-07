# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T17:01:06.824016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0856` n `228`; crypto_major avg `-0.1161` n `8`; equity avg `-0.0815` n `74`; fx avg `0.0031` n `6`; index avg `-0.0117` n `23`; metal avg `0.0075` n `18`; unknown avg `0.0049` n `516`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.1753` n `228`; crypto_major avg `0.317` n `8`; equity avg `0.2407` n `74`; fx avg `0.0031` n `6`; index avg `0.122` n `23`; metal avg `0.1099` n `18`; unknown avg `5.0075` n `516`
- 4h: commodity avg `0.193` n `12`; crypto_alt avg `0.9099` n `228`; crypto_major avg `1.0612` n `8`; equity avg `0.6679` n `74`; fx avg `-0.005` n `6`; index avg `0.2309` n `23`; metal avg `0.1628` n `18`; unknown avg `0.3357` n `516`
- 24h: commodity avg `0.2587` n `12`; crypto_alt avg `2.8481` n `228`; crypto_major avg `3.1726` n `8`; equity avg `1.9526` n `74`; fx avg `-0.0387` n `6`; index avg `0.3795` n `23`; metal avg `0.6544` n `18`; unknown avg `-4.0548` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
