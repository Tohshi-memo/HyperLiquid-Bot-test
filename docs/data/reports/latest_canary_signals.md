# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T11:37:25.553307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.098` n `228`; crypto_major avg `-0.0582` n `8`; equity avg `0.0139` n `78`; fx avg `-0.0001` n `6`; index avg `-0.0086` n `23`; metal avg `0.0079` n `18`; unknown avg `-0.0228` n `702`
- 1h: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.4117` n `228`; crypto_major avg `-0.4878` n `8`; equity avg `-0.0273` n `78`; fx avg `0.0062` n `6`; index avg `-0.0019` n `23`; metal avg `-0.0553` n `18`; unknown avg `-0.0139` n `702`
- 4h: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.0664` n `228`; crypto_major avg `-0.4242` n `8`; equity avg `-0.0985` n `78`; fx avg `0.1` n `6`; index avg `-0.0025` n `23`; metal avg `-0.092` n `18`; unknown avg `-0.3758` n `694`
- 24h: commodity avg `0.1351` n `12`; crypto_alt avg `1.2163` n `228`; crypto_major avg `-0.2711` n `8`; equity avg `0.4053` n `78`; fx avg `0.0261` n `6`; index avg `0.0314` n `23`; metal avg `-0.0672` n `18`; unknown avg `0.4702` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
