# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T11:22:22.159714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1034` n `12`; crypto_alt avg `0.006` n `228`; crypto_major avg `0.0058` n `8`; equity avg `0.1088` n `67`; fx avg `0.0057` n `6`; index avg `0.0396` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.2425` n `419`
- 1h: commodity avg `0.4294` n `12`; crypto_alt avg `-0.3813` n `228`; crypto_major avg `-0.1256` n `8`; equity avg `-0.1303` n `67`; fx avg `0.0043` n `6`; index avg `-0.0611` n `23`; metal avg `-0.2262` n `18`; unknown avg `0.0586` n `419`
- 4h: commodity avg `0.1758` n `12`; crypto_alt avg `-0.773` n `228`; crypto_major avg `-0.3712` n `8`; equity avg `-0.2746` n `67`; fx avg `-0.0556` n `6`; index avg `-0.1652` n `23`; metal avg `-0.3518` n `18`; unknown avg `-0.0587` n `419`
- 24h: commodity avg `0.5714` n `12`; crypto_alt avg `-5.4856` n `228`; crypto_major avg `-3.9919` n `8`; equity avg `-1.9732` n `67`; fx avg `-0.1057` n `6`; index avg `-1.2661` n `23`; metal avg `-1.1792` n `18`; unknown avg `-1.5097` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
