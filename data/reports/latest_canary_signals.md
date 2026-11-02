# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T02:22:28.746283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0361` n `13`; crypto_alt avg `0.052` n `238`; crypto_major avg `0.0494` n `8`; equity avg `0.1997` n `156`; fx avg `0.0268` n `6`; index avg `0.0205` n `27`; metal avg `0.0032` n `20`; unknown avg `454.0545` n `1263`
- 1h: commodity avg `-0.1166` n `13`; crypto_alt avg `-0.2658` n `238`; crypto_major avg `-0.2099` n `8`; equity avg `-0.1544` n `156`; fx avg `0.0383` n `6`; index avg `0.0031` n `27`; metal avg `0.0083` n `20`; unknown avg `450.046` n `1251`
- 4h: commodity avg `-0.2028` n `13`; crypto_alt avg `0.5067` n `238`; crypto_major avg `1.1276` n `8`; equity avg `0.8118` n `156`; fx avg `0.1547` n `6`; index avg `0.2284` n `27`; metal avg `0.1331` n `20`; unknown avg `813.0682` n `1229`
- 24h: commodity avg `-0.1797` n `13`; crypto_alt avg `-0.2308` n `238`; crypto_major avg `0.4541` n `8`; equity avg `1.0283` n `156`; fx avg `0.1486` n `6`; index avg `0.2915` n `27`; metal avg `0.1376` n `20`; unknown avg `486.6137` n `1120`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
