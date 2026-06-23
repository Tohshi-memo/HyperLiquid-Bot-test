# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T16:07:38.568119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.5477` n `228`; crypto_major avg `0.6875` n `8`; equity avg `0.4146` n `86`; fx avg `0.0009` n `6`; index avg `0.0543` n `23`; metal avg `0.0238` n `20`; unknown avg `0.3907` n `764`
- 1h: commodity avg `-0.0729` n `12`; crypto_alt avg `0.2284` n `228`; crypto_major avg `0.3912` n `8`; equity avg `0.2474` n `86`; fx avg `-0.0258` n `6`; index avg `0.0029` n `23`; metal avg `0.094` n `20`; unknown avg `-0.0795` n `764`
- 4h: commodity avg `-0.1535` n `12`; crypto_alt avg `0.0245` n `228`; crypto_major avg `-0.124` n `8`; equity avg `0.6128` n `86`; fx avg `-0.09` n `6`; index avg `-0.014` n `23`; metal avg `0.1432` n `20`; unknown avg `-0.3647` n `764`
- 24h: commodity avg `-0.3608` n `12`; crypto_alt avg `-3.3504` n `228`; crypto_major avg `-3.5591` n `8`; equity avg `-2.689` n `86`; fx avg `-0.2044` n `6`; index avg `-0.8469` n `23`; metal avg `-0.8172` n `20`; unknown avg `-0.1728` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
