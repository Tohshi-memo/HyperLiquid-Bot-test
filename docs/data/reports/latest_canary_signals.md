# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T18:07:30.238953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.2253` n `228`; crypto_major avg `0.1869` n `8`; equity avg `-0.0877` n `74`; fx avg `0.0` n `6`; index avg `-0.0292` n `23`; metal avg `0.0029` n `18`; unknown avg `0.2067` n `516`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.1191` n `228`; crypto_major avg `0.1049` n `8`; equity avg `-0.1801` n `74`; fx avg `0.0292` n `6`; index avg `-0.1275` n `23`; metal avg `0.002` n `18`; unknown avg `-0.0842` n `516`
- 4h: commodity avg `0.2994` n `12`; crypto_alt avg `0.7532` n `228`; crypto_major avg `1.0953` n `8`; equity avg `0.2171` n `74`; fx avg `0.0004` n `6`; index avg `-0.037` n `23`; metal avg `0.1108` n `18`; unknown avg `-2.1831` n `516`
- 24h: commodity avg `0.1957` n `12`; crypto_alt avg `3.7336` n `228`; crypto_major avg `4.2337` n `8`; equity avg `2.0105` n `74`; fx avg `-0.1606` n `6`; index avg `0.4131` n `23`; metal avg `0.6332` n `18`; unknown avg `-4.7043` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
