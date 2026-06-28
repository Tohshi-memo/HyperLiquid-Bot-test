# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T00:22:27.087417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.1961` n `228`; crypto_major avg `0.1142` n `8`; equity avg `0.0298` n `88`; fx avg `-0.0025` n `6`; index avg `-0.0089` n `23`; metal avg `0.0068` n `20`; unknown avg `-0.0132` n `764`
- 1h: commodity avg `0.1368` n `12`; crypto_alt avg `0.2876` n `228`; crypto_major avg `0.0893` n `8`; equity avg `0.0418` n `88`; fx avg `-0.023` n `6`; index avg `0.0084` n `23`; metal avg `0.0499` n `20`; unknown avg `13.136` n `764`
- 4h: commodity avg `0.2188` n `12`; crypto_alt avg `-0.2033` n `228`; crypto_major avg `-0.4049` n `8`; equity avg `-0.0006` n `88`; fx avg `-0.0171` n `6`; index avg `-0.0574` n `23`; metal avg `0.0377` n `20`; unknown avg `-0.5225` n `764`
- 24h: commodity avg `0.2272` n `12`; crypto_alt avg `-0.6098` n `228`; crypto_major avg `-0.9553` n `8`; equity avg `0.2592` n `88`; fx avg `0.0067` n `6`; index avg `-0.0669` n `23`; metal avg `-0.0356` n `20`; unknown avg `-0.7721` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
