# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T20:37:28.581588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.2268` n `228`; crypto_major avg `-0.4022` n `8`; equity avg `-0.486` n `73`; fx avg `0.0076` n `6`; index avg `-0.0915` n `23`; metal avg `-0.1102` n `18`; unknown avg `-0.0332` n `419`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.6808` n `228`; crypto_major avg `-0.6614` n `8`; equity avg `-0.8973` n `73`; fx avg `-0.0017` n `6`; index avg `-0.2682` n `23`; metal avg `-0.3609` n `18`; unknown avg `-0.2763` n `419`
- 4h: commodity avg `-0.0422` n `12`; crypto_alt avg `-0.3038` n `228`; crypto_major avg `-0.5398` n `8`; equity avg `-0.6005` n `73`; fx avg `0.028` n `6`; index avg `-0.1723` n `23`; metal avg `-0.4325` n `18`; unknown avg `-0.3775` n `419`
- 24h: commodity avg `0.9775` n `12`; crypto_alt avg `0.5727` n `228`; crypto_major avg `-2.2005` n `8`; equity avg `-2.929` n `72`; fx avg `0.0636` n `6`; index avg `-0.6207` n `23`; metal avg `-2.359` n `18`; unknown avg `-0.063` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0418`, n `668`, weak_sample_signal
