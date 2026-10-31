# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T18:22:31.835205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `0.0471` n `238`; crypto_major avg `0.0561` n `8`; equity avg `0.0315` n `156`; fx avg `0.0095` n `6`; index avg `0.0078` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.3514` n `1260`
- 1h: commodity avg `0.0363` n `13`; crypto_alt avg `-0.0807` n `238`; crypto_major avg `0.2527` n `8`; equity avg `0.0582` n `156`; fx avg `-0.0046` n `6`; index avg `0.0096` n `27`; metal avg `-0.0127` n `20`; unknown avg `-0.6272` n `1216`
- 4h: commodity avg `-0.0238` n `13`; crypto_alt avg `0.5161` n `238`; crypto_major avg `0.5389` n `8`; equity avg `0.124` n `156`; fx avg `0.0008` n `6`; index avg `0.0105` n `27`; metal avg `0.0036` n `20`; unknown avg `0.3269` n `1196`
- 24h: commodity avg `-0.3974` n `13`; crypto_alt avg `1.5418` n `238`; crypto_major avg `0.6756` n `8`; equity avg `1.5923` n `156`; fx avg `-0.018` n `6`; index avg `0.1045` n `27`; metal avg `0.1745` n `20`; unknown avg `0.9987` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
