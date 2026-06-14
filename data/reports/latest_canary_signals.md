# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T20:22:34.053563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `0.1278` n `228`; crypto_major avg `0.1144` n `8`; equity avg `-0.0197` n `74`; fx avg `0.0363` n `6`; index avg `0.0047` n `23`; metal avg `-0.0297` n `18`; unknown avg `-0.3045` n `645`
- 1h: commodity avg `-0.0608` n `12`; crypto_alt avg `-0.0448` n `228`; crypto_major avg `0.0055` n `8`; equity avg `-0.0665` n `74`; fx avg `0.0444` n `6`; index avg `-0.0064` n `23`; metal avg `-0.0757` n `18`; unknown avg `0.092` n `645`
- 4h: commodity avg `0.0961` n `12`; crypto_alt avg `-0.2318` n `228`; crypto_major avg `-0.1332` n `8`; equity avg `-0.1105` n `74`; fx avg `0.0474` n `6`; index avg `-0.0538` n `23`; metal avg `-0.0359` n `18`; unknown avg `0.1194` n `645`
- 24h: commodity avg `0.0893` n `12`; crypto_alt avg `-1.1099` n `228`; crypto_major avg `-0.5282` n `8`; equity avg `0.1863` n `74`; fx avg `-0.0068` n `6`; index avg `0.1214` n `23`; metal avg `-0.1853` n `18`; unknown avg `1.027` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
