# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T08:07:31.774667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.1309` n `239`; crypto_major avg `-0.1061` n `8`; equity avg `-0.0774` n `168`; fx avg `0.0012` n `6`; index avg `0.0011` n `27`; metal avg `-0.0125` n `20`; unknown avg `-0.0442` n `1239`
- 1h: commodity avg `0.0038` n `13`; crypto_alt avg `0.0303` n `239`; crypto_major avg `0.1765` n `8`; equity avg `0.1422` n `168`; fx avg `-0.0133` n `6`; index avg `0.0173` n `27`; metal avg `0.001` n `20`; unknown avg `-0.0033` n `1245`
- 4h: commodity avg `-0.0141` n `13`; crypto_alt avg `-1.4107` n `239`; crypto_major avg `-0.6693` n `8`; equity avg `-0.1064` n `168`; fx avg `-0.0104` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0147` n `20`; unknown avg `175.8645` n `1201`
- 24h: commodity avg `-0.7361` n `13`; crypto_alt avg `-3.1299` n `239`; crypto_major avg `-2.8514` n `8`; equity avg `-0.067` n `168`; fx avg `-0.0964` n `6`; index avg `0.0542` n `27`; metal avg `-0.2629` n `20`; unknown avg `211.306` n `987`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
