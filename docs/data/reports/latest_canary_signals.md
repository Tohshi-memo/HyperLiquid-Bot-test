# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T04:37:27.887164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0913` n `13`; crypto_alt avg `-0.436` n `235`; crypto_major avg `-0.0935` n `8`; equity avg `-0.0645` n `144`; fx avg `0.0217` n `6`; index avg `-0.0182` n `26`; metal avg `-0.0059` n `20`; unknown avg `1.6582` n `1079`
- 1h: commodity avg `0.0397` n `13`; crypto_alt avg `-0.7475` n `235`; crypto_major avg `-0.5901` n `8`; equity avg `-0.2092` n `144`; fx avg `0.0279` n `6`; index avg `-0.0375` n `26`; metal avg `-0.0873` n `20`; unknown avg `3.1716` n `1033`
- 4h: commodity avg `-0.041` n `13`; crypto_alt avg `-0.7714` n `235`; crypto_major avg `-0.4227` n `8`; equity avg `-0.2365` n `144`; fx avg `-0.0953` n `6`; index avg `-0.0701` n `26`; metal avg `-0.1484` n `20`; unknown avg `1.6739` n `980`
- 24h: commodity avg `-0.2664` n `13`; crypto_alt avg `-0.0554` n `235`; crypto_major avg `0.7501` n `8`; equity avg `0.2168` n `144`; fx avg `-0.0811` n `6`; index avg `-0.0486` n `26`; metal avg `0.0169` n `20`; unknown avg `0.4051` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
