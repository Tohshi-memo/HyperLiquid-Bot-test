# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T23:37:29.195345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0447` n `228`; crypto_major avg `0.1462` n `8`; equity avg `0.0342` n `86`; fx avg `0.032` n `6`; index avg `-0.002` n `23`; metal avg `0.0063` n `20`; unknown avg `-0.0666` n `716`
- 1h: commodity avg `-0.0552` n `12`; crypto_alt avg `0.3535` n `228`; crypto_major avg `0.3305` n `8`; equity avg `-0.0686` n `86`; fx avg `0.0458` n `6`; index avg `-0.011` n `23`; metal avg `0.0142` n `20`; unknown avg `0.0422` n `716`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.8114` n `228`; crypto_major avg `-0.5939` n `8`; equity avg `-0.1027` n `86`; fx avg `0.0367` n `6`; index avg `-0.0056` n `23`; metal avg `0.0291` n `20`; unknown avg `-0.2504` n `708`
- 24h: commodity avg `-0.9169` n `12`; crypto_alt avg `0.1242` n `228`; crypto_major avg `0.5258` n `8`; equity avg `-0.1983` n `85`; fx avg `0.1412` n `6`; index avg `0.2278` n `23`; metal avg `0.4567` n `18`; unknown avg `0.405` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
