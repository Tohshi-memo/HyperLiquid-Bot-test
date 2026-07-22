# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T20:37:42.316956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.0228` n `230`; crypto_major avg `-0.0374` n `8`; equity avg `-0.1284` n `98`; fx avg `-0.004` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0954` n `773`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.169` n `230`; crypto_major avg `0.0457` n `8`; equity avg `0.2031` n `98`; fx avg `-0.0007` n `6`; index avg `0.0371` n `25`; metal avg `0.0126` n `20`; unknown avg `0.0163` n `773`
- 4h: commodity avg `0.0914` n `12`; crypto_alt avg `-0.4687` n `230`; crypto_major avg `-0.4552` n `8`; equity avg `-0.4255` n `98`; fx avg `0.0123` n `6`; index avg `-0.0493` n `25`; metal avg `-0.0814` n `20`; unknown avg `0.1903` n `773`
- 24h: commodity avg `0.5506` n `12`; crypto_alt avg `-0.4125` n `230`; crypto_major avg `-0.6652` n `8`; equity avg `-0.8517` n `98`; fx avg `-0.0662` n `6`; index avg `-0.0968` n `25`; metal avg `0.2737` n `20`; unknown avg `0.8658` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
