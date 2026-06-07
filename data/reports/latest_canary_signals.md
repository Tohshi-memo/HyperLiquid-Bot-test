# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T08:07:22.074123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.2026` n `228`; crypto_major avg `-0.0798` n `8`; equity avg `-0.0346` n `74`; fx avg `0.0145` n `6`; index avg `0.0052` n `23`; metal avg `0.0012` n `18`; unknown avg `-0.1642` n `516`
- 1h: commodity avg `-0.1742` n `12`; crypto_alt avg `-0.2591` n `228`; crypto_major avg `-0.007` n `8`; equity avg `-0.0311` n `74`; fx avg `0.0127` n `6`; index avg `-0.0246` n `23`; metal avg `0.0069` n `18`; unknown avg `-0.2517` n `516`
- 4h: commodity avg `-0.3679` n `12`; crypto_alt avg `0.8251` n `228`; crypto_major avg `1.476` n `8`; equity avg `0.6194` n `74`; fx avg `0.0019` n `6`; index avg `0.0045` n `23`; metal avg `0.1742` n `18`; unknown avg `-0.2054` n `506`
- 24h: commodity avg `0.1791` n `12`; crypto_alt avg `2.568` n `228`; crypto_major avg `2.1177` n `8`; equity avg `2.5598` n `74`; fx avg `0.0642` n `6`; index avg `1.167` n `23`; metal avg `0.6442` n `18`; unknown avg `0.3545` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
