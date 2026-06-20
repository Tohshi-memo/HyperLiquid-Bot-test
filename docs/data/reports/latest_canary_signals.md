# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T10:37:31.039530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `-0.2552` n `228`; crypto_major avg `-0.0927` n `8`; equity avg `-0.0386` n `78`; fx avg `-0.0016` n `6`; index avg `-0.0113` n `23`; metal avg `0.01` n `18`; unknown avg `-0.1477` n `687`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.2026` n `228`; crypto_major avg `-0.1197` n `8`; equity avg `-0.0321` n `78`; fx avg `0.0113` n `6`; index avg `-0.0163` n `23`; metal avg `0.0053` n `18`; unknown avg `-0.0942` n `687`
- 4h: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0133` n `228`; crypto_major avg `-0.1776` n `8`; equity avg `-0.1893` n `78`; fx avg `0.0259` n `6`; index avg `-0.0483` n `23`; metal avg `0.0073` n `18`; unknown avg `-0.2533` n `679`
- 24h: commodity avg `0.5083` n `12`; crypto_alt avg `-3.0734` n `228`; crypto_major avg `-3.4023` n `8`; equity avg `1.1676` n `78`; fx avg `-0.0808` n `6`; index avg `0.2805` n `23`; metal avg `-4.1036` n `18`; unknown avg `-0.1346` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
