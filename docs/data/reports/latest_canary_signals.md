# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T12:37:30.616790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `13`; crypto_alt avg `-0.0551` n `235`; crypto_major avg `-0.1319` n `8`; equity avg `0.0251` n `144`; fx avg `0.0222` n `6`; index avg `-0.0054` n `26`; metal avg `0.0015` n `20`; unknown avg `0.6051` n `1079`
- 1h: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.0827` n `235`; crypto_major avg `-0.2885` n `8`; equity avg `-0.0475` n `144`; fx avg `0.0038` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0182` n `20`; unknown avg `2.3597` n `1071`
- 4h: commodity avg `-0.2058` n `13`; crypto_alt avg `-0.1567` n `235`; crypto_major avg `-0.536` n `8`; equity avg `-0.1335` n `144`; fx avg `0.012` n `6`; index avg `0.0181` n `26`; metal avg `-0.0041` n `20`; unknown avg `45.3291` n `1071`
- 24h: commodity avg `-0.2155` n `13`; crypto_alt avg `1.0887` n `235`; crypto_major avg `0.7694` n `8`; equity avg `0.086` n `144`; fx avg `-0.0441` n `6`; index avg `-0.0448` n `26`; metal avg `0.299` n `20`; unknown avg `0.6619` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
