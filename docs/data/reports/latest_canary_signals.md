# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T18:22:33.044287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `-0.1477` n `239`; crypto_major avg `-0.1403` n `8`; equity avg `-0.0298` n `166`; fx avg `0.0083` n `6`; index avg `0.0058` n `27`; metal avg `-0.0025` n `20`; unknown avg `2.0453` n `1260`
- 1h: commodity avg `0.0227` n `13`; crypto_alt avg `-0.1757` n `239`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0002` n `166`; fx avg `0.0034` n `6`; index avg `-0.0721` n `27`; metal avg `-0.0026` n `20`; unknown avg `226.7243` n `1212`
- 4h: commodity avg `-0.0` n `13`; crypto_alt avg `-0.2283` n `239`; crypto_major avg `-0.2411` n `8`; equity avg `0.005` n `166`; fx avg `0.01` n `6`; index avg `-0.0857` n `27`; metal avg `0.0107` n `20`; unknown avg `497.3444` n `1200`
- 24h: commodity avg `0.4621` n `13`; crypto_alt avg `0.312` n `239`; crypto_major avg `1.1316` n `8`; equity avg `0.1184` n `166`; fx avg `-0.1191` n `6`; index avg `-0.0733` n `27`; metal avg `0.1712` n `20`; unknown avg `415.9844` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
