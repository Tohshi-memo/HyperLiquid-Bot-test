# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T14:22:39.085727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `-0.7029` n `237`; crypto_major avg `-0.6396` n `8`; equity avg `-0.1559` n `152`; fx avg `0.007` n `6`; index avg `-0.0438` n `26`; metal avg `-0.1174` n `20`; unknown avg `0.6792` n `1233`
- 1h: commodity avg `0.2045` n `13`; crypto_alt avg `-0.5271` n `237`; crypto_major avg `-0.3928` n `8`; equity avg `0.1419` n `152`; fx avg `0.048` n `6`; index avg `0.0139` n `26`; metal avg `-0.185` n `20`; unknown avg `0.162` n `1167`
- 4h: commodity avg `0.0354` n `13`; crypto_alt avg `-0.7582` n `237`; crypto_major avg `-0.5406` n `8`; equity avg `-0.5244` n `152`; fx avg `0.0233` n `6`; index avg `-0.0693` n `26`; metal avg `-0.1509` n `20`; unknown avg `-0.0729` n `1161`
- 24h: commodity avg `0.3653` n `13`; crypto_alt avg `-0.5058` n `237`; crypto_major avg `-0.2986` n `8`; equity avg `-1.1319` n `152`; fx avg `-0.0261` n `6`; index avg `-0.2118` n `26`; metal avg `-0.414` n `20`; unknown avg `-0.3702` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
