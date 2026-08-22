# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T13:06:06.283635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.3088` n `230`; crypto_major avg `-0.1447` n `8`; equity avg `-0.0061` n `121`; fx avg `-0.0012` n `6`; index avg `-0.0051` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0359` n `794`
- 1h: commodity avg `0.0295` n `12`; crypto_alt avg `-0.4353` n `230`; crypto_major avg `-0.1139` n `8`; equity avg `-0.0033` n `121`; fx avg `-0.0023` n `6`; index avg `-0.0039` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0459` n `794`
- 4h: commodity avg `0.007` n `12`; crypto_alt avg `0.058` n `230`; crypto_major avg `0.3174` n `8`; equity avg `-0.0214` n `121`; fx avg `0.0159` n `6`; index avg `0.0023` n `25`; metal avg `0.0361` n `20`; unknown avg `0.3065` n `794`
- 24h: commodity avg `0.0228` n `12`; crypto_alt avg `0.9835` n `230`; crypto_major avg `3.4624` n `8`; equity avg `-0.9541` n `121`; fx avg `0.0606` n `6`; index avg `-0.1347` n `25`; metal avg `-0.1171` n `20`; unknown avg `1.3925` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
