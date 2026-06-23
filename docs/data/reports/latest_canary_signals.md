# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T15:52:35.033070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0733` n `228`; crypto_major avg `-0.0251` n `8`; equity avg `0.1371` n `86`; fx avg `-0.0101` n `6`; index avg `0.0307` n `23`; metal avg `-0.0119` n `20`; unknown avg `-0.0422` n `764`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `-0.7123` n `228`; crypto_major avg `-0.6862` n `8`; equity avg `-0.3808` n `86`; fx avg `-0.0244` n `6`; index avg `-0.0644` n `23`; metal avg `0.0804` n `20`; unknown avg `-0.451` n `764`
- 4h: commodity avg `-0.1344` n `12`; crypto_alt avg `-0.3996` n `228`; crypto_major avg `-0.7104` n `8`; equity avg `0.2504` n `86`; fx avg `-0.1101` n `6`; index avg `-0.0683` n `23`; metal avg `0.1538` n `20`; unknown avg `-0.439` n `764`
- 24h: commodity avg `-0.3345` n `12`; crypto_alt avg `-4.1139` n `228`; crypto_major avg `-4.5193` n `8`; equity avg `-3.2725` n `86`; fx avg `-0.197` n `6`; index avg `-0.913` n `23`; metal avg `-0.8422` n `20`; unknown avg `-0.263` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
