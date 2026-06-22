# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T16:16:15.797398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `0.0236` n `228`; crypto_major avg `0.0601` n `8`; equity avg `0.0268` n `85`; fx avg `-0.0002` n `6`; index avg `0.0236` n `23`; metal avg `0.0182` n `20`; unknown avg `-0.0162` n `717`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `-0.5339` n `228`; crypto_major avg `-0.6764` n `8`; equity avg `-0.1112` n `85`; fx avg `0.0139` n `6`; index avg `-0.0004` n `23`; metal avg `-0.1549` n `20`; unknown avg `0.1509` n `716`
- 4h: commodity avg `-0.2642` n `12`; crypto_alt avg `-0.972` n `228`; crypto_major avg `-0.907` n `8`; equity avg `-0.8542` n `85`; fx avg `-0.0577` n `6`; index avg `-0.0361` n `23`; metal avg `-0.392` n `20`; unknown avg `0.206` n `716`
- 24h: commodity avg `-0.7895` n `12`; crypto_alt avg `-0.6035` n `228`; crypto_major avg `-0.3446` n `8`; equity avg `-0.6249` n `85`; fx avg `-0.0252` n `6`; index avg `0.1247` n `23`; metal avg `0.1196` n `18`; unknown avg `0.7628` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
