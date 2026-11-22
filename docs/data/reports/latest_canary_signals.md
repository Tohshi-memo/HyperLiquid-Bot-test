# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T19:37:26.780815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.1419` n `239`; crypto_major avg `-0.0657` n `8`; equity avg `0.0095` n `166`; fx avg `-0.0105` n `6`; index avg `0.0045` n `27`; metal avg `-0.002` n `20`; unknown avg `1.262` n `1256`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `0.1834` n `239`; crypto_major avg `-0.2075` n `8`; equity avg `-0.0933` n `166`; fx avg `-0.0121` n `6`; index avg `-0.021` n `27`; metal avg `-0.041` n `20`; unknown avg `0.7442` n `1254`
- 4h: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.1864` n `239`; crypto_major avg `-0.1994` n `8`; equity avg `0.0891` n `166`; fx avg `0.0087` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0352` n `20`; unknown avg `327.3739` n `1223`
- 24h: commodity avg `-0.1132` n `13`; crypto_alt avg `0.6476` n `239`; crypto_major avg `0.311` n `8`; equity avg `0.8808` n `166`; fx avg `-0.0151` n `6`; index avg `0.113` n `27`; metal avg `-0.0427` n `20`; unknown avg `236.3524` n `1054`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
