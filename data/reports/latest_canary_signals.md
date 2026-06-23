# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T23:07:30.628744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.273` n `228`; crypto_major avg `-0.1171` n `8`; equity avg `-0.2957` n `86`; fx avg `-0.0021` n `6`; index avg `-0.0693` n `23`; metal avg `-0.0926` n `20`; unknown avg `0.1521` n `756`
- 1h: commodity avg `-0.032` n `12`; crypto_alt avg `-0.5585` n `228`; crypto_major avg `-0.3125` n `8`; equity avg `-0.5173` n `86`; fx avg `-0.0051` n `6`; index avg `-0.1294` n `23`; metal avg `-0.1678` n `20`; unknown avg `-0.0685` n `756`
- 4h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.0995` n `228`; crypto_major avg `0.2239` n `8`; equity avg `-0.3337` n `86`; fx avg `-0.0131` n `6`; index avg `-0.0581` n `23`; metal avg `-0.2004` n `20`; unknown avg `0.115` n `748`
- 24h: commodity avg `-0.4694` n `12`; crypto_alt avg `-1.9514` n `228`; crypto_major avg `-3.0015` n `8`; equity avg `-3.4912` n `86`; fx avg `-0.2088` n `6`; index avg `-0.9571` n `23`; metal avg `-1.334` n `20`; unknown avg `0.6492` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
