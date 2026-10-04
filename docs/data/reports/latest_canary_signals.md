# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T08:37:33.799091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `-0.0379` n `235`; crypto_major avg `-0.0097` n `8`; equity avg `-0.0094` n `143`; fx avg `0.0` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0011` n `20`; unknown avg `3.0309` n `1079`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `0.1883` n `235`; crypto_major avg `0.2298` n `8`; equity avg `0.0015` n `143`; fx avg `0.0012` n `6`; index avg `-0.0009` n `26`; metal avg `0.0019` n `20`; unknown avg `2.7569` n `1061`
- 4h: commodity avg `0.0102` n `13`; crypto_alt avg `0.432` n `235`; crypto_major avg `0.4039` n `8`; equity avg `-0.0015` n `143`; fx avg `-0.0159` n `6`; index avg `-0.0016` n `26`; metal avg `0.0012` n `20`; unknown avg `3.1023` n `1033`
- 24h: commodity avg `0.1213` n `13`; crypto_alt avg `2.6558` n `235`; crypto_major avg `1.3443` n `8`; equity avg `0.2393` n `143`; fx avg `-0.041` n `6`; index avg `0.0179` n `26`; metal avg `0.0062` n `20`; unknown avg `0.3515` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
