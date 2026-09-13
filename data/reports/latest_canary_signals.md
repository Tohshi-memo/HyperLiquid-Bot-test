# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T21:37:26.433692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.0521` n `233`; crypto_major avg `-0.0782` n `8`; equity avg `0.0271` n `136`; fx avg `0.0053` n `6`; index avg `0.0038` n `27`; metal avg `0.0103` n `20`; unknown avg `0.506` n `840`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `0.0921` n `233`; crypto_major avg `0.0047` n `8`; equity avg `0.1178` n `136`; fx avg `0.0284` n `6`; index avg `0.0192` n `27`; metal avg `0.0353` n `20`; unknown avg `17.4706` n `814`
- 4h: commodity avg `0.0749` n `12`; crypto_alt avg `0.0421` n `233`; crypto_major avg `0.1551` n `8`; equity avg `0.0962` n `136`; fx avg `0.0315` n `6`; index avg `0.0202` n `27`; metal avg `-0.0081` n `20`; unknown avg `5.1999` n `794`
- 24h: commodity avg `0.3402` n `12`; crypto_alt avg `0.2472` n `233`; crypto_major avg `-0.4621` n `8`; equity avg `-1.0697` n `136`; fx avg `0.0499` n `6`; index avg `-0.2147` n `26`; metal avg `-0.0575` n `20`; unknown avg `2.608` n `698`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
