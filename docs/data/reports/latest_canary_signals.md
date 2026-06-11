# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T03:52:24.335657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `0.1048` n `228`; crypto_major avg `0.09` n `8`; equity avg `0.1802` n `74`; fx avg `0.0066` n `6`; index avg `0.1194` n `23`; metal avg `0.0533` n `18`; unknown avg `-0.0171` n `550`
- 1h: commodity avg `0.1092` n `12`; crypto_alt avg `0.6371` n `228`; crypto_major avg `0.6407` n `8`; equity avg `0.4702` n `74`; fx avg `-0.0243` n `6`; index avg `0.2183` n `23`; metal avg `0.3101` n `18`; unknown avg `1.6032` n `550`
- 4h: commodity avg `-0.1795` n `12`; crypto_alt avg `1.646` n `228`; crypto_major avg `1.5462` n `8`; equity avg `1.2028` n `74`; fx avg `0.0835` n `6`; index avg `0.4473` n `23`; metal avg `0.8435` n `18`; unknown avg `1.4204` n `550`
- 24h: commodity avg `1.5968` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.0454` n `8`; equity avg `-0.699` n `74`; fx avg `0.0263` n `6`; index avg `-0.9328` n `23`; metal avg `-0.8843` n `18`; unknown avg `0.3011` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
