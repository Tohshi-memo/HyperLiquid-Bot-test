# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T05:52:32.201541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0584` n `12`; crypto_alt avg `0.069` n `228`; crypto_major avg `0.0069` n `8`; equity avg `-0.069` n `86`; fx avg `-0.0003` n `6`; index avg `0.0015` n `23`; metal avg `-0.1366` n `20`; unknown avg `0.2739` n `708`
- 1h: commodity avg `-0.0938` n `12`; crypto_alt avg `-0.4108` n `228`; crypto_major avg `-0.4077` n `8`; equity avg `-0.6494` n `86`; fx avg `-0.0127` n `6`; index avg `-0.1309` n `23`; metal avg `-0.1609` n `20`; unknown avg `-0.9089` n `708`
- 4h: commodity avg `-0.113` n `12`; crypto_alt avg `-0.1371` n `228`; crypto_major avg `-0.528` n `8`; equity avg `-1.6809` n `86`; fx avg `-0.0274` n `6`; index avg `-0.3519` n `23`; metal avg `-0.4633` n `20`; unknown avg `-0.1872` n `700`
- 24h: commodity avg `-0.5357` n `12`; crypto_alt avg `-1.3524` n `228`; crypto_major avg `-1.385` n `8`; equity avg `-3.4582` n `85`; fx avg `-0.0477` n `6`; index avg `-0.5853` n `23`; metal avg `-1.2507` n `18`; unknown avg `1.1291` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
