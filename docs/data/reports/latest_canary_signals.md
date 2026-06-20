# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T04:22:26.613609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0643` n `228`; crypto_major avg `0.0838` n `8`; equity avg `0.0326` n `78`; fx avg `0.0064` n `6`; index avg `0.0058` n `23`; metal avg `0.012` n `18`; unknown avg `-0.1773` n `687`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.1509` n `228`; crypto_major avg `0.1511` n `8`; equity avg `0.1426` n `78`; fx avg `-0.0127` n `6`; index avg `-0.0013` n `23`; metal avg `0.0374` n `18`; unknown avg `1.6925` n `687`
- 4h: commodity avg `0.1448` n `12`; crypto_alt avg `-0.3527` n `228`; crypto_major avg `-0.0259` n `8`; equity avg `0.1438` n `78`; fx avg `-0.0035` n `6`; index avg `0.0179` n `23`; metal avg `-0.0254` n `18`; unknown avg `-0.7198` n `679`
- 24h: commodity avg `0.4342` n `12`; crypto_alt avg `-3.6207` n `228`; crypto_major avg `-4.3749` n `8`; equity avg `1.0997` n `78`; fx avg `-0.0881` n `6`; index avg `0.2949` n `23`; metal avg `-4.1286` n `18`; unknown avg `-0.547` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
