# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T19:07:26.792062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1096` n `12`; crypto_alt avg `-0.0042` n `228`; crypto_major avg `-0.0224` n `8`; equity avg `0.0105` n `74`; fx avg `-0.0136` n `6`; index avg `0.0008` n `23`; metal avg `0.0064` n `18`; unknown avg `0.0234` n `645`
- 1h: commodity avg `0.3426` n `12`; crypto_alt avg `0.1198` n `228`; crypto_major avg `0.0816` n `8`; equity avg `0.0337` n `74`; fx avg `-0.0272` n `6`; index avg `-0.0127` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.3455` n `645`
- 4h: commodity avg `0.2136` n `12`; crypto_alt avg `-0.0287` n `228`; crypto_major avg `-0.1075` n `8`; equity avg `-0.093` n `74`; fx avg `-0.0069` n `6`; index avg `0.0479` n `23`; metal avg `-0.0083` n `18`; unknown avg `-0.4326` n `645`
- 24h: commodity avg `0.2256` n `12`; crypto_alt avg `-1.2434` n `228`; crypto_major avg `-0.6142` n `8`; equity avg `0.3213` n `74`; fx avg `-0.0738` n `6`; index avg `0.1976` n `23`; metal avg `-0.0924` n `18`; unknown avg `0.9364` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
