# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T08:23:04.348869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `0.0914` n `235`; crypto_major avg `0.0312` n `8`; equity avg `0.0134` n `143`; fx avg `0.0` n `6`; index avg `0.0012` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.1324` n `1079`
- 1h: commodity avg `-0.022` n `13`; crypto_alt avg `0.1283` n `235`; crypto_major avg `0.1819` n `8`; equity avg `0.0045` n `143`; fx avg `0.0034` n `6`; index avg `-0.0018` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0275` n `1061`
- 4h: commodity avg `0.0054` n `13`; crypto_alt avg `0.4697` n `235`; crypto_major avg `0.4322` n `8`; equity avg `0.0144` n `143`; fx avg `-0.0159` n `6`; index avg `-0.0038` n `26`; metal avg `0.0059` n `20`; unknown avg `0.2968` n `1033`
- 24h: commodity avg `0.1245` n `13`; crypto_alt avg `2.7121` n `235`; crypto_major avg `1.3236` n `8`; equity avg `0.2407` n `143`; fx avg `-0.0432` n `6`; index avg `0.0191` n `26`; metal avg `-0.002` n `20`; unknown avg `0.3337` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
