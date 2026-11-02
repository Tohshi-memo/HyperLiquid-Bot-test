# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T04:52:38.521679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `13`; crypto_alt avg `-0.0874` n `238`; crypto_major avg `-0.1816` n `8`; equity avg `-0.0673` n `156`; fx avg `-0.0136` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0126` n `20`; unknown avg `0.5065` n `1263`
- 1h: commodity avg `-0.0054` n `13`; crypto_alt avg `-0.4143` n `238`; crypto_major avg `-0.3622` n `8`; equity avg `-0.0856` n `156`; fx avg `-0.0117` n `6`; index avg `0.0199` n `27`; metal avg `-0.0135` n `20`; unknown avg `0.5618` n `1249`
- 4h: commodity avg `-0.3778` n `13`; crypto_alt avg `0.16` n `238`; crypto_major avg `0.4628` n `8`; equity avg `0.8921` n `156`; fx avg `0.0861` n `6`; index avg `0.1196` n `27`; metal avg `-0.1164` n `20`; unknown avg `2.0125` n `1195`
- 24h: commodity avg `-0.3723` n `13`; crypto_alt avg `-0.7557` n `238`; crypto_major avg `0.3268` n `8`; equity avg `1.375` n `156`; fx avg `0.2053` n `6`; index avg `0.3578` n `27`; metal avg `0.0418` n `20`; unknown avg `3.7872` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
