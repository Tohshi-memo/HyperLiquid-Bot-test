# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T15:37:45.553952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `0.1243` n `239`; crypto_major avg `0.0838` n `8`; equity avg `0.0539` n `157`; fx avg `0.0015` n `6`; index avg `0.0059` n `27`; metal avg `0.0051` n `20`; unknown avg `2.7909` n `1264`
- 1h: commodity avg `0.0642` n `13`; crypto_alt avg `-0.1059` n `239`; crypto_major avg `-0.0954` n `8`; equity avg `0.1932` n `157`; fx avg `0.0186` n `6`; index avg `-0.0112` n `27`; metal avg `-0.1344` n `20`; unknown avg `21.4318` n `1258`
- 4h: commodity avg `-0.5878` n `13`; crypto_alt avg `0.6672` n `239`; crypto_major avg `0.9553` n `8`; equity avg `1.3765` n `157`; fx avg `0.0292` n `6`; index avg `0.1427` n `27`; metal avg `0.211` n `20`; unknown avg `24.7358` n `1250`
- 24h: commodity avg `-0.337` n `13`; crypto_alt avg `-0.7326` n `239`; crypto_major avg `-0.0543` n `8`; equity avg `-1.6994` n `157`; fx avg `0.0431` n `6`; index avg `-0.1684` n `27`; metal avg `-0.5462` n `20`; unknown avg `1.6496` n `1022`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
