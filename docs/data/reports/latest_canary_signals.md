# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T10:52:33.434986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0546` n `13`; crypto_alt avg `0.2087` n `237`; crypto_major avg `0.2598` n `8`; equity avg `0.4761` n `151`; fx avg `-0.017` n `6`; index avg `0.0588` n `26`; metal avg `0.0092` n `20`; unknown avg `0.1086` n `1195`
- 1h: commodity avg `0.0376` n `13`; crypto_alt avg `-0.7045` n `237`; crypto_major avg `-0.6654` n `8`; equity avg `0.3191` n `151`; fx avg `0.0033` n `6`; index avg `0.0545` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.4859` n `1193`
- 4h: commodity avg `0.3413` n `13`; crypto_alt avg `-0.654` n `237`; crypto_major avg `-0.5677` n `8`; equity avg `0.2239` n `151`; fx avg `-0.0099` n `6`; index avg `0.0203` n `26`; metal avg `-0.0477` n `20`; unknown avg `0.4285` n `1146`
- 24h: commodity avg `-0.1138` n `13`; crypto_alt avg `-0.3947` n `237`; crypto_major avg `0.2633` n `8`; equity avg `2.7919` n `151`; fx avg `-0.0454` n `6`; index avg `0.4855` n `26`; metal avg `0.2162` n `20`; unknown avg `1.2906` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1993`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1328`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0615`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
