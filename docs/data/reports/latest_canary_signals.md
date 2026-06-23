# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T16:38:00.231747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1033` n `12`; crypto_alt avg `-0.0466` n `228`; crypto_major avg `-0.0903` n `8`; equity avg `-0.0103` n `86`; fx avg `-0.0094` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0215` n `20`; unknown avg `0.0998` n `764`
- 1h: commodity avg `-0.1328` n `12`; crypto_alt avg `0.3233` n `228`; crypto_major avg `0.4624` n `8`; equity avg `0.4854` n `86`; fx avg `-0.0063` n `6`; index avg `0.0909` n `23`; metal avg `0.0096` n `20`; unknown avg `0.7925` n `764`
- 4h: commodity avg `-0.2307` n `12`; crypto_alt avg `-0.0032` n `228`; crypto_major avg `-0.1251` n `8`; equity avg `1.0632` n `86`; fx avg `-0.0687` n `6`; index avg `0.0865` n `23`; metal avg `0.22` n `20`; unknown avg `-0.1452` n `764`
- 24h: commodity avg `-0.5587` n `12`; crypto_alt avg `-3.5811` n `228`; crypto_major avg `-3.8216` n `8`; equity avg `-2.5651` n `86`; fx avg `-0.1868` n `6`; index avg `-0.8519` n `23`; metal avg `-0.9039` n `20`; unknown avg `-0.1304` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
