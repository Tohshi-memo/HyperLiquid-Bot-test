# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T21:22:20.102071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.1001` n `228`; crypto_major avg `0.1083` n `8`; equity avg `0.0745` n `74`; fx avg `0.0067` n `6`; index avg `0.0256` n `23`; metal avg `0.0081` n `18`; unknown avg `0.0188` n `516`
- 1h: commodity avg `0.0296` n `12`; crypto_alt avg `0.0358` n `228`; crypto_major avg `-0.0394` n `8`; equity avg `0.1288` n `74`; fx avg `-0.011` n `6`; index avg `0.1354` n `23`; metal avg `-0.0252` n `18`; unknown avg `0.1778` n `516`
- 4h: commodity avg `0.1767` n `12`; crypto_alt avg `-1.3791` n `228`; crypto_major avg `-0.8303` n `8`; equity avg `-0.6231` n `74`; fx avg `-0.0071` n `6`; index avg `-0.0863` n `23`; metal avg `-0.3569` n `18`; unknown avg `0.0496` n `516`
- 24h: commodity avg `0.2666` n `12`; crypto_alt avg `1.7072` n `228`; crypto_major avg `2.7652` n `8`; equity avg `1.1171` n `74`; fx avg `-0.0532` n `6`; index avg `0.2798` n `23`; metal avg `0.3038` n `18`; unknown avg `-4.6059` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
