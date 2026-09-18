# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T01:52:31.770061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.3079` n `234`; crypto_major avg `0.1925` n `8`; equity avg `0.0221` n `140`; fx avg `0.0224` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0203` n `20`; unknown avg `-0.3188` n `919`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.7536` n `234`; crypto_major avg `0.7061` n `8`; equity avg `0.0035` n `140`; fx avg `0.0422` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.1014` n `917`
- 4h: commodity avg `-0.0576` n `12`; crypto_alt avg `1.5926` n `234`; crypto_major avg `1.211` n `8`; equity avg `-0.2446` n `140`; fx avg `0.1257` n `6`; index avg `-0.1234` n `26`; metal avg `0.1238` n `20`; unknown avg `0.1986` n `845`
- 24h: commodity avg `-0.2939` n `12`; crypto_alt avg `3.9122` n `234`; crypto_major avg `2.2476` n `8`; equity avg `1.434` n `138`; fx avg `0.0545` n `6`; index avg `0.1772` n `26`; metal avg `0.3836` n `20`; unknown avg `1.6566` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
