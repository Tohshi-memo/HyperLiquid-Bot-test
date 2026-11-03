# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T08:52:26.253203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `0.178` n `239`; crypto_major avg `0.1096` n `8`; equity avg `-0.0715` n `157`; fx avg `0.005` n `6`; index avg `0.0092` n `27`; metal avg `-0.1117` n `20`; unknown avg `249.4081` n `1264`
- 1h: commodity avg `0.1718` n `13`; crypto_alt avg `-0.1922` n `239`; crypto_major avg `-0.2642` n `8`; equity avg `-0.1167` n `157`; fx avg `0.0398` n `6`; index avg `0.0056` n `27`; metal avg `-0.1864` n `20`; unknown avg `0.1861` n `1242`
- 4h: commodity avg `0.4156` n `13`; crypto_alt avg `-0.5149` n `239`; crypto_major avg `-0.3481` n `8`; equity avg `-0.1975` n `157`; fx avg `0.0792` n `6`; index avg `0.0215` n `27`; metal avg `-0.3784` n `20`; unknown avg `0.3729` n `1210`
- 24h: commodity avg `-0.2403` n `13`; crypto_alt avg `-2.5655` n `238`; crypto_major avg `-1.9834` n `8`; equity avg `-4.3631` n `157`; fx avg `-0.0054` n `6`; index avg `-0.3045` n `27`; metal avg `-0.6919` n `20`; unknown avg `3.948` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
