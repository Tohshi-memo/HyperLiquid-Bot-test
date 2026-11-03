# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T19:38:42.381239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `13`; crypto_alt avg `-0.1389` n `239`; crypto_major avg `-0.1454` n `8`; equity avg `0.0172` n `158`; fx avg `-0.0074` n `6`; index avg `-0.0146` n `27`; metal avg `-0.0069` n `20`; unknown avg `24.7824` n `1263`
- 1h: commodity avg `0.0704` n `13`; crypto_alt avg `-0.1627` n `239`; crypto_major avg `-0.3553` n `8`; equity avg `-0.2776` n `158`; fx avg `0.0017` n `6`; index avg `-0.0531` n `27`; metal avg `-0.0605` n `20`; unknown avg `21.203` n `1257`
- 4h: commodity avg `0.1246` n `13`; crypto_alt avg `-0.0531` n `239`; crypto_major avg `-0.1624` n `8`; equity avg `-0.2763` n `158`; fx avg `0.0408` n `6`; index avg `-0.0367` n `27`; metal avg `-0.1165` n `20`; unknown avg `-0.2012` n `1215`
- 24h: commodity avg `0.1953` n `13`; crypto_alt avg `1.4021` n `239`; crypto_major avg `1.6407` n `8`; equity avg `1.3794` n `158`; fx avg `0.079` n `6`; index avg `0.1223` n `27`; metal avg `-0.5017` n `20`; unknown avg `371.11` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
