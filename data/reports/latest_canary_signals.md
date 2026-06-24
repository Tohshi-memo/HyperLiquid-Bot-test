# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T12:13:42.604420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0497` n `12`; crypto_alt avg `0.0129` n `228`; crypto_major avg `-0.1872` n `8`; equity avg `-0.0462` n `86`; fx avg `0.0012` n `6`; index avg `0.0051` n `23`; metal avg `-0.2568` n `20`; unknown avg `-0.0077` n `764`
- 1h: commodity avg `-0.1598` n `12`; crypto_alt avg `0.7996` n `228`; crypto_major avg `0.7741` n `8`; equity avg `0.184` n `86`; fx avg `-0.0076` n `6`; index avg `0.0526` n `23`; metal avg `-0.3408` n `20`; unknown avg `0.2597` n `764`
- 4h: commodity avg `-0.1222` n `12`; crypto_alt avg `0.3029` n `228`; crypto_major avg `0.2983` n `8`; equity avg `-0.0438` n `86`; fx avg `-0.0302` n `6`; index avg `0.0504` n `23`; metal avg `-0.7916` n `20`; unknown avg `-0.1083` n `764`
- 24h: commodity avg `-0.5761` n `12`; crypto_alt avg `0.0372` n `228`; crypto_major avg `-0.0163` n `8`; equity avg `4.3557` n `86`; fx avg `-0.0213` n `6`; index avg `0.1248` n `23`; metal avg `-1.1204` n `20`; unknown avg `-0.1794` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
