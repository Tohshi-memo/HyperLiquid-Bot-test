# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T07:37:28.447421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `0.123` n `239`; crypto_major avg `0.0721` n `8`; equity avg `0.016` n `166`; fx avg `0.0058` n `6`; index avg `0.0043` n `27`; metal avg `-0.0016` n `20`; unknown avg `110.8069` n `1263`
- 1h: commodity avg `-0.0192` n `13`; crypto_alt avg `-0.1564` n `239`; crypto_major avg `0.0018` n `8`; equity avg `-0.0721` n `166`; fx avg `-0.0141` n `6`; index avg `0.0019` n `27`; metal avg `0.0062` n `20`; unknown avg `0.2443` n `1259`
- 4h: commodity avg `-0.0126` n `13`; crypto_alt avg `0.1682` n `239`; crypto_major avg `-0.0054` n `8`; equity avg `-0.1266` n `166`; fx avg `-0.0123` n `6`; index avg `0.0131` n `27`; metal avg `0.0285` n `20`; unknown avg `3.5118` n `1223`
- 24h: commodity avg `-0.0118` n `13`; crypto_alt avg `1.3102` n `239`; crypto_major avg `1.6999` n `8`; equity avg `0.5702` n `166`; fx avg `0.0664` n `6`; index avg `0.1039` n `27`; metal avg `0.0609` n `20`; unknown avg `235.1679` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
