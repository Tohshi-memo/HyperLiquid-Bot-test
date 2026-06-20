# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T15:22:26.284019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.4851` n `228`; crypto_major avg `0.4416` n `8`; equity avg `0.1198` n `78`; fx avg `-0.0163` n `6`; index avg `0.012` n `23`; metal avg `0.0346` n `18`; unknown avg `0.062` n `701`
- 1h: commodity avg `-0.1289` n `12`; crypto_alt avg `1.5639` n `228`; crypto_major avg `1.4476` n `8`; equity avg `0.4147` n `78`; fx avg `-0.0148` n `6`; index avg `0.0255` n `23`; metal avg `0.1153` n `18`; unknown avg `1.5845` n `701`
- 4h: commodity avg `0.1759` n `12`; crypto_alt avg `0.5061` n `228`; crypto_major avg `0.4659` n `8`; equity avg `0.1188` n `78`; fx avg `-0.0006` n `6`; index avg `-0.0016` n `23`; metal avg `0.0495` n `18`; unknown avg `1.6335` n `573`
- 24h: commodity avg `0.626` n `12`; crypto_alt avg `-2.633` n `228`; crypto_major avg `-2.9617` n `8`; equity avg `1.2704` n `78`; fx avg `-0.0726` n `6`; index avg `0.2916` n `23`; metal avg `-4.0551` n `18`; unknown avg `-0.1434` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
