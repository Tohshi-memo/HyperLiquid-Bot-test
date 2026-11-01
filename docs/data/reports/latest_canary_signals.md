# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T14:22:26.738592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.0539` n `238`; crypto_major avg `-0.0211` n `8`; equity avg `0.0032` n `156`; fx avg `-0.0134` n `6`; index avg `0.0066` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.0776` n `1263`
- 1h: commodity avg `0.0372` n `13`; crypto_alt avg `-0.0045` n `238`; crypto_major avg `0.1179` n `8`; equity avg `-0.0242` n `156`; fx avg `-0.0004` n `6`; index avg `0.0198` n `27`; metal avg `-0.008` n `20`; unknown avg `0.0055` n `1257`
- 4h: commodity avg `0.0026` n `13`; crypto_alt avg `0.024` n `238`; crypto_major avg `-0.1249` n `8`; equity avg `-0.0495` n `156`; fx avg `0.0012` n `6`; index avg `0.0247` n `27`; metal avg `0.0157` n `20`; unknown avg `-0.038` n `1253`
- 24h: commodity avg `0.0414` n `13`; crypto_alt avg `0.6886` n `238`; crypto_major avg `0.6587` n `8`; equity avg `0.5201` n `156`; fx avg `-0.0118` n `6`; index avg `0.0612` n `27`; metal avg `0.0623` n `20`; unknown avg `1.4411` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
