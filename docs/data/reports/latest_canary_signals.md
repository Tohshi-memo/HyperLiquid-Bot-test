# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T15:52:32.872421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1078` n `13`; crypto_alt avg `0.2787` n `239`; crypto_major avg `0.3593` n `8`; equity avg `0.169` n `158`; fx avg `0.0046` n `6`; index avg `0.0287` n `27`; metal avg `0.0601` n `20`; unknown avg `0.1804` n `1263`
- 1h: commodity avg `0.0019` n `13`; crypto_alt avg `-0.0707` n `239`; crypto_major avg `0.1543` n `8`; equity avg `0.1501` n `158`; fx avg `0.0051` n `6`; index avg `0.0368` n `27`; metal avg `-0.0562` n `20`; unknown avg `-0.2262` n `1257`
- 4h: commodity avg `-0.7198` n `13`; crypto_alt avg `0.673` n `239`; crypto_major avg `1.2162` n `8`; equity avg `1.6237` n `158`; fx avg `0.0324` n `6`; index avg `0.1865` n `27`; metal avg `0.2588` n `20`; unknown avg `25.1644` n `1249`
- 24h: commodity avg `-0.416` n `13`; crypto_alt avg `-0.3125` n `239`; crypto_major avg `0.501` n `8`; equity avg `-0.9849` n `158`; fx avg `0.0367` n `6`; index avg `-0.0947` n `27`; metal avg `-0.5317` n `20`; unknown avg `0.0235` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
