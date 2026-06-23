# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T19:44:58.174898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0634` n `228`; crypto_major avg `0.0747` n `8`; equity avg `0.1207` n `86`; fx avg `-0.0072` n `6`; index avg `-0.0037` n `23`; metal avg `0.0439` n `20`; unknown avg `0.1786` n `764`
- 1h: commodity avg `0.0443` n `12`; crypto_alt avg `0.0655` n `228`; crypto_major avg `-0.0048` n `8`; equity avg `-0.1015` n `86`; fx avg `0.0042` n `6`; index avg `-0.0236` n `23`; metal avg `0.0206` n `20`; unknown avg `0.0551` n `756`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `0.1464` n `228`; crypto_major avg `0.1337` n `8`; equity avg `-0.2897` n `86`; fx avg `-0.0068` n `6`; index avg `-0.0453` n `23`; metal avg `-0.1912` n `20`; unknown avg `-0.0242` n `756`
- 24h: commodity avg `-0.3975` n `12`; crypto_alt avg `-3.1613` n `228`; crypto_major avg `-4.0724` n `8`; equity avg `-3.215` n `86`; fx avg `-0.1789` n `6`; index avg `-0.932` n `23`; metal avg `-1.1164` n `20`; unknown avg `-0.0017` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
