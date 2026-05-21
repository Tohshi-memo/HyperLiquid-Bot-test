# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T16:22:21.626766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1384` n `12`; crypto_alt avg `-0.2677` n `228`; crypto_major avg `-0.2209` n `8`; equity avg `-0.0454` n `67`; fx avg `0.0076` n `6`; index avg `-0.044` n `23`; metal avg `-0.224` n `18`; unknown avg `-0.1869` n `385`
- 1h: commodity avg `-0.4171` n `12`; crypto_alt avg `-0.2394` n `228`; crypto_major avg `-0.6066` n `8`; equity avg `-0.9027` n `67`; fx avg `-0.0017` n `6`; index avg `0.0287` n `23`; metal avg `0.411` n `18`; unknown avg `0.6596` n `385`
- 4h: commodity avg `-0.0518` n `12`; crypto_alt avg `0.9401` n `228`; crypto_major avg `0.8527` n `8`; equity avg `0.5696` n `67`; fx avg `-0.031` n `6`; index avg `0.1007` n `23`; metal avg `0.9715` n `18`; unknown avg `1.419` n `385`
- 24h: commodity avg `0.3301` n `12`; crypto_alt avg `1.2473` n `228`; crypto_major avg `2.1694` n `8`; equity avg `1.0604` n `66`; fx avg `-0.0023` n `6`; index avg `0.1569` n `23`; metal avg `0.0525` n `18`; unknown avg `7.8201` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
