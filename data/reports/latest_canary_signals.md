# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T20:22:33.819734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.0398` n `228`; crypto_major avg `0.1741` n `8`; equity avg `-0.1193` n `73`; fx avg `-0.0011` n `6`; index avg `-0.0598` n `23`; metal avg `0.0088` n `18`; unknown avg `-0.0842` n `419`
- 1h: commodity avg `0.1108` n `12`; crypto_alt avg `-0.3164` n `228`; crypto_major avg `-0.1305` n `8`; equity avg `-0.3004` n `73`; fx avg `0.0088` n `6`; index avg `-0.0967` n `23`; metal avg `-0.21` n `18`; unknown avg `-0.2676` n `419`
- 4h: commodity avg `0.0902` n `12`; crypto_alt avg `0.0951` n `228`; crypto_major avg `0.1102` n `8`; equity avg `-0.3835` n `73`; fx avg `0.0193` n `6`; index avg `-0.1212` n `23`; metal avg `-0.3664` n `18`; unknown avg `-0.4659` n `419`
- 24h: commodity avg `0.9509` n `12`; crypto_alt avg `1.3136` n `228`; crypto_major avg `-1.6933` n `8`; equity avg `-2.489` n `72`; fx avg `0.0466` n `6`; index avg `-0.4926` n `23`; metal avg `-2.2242` n `18`; unknown avg `0.1556` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0421`, n `668`, weak_sample_signal
