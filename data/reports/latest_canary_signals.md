# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T04:07:26.819818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.1267` n `236`; crypto_major avg `-0.1027` n `8`; equity avg `0.0319` n `151`; fx avg `-0.0015` n `6`; index avg `0.0126` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.1469` n `1185`
- 1h: commodity avg `0.0229` n `13`; crypto_alt avg `0.3052` n `236`; crypto_major avg `0.1884` n `8`; equity avg `0.057` n `151`; fx avg `-0.0015` n `6`; index avg `0.0124` n `26`; metal avg `0.0185` n `20`; unknown avg `-0.0662` n `1185`
- 4h: commodity avg `0.0856` n `13`; crypto_alt avg `-0.2021` n `236`; crypto_major avg `-0.0854` n `8`; equity avg `0.1683` n `151`; fx avg `-0.0093` n `6`; index avg `0.0232` n `26`; metal avg `0.0117` n `20`; unknown avg `0.192` n `1183`
- 24h: commodity avg `0.6459` n `13`; crypto_alt avg `-0.9454` n `236`; crypto_major avg `-0.8879` n `8`; equity avg `-4.2879` n `151`; fx avg `-0.0498` n `6`; index avg `-0.6906` n `26`; metal avg `-0.2815` n `20`; unknown avg `40.5128` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1726`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.119`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0762`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0714`, n `666`, weak_sample_signal
