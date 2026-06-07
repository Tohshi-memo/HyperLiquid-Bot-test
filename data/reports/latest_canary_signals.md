# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T07:37:27.499435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0842` n `12`; crypto_alt avg `0.0933` n `228`; crypto_major avg `0.2638` n `8`; equity avg `0.1009` n `74`; fx avg `0.0145` n `6`; index avg `-0.0183` n `23`; metal avg `0.0001` n `18`; unknown avg `0.0097` n `516`
- 1h: commodity avg `-0.0893` n `12`; crypto_alt avg `-0.1672` n `228`; crypto_major avg `0.1826` n `8`; equity avg `0.0323` n `74`; fx avg `0.0077` n `6`; index avg `-0.0429` n `23`; metal avg `0.0027` n `18`; unknown avg `-0.1254` n `516`
- 4h: commodity avg `-0.248` n `12`; crypto_alt avg `1.0139` n `228`; crypto_major avg `1.5608` n `8`; equity avg `0.7096` n `74`; fx avg `0.0074` n `6`; index avg `-0.0036` n `23`; metal avg `0.1585` n `18`; unknown avg `-0.0885` n `506`
- 24h: commodity avg `0.369` n `12`; crypto_alt avg `2.8287` n `228`; crypto_major avg `2.2433` n `8`; equity avg `2.3174` n `74`; fx avg `0.0639` n `6`; index avg `0.9615` n `23`; metal avg `0.5746` n `18`; unknown avg `0.7622` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
