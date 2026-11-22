# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T08:37:27.137192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.303` n `239`; crypto_major avg `0.4692` n `8`; equity avg `0.367` n `166`; fx avg `0.0076` n `6`; index avg `0.0299` n `27`; metal avg `0.0203` n `20`; unknown avg `316.7347` n `1263`
- 1h: commodity avg `0.0533` n `13`; crypto_alt avg `1.3565` n `239`; crypto_major avg `1.4482` n `8`; equity avg `0.6602` n `166`; fx avg `-0.0014` n `6`; index avg `0.0636` n `27`; metal avg `0.058` n `20`; unknown avg `40.8819` n `1243`
- 4h: commodity avg `0.0311` n `13`; crypto_alt avg `1.151` n `239`; crypto_major avg `1.2252` n `8`; equity avg `0.5609` n `166`; fx avg `0.0024` n `6`; index avg `0.0628` n `27`; metal avg `0.0577` n `20`; unknown avg `206.2863` n `1213`
- 24h: commodity avg `0.0452` n `13`; crypto_alt avg `3.9114` n `239`; crypto_major avg `4.765` n `8`; equity avg `1.5078` n `166`; fx avg `0.0569` n `6`; index avg `0.1965` n `27`; metal avg `0.1538` n `20`; unknown avg `237.1293` n `1068`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
