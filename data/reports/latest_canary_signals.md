# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T08:07:27.451170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `-0.008` n `236`; crypto_major avg `-0.003` n `8`; equity avg `0.0024` n `151`; fx avg `-0.0013` n `6`; index avg `0.0117` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.0047` n `1175`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.1927` n `236`; crypto_major avg `0.0279` n `8`; equity avg `-0.0628` n `151`; fx avg `-0.0015` n `6`; index avg `0.0208` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.0575` n `1175`
- 4h: commodity avg `-0.2535` n `13`; crypto_alt avg `-0.2899` n `236`; crypto_major avg `0.1954` n `8`; equity avg `0.0145` n `151`; fx avg `-0.0015` n `6`; index avg `0.0314` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.1621` n `1157`
- 24h: commodity avg `0.3093` n `13`; crypto_alt avg `-1.897` n `236`; crypto_major avg `-1.2123` n `8`; equity avg `-3.8265` n `151`; fx avg `0.0435` n `6`; index avg `-0.5716` n `26`; metal avg `-0.2343` n `20`; unknown avg `39.3806` n `938`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1812`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1461`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
