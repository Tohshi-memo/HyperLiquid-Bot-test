# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T10:37:26.708405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.0343` n `230`; crypto_major avg `0.1261` n `8`; equity avg `0.1589` n `98`; fx avg `-0.0039` n `6`; index avg `0.0452` n `25`; metal avg `0.0346` n `20`; unknown avg `0.0579` n `773`
- 1h: commodity avg `0.0569` n `12`; crypto_alt avg `-0.0929` n `230`; crypto_major avg `0.0735` n `8`; equity avg `0.0348` n `98`; fx avg `-0.0191` n `6`; index avg `0.0294` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.0258` n `773`
- 4h: commodity avg `0.2881` n `12`; crypto_alt avg `0.0618` n `230`; crypto_major avg `0.1048` n `8`; equity avg `0.2625` n `98`; fx avg `-0.0053` n `6`; index avg `0.0252` n `25`; metal avg `-0.3184` n `20`; unknown avg `-0.0061` n `773`
- 24h: commodity avg `0.8514` n `12`; crypto_alt avg `-0.2888` n `230`; crypto_major avg `-0.0439` n `8`; equity avg `0.6631` n `98`; fx avg `-0.0931` n `6`; index avg `0.1606` n `25`; metal avg `-0.3748` n `20`; unknown avg `11.4419` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
