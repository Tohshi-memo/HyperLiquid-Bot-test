# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T15:22:42.959115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0392` n `12`; crypto_alt avg `-0.1095` n `228`; crypto_major avg `-0.1964` n `8`; equity avg `-0.2445` n `86`; fx avg `-0.0023` n `6`; index avg `-0.0261` n `23`; metal avg `-0.0386` n `20`; unknown avg `-0.1252` n `764`
- 1h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.6226` n `228`; crypto_major avg `-0.7355` n `8`; equity avg `-0.8007` n `86`; fx avg `-0.0328` n `6`; index avg `-0.1644` n `23`; metal avg `-0.057` n `20`; unknown avg `-0.305` n `764`
- 4h: commodity avg `-0.1808` n `12`; crypto_alt avg `-0.1974` n `228`; crypto_major avg `-0.6482` n `8`; equity avg `0.3913` n `86`; fx avg `-0.0863` n `6`; index avg `0.0106` n `23`; metal avg `-0.0388` n `20`; unknown avg `-0.2036` n `764`
- 24h: commodity avg `-0.3122` n `12`; crypto_alt avg `-4.198` n `228`; crypto_major avg `-4.8146` n `8`; equity avg `-3.3112` n `85`; fx avg `-0.1668` n `6`; index avg `-0.8984` n `23`; metal avg `-1.1139` n `20`; unknown avg `-0.1768` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
