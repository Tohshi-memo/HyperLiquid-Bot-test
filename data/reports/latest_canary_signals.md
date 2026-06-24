# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T09:49:18.118102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `-0.0106` n `228`; crypto_major avg `0.0924` n `8`; equity avg `-0.0671` n `86`; fx avg `0.0017` n `6`; index avg `-0.0075` n `23`; metal avg `0.0034` n `20`; unknown avg `-0.024` n `764`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `-0.1518` n `228`; crypto_major avg `-0.2153` n `8`; equity avg `-0.1433` n `86`; fx avg `0.0178` n `6`; index avg `-0.0363` n `23`; metal avg `-0.0454` n `20`; unknown avg `-0.1489` n `764`
- 4h: commodity avg `-0.0537` n `12`; crypto_alt avg `-0.3589` n `228`; crypto_major avg `-0.3498` n `8`; equity avg `-0.1142` n `86`; fx avg `0.0501` n `6`; index avg `0.0144` n `23`; metal avg `-0.1688` n `20`; unknown avg `-0.2612` n `740`
- 24h: commodity avg `-0.4089` n `12`; crypto_alt avg `0.1578` n `228`; crypto_major avg `0.136` n `8`; equity avg `4.5908` n `86`; fx avg `0.0217` n `6`; index avg `0.0416` n `23`; metal avg `-0.5439` n `20`; unknown avg `0.001` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
