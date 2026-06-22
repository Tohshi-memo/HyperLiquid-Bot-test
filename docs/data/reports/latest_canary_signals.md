# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T21:37:29.103765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.062` n `228`; crypto_major avg `-0.0386` n `8`; equity avg `0.0018` n `85`; fx avg `-0.0098` n `6`; index avg `0.0186` n `23`; metal avg `0.0077` n `20`; unknown avg `0.0692` n `717`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.2701` n `228`; crypto_major avg `-0.2552` n `8`; equity avg `0.0377` n `85`; fx avg `-0.0379` n `6`; index avg `0.011` n `23`; metal avg `0.0287` n `20`; unknown avg `-0.2817` n `717`
- 4h: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.4986` n `228`; crypto_major avg `-0.2095` n `8`; equity avg `-0.0144` n `85`; fx avg `-0.0243` n `6`; index avg `-0.0337` n `23`; metal avg `0.1614` n `20`; unknown avg `-0.3546` n `709`
- 24h: commodity avg `-1.0619` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `-0.0711` n `8`; equity avg `-0.5642` n `85`; fx avg `0.1153` n `6`; index avg `0.1141` n `23`; metal avg `0.3785` n `18`; unknown avg `0.4278` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
