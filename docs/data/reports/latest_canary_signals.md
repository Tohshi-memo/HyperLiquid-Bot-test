# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T02:52:24.518969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.25` n `228`; crypto_major avg `0.4064` n `8`; equity avg `0.0067` n `74`; fx avg `0.0024` n `6`; index avg `-0.0203` n `23`; metal avg `0.1967` n `18`; unknown avg `0.0948` n `425`
- 1h: commodity avg `0.085` n `12`; crypto_alt avg `-0.2543` n `228`; crypto_major avg `-0.0072` n `8`; equity avg `-0.6086` n `74`; fx avg `-0.0031` n `6`; index avg `-0.1861` n `23`; metal avg `-0.1854` n `18`; unknown avg `0.915` n `425`
- 4h: commodity avg `0.4619` n `12`; crypto_alt avg `-1.1519` n `228`; crypto_major avg `-0.5088` n `8`; equity avg `-1.6064` n `74`; fx avg `-0.0237` n `6`; index avg `-0.5063` n `23`; metal avg `-0.3959` n `18`; unknown avg `0.1802` n `425`
- 24h: commodity avg `-1.2673` n `12`; crypto_alt avg `-5.0097` n `228`; crypto_major avg `-4.3955` n `8`; equity avg `-6.9215` n `74`; fx avg `-0.1887` n `6`; index avg `-4.089` n `23`; metal avg `-4.1249` n `18`; unknown avg `0.2114` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
