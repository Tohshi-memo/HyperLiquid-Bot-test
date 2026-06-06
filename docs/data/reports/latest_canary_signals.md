# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T21:37:24.117699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.1396` n `228`; crypto_major avg `-0.0686` n `8`; equity avg `0.0218` n `74`; fx avg `-0.0313` n `6`; index avg `0.0914` n `23`; metal avg `-0.0067` n `18`; unknown avg `0.075` n `515`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `0.5305` n `228`; crypto_major avg `0.4516` n `8`; equity avg `0.0936` n `74`; fx avg `-0.0455` n `6`; index avg `0.2119` n `23`; metal avg `0.0121` n `18`; unknown avg `0.1605` n `515`
- 4h: commodity avg `0.0615` n `12`; crypto_alt avg `0.4618` n `228`; crypto_major avg `0.0895` n `8`; equity avg `0.3722` n `74`; fx avg `-0.0223` n `6`; index avg `0.1816` n `23`; metal avg `-0.0057` n `18`; unknown avg `3.4146` n `515`
- 24h: commodity avg `0.773` n `12`; crypto_alt avg `-2.6664` n `228`; crypto_major avg `-2.5067` n `8`; equity avg `-0.982` n `74`; fx avg `-0.0025` n `6`; index avg `0.0821` n `23`; metal avg `-0.5784` n `18`; unknown avg `0.276` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
