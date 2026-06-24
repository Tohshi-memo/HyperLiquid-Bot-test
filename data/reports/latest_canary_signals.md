# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T11:22:33.297959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.2552` n `228`; crypto_major avg `-0.1993` n `8`; equity avg `-0.1231` n `86`; fx avg `0.0052` n `6`; index avg `-0.025` n `23`; metal avg `-0.2015` n `20`; unknown avg `-0.0042` n `764`
- 1h: commodity avg `-0.0546` n `12`; crypto_alt avg `-0.4818` n `228`; crypto_major avg `-0.4912` n `8`; equity avg `-0.2476` n `86`; fx avg `-0.0035` n `6`; index avg `-0.0324` n `23`; metal avg `-0.3357` n `20`; unknown avg `-0.0349` n `764`
- 4h: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.829` n `228`; crypto_major avg `-0.8885` n `8`; equity avg `-0.2332` n `86`; fx avg `-0.0392` n `6`; index avg `-0.0049` n `23`; metal avg `-0.7687` n `20`; unknown avg `-0.2985` n `764`
- 24h: commodity avg `-0.4929` n `12`; crypto_alt avg `-0.8906` n `228`; crypto_major avg `-0.9215` n `8`; equity avg `4.3213` n `86`; fx avg `-0.028` n `6`; index avg `0.1009` n `23`; metal avg `-1.0322` n `20`; unknown avg `-0.0644` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
