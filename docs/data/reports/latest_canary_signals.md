# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T19:22:41.211687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.074` n `12`; crypto_alt avg `0.2543` n `228`; crypto_major avg `0.1586` n `8`; equity avg `0.0388` n `74`; fx avg `0.0114` n `6`; index avg `0.0114` n `23`; metal avg `-0.0037` n `18`; unknown avg `0.0916` n `645`
- 1h: commodity avg `0.1655` n `12`; crypto_alt avg `0.5123` n `228`; crypto_major avg `0.3898` n `8`; equity avg `0.117` n `74`; fx avg `-0.017` n `6`; index avg `0.0093` n `23`; metal avg `0.0012` n `18`; unknown avg `-0.1589` n `645`
- 4h: commodity avg `0.0828` n `12`; crypto_alt avg `0.1645` n `228`; crypto_major avg `0.0328` n `8`; equity avg `-0.0426` n `74`; fx avg `-0.0134` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0046` n `18`; unknown avg `-0.4297` n `645`
- 24h: commodity avg `0.2678` n `12`; crypto_alt avg `-1.0332` n `228`; crypto_major avg `-0.463` n `8`; equity avg `0.3146` n `74`; fx avg `-0.0616` n `6`; index avg `0.2065` n `23`; metal avg `-0.0921` n `18`; unknown avg `1.018` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
