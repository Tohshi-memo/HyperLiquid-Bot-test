# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T17:37:37.708226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.2347` n `239`; crypto_major avg `-0.1681` n `8`; equity avg `-0.0942` n `158`; fx avg `0.002` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0395` n `20`; unknown avg `0.2049` n `1263`
- 1h: commodity avg `0.0553` n `13`; crypto_alt avg `-0.076` n `239`; crypto_major avg `-0.0175` n `8`; equity avg `0.1645` n `158`; fx avg `0.0163` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0614` n `20`; unknown avg `-0.0551` n `1257`
- 4h: commodity avg `0.3874` n `13`; crypto_alt avg `-0.3417` n `239`; crypto_major avg `0.0198` n `8`; equity avg `0.1363` n `158`; fx avg `0.0769` n `6`; index avg `-0.0518` n `27`; metal avg `-0.3025` n `20`; unknown avg `229.9099` n `1251`
- 24h: commodity avg `0.1312` n `13`; crypto_alt avg `0.6297` n `239`; crypto_major avg `1.2456` n `8`; equity avg `-0.2051` n `158`; fx avg `0.0538` n `6`; index avg `-0.0719` n `27`; metal avg `-0.61` n `20`; unknown avg `0.2678` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
