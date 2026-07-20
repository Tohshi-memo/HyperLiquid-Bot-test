# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T20:52:27.585485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `-0.1315` n `230`; crypto_major avg `-0.1095` n `8`; equity avg `0.0063` n `98`; fx avg `-0.0063` n `6`; index avg `0.0` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.0134` n `770`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.1293` n `230`; crypto_major avg `0.1488` n `8`; equity avg `-0.1945` n `98`; fx avg `-0.0221` n `6`; index avg `-0.0407` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0064` n `770`
- 4h: commodity avg `0.1417` n `12`; crypto_alt avg `0.0633` n `230`; crypto_major avg `-0.1114` n `8`; equity avg `-0.9695` n `98`; fx avg `-0.0155` n `6`; index avg `-0.1838` n `25`; metal avg `-0.0851` n `20`; unknown avg `-0.0085` n `770`
- 24h: commodity avg `-0.426` n `12`; crypto_alt avg `1.6215` n `230`; crypto_major avg `1.1828` n `8`; equity avg `-0.3428` n `98`; fx avg `-0.2275` n `6`; index avg `0.0091` n `25`; metal avg `0.1134` n `20`; unknown avg `0.263` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
