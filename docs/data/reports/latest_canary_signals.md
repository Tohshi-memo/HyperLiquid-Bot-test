# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T00:37:25.794187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `-0.1641` n `230`; crypto_major avg `-0.2395` n `8`; equity avg `-0.1028` n `94`; fx avg `0.0063` n `6`; index avg `-0.0412` n `25`; metal avg `-0.0341` n `20`; unknown avg `-0.1241` n `768`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1951` n `230`; crypto_major avg `-0.3884` n `8`; equity avg `-0.3593` n `94`; fx avg `0.0117` n `6`; index avg `-0.1051` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.028` n `766`
- 4h: commodity avg `-0.1159` n `12`; crypto_alt avg `-0.2428` n `230`; crypto_major avg `-0.4626` n `8`; equity avg `-0.4575` n `94`; fx avg `-0.0002` n `6`; index avg `-0.1089` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.1807` n `766`
- 24h: commodity avg `-0.1539` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.1795` n `8`; equity avg `-1.3526` n `93`; fx avg `0.1605` n `6`; index avg `-0.326` n `25`; metal avg `0.0927` n `20`; unknown avg `0.0663` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
