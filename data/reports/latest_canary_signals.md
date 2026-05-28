# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T21:22:21.714984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4736` n `12`; crypto_alt avg `0.2108` n `228`; crypto_major avg `0.2718` n `8`; equity avg `0.0154` n `69`; fx avg `0.0023` n `6`; index avg `-0.0133` n `23`; metal avg `0.0184` n `18`; unknown avg `-0.0008` n `417`
- 1h: commodity avg `-0.4329` n `12`; crypto_alt avg `0.2854` n `228`; crypto_major avg `0.2453` n `8`; equity avg `0.074` n `69`; fx avg `0.011` n `6`; index avg `-0.0213` n `23`; metal avg `-0.0153` n `18`; unknown avg `-0.0745` n `417`
- 4h: commodity avg `-0.2092` n `12`; crypto_alt avg `0.75` n `228`; crypto_major avg `0.6601` n `8`; equity avg `0.7069` n `69`; fx avg `0.0111` n `6`; index avg `-0.1511` n `23`; metal avg `-0.0529` n `18`; unknown avg `0.3923` n `417`
- 24h: commodity avg `0.6021` n `12`; crypto_alt avg `-3.2989` n `228`; crypto_major avg `-0.9194` n `8`; equity avg `1.7083` n `69`; fx avg `0.0034` n `6`; index avg `0.6632` n `23`; metal avg `0.4992` n `18`; unknown avg `-0.5891` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
