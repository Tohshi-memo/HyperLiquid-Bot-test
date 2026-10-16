# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T19:37:30.173426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `-0.1971` n `236`; crypto_major avg `-0.2175` n `8`; equity avg `-0.3175` n `151`; fx avg `-0.0041` n `6`; index avg `-0.0403` n `26`; metal avg `0.0356` n `20`; unknown avg `58.0814` n `1177`
- 1h: commodity avg `-0.0633` n `13`; crypto_alt avg `-0.1433` n `236`; crypto_major avg `-0.3241` n `8`; equity avg `-0.4317` n `151`; fx avg `0.0021` n `6`; index avg `-0.0492` n `26`; metal avg `0.0669` n `20`; unknown avg `120.9974` n `1175`
- 4h: commodity avg `0.6759` n `13`; crypto_alt avg `-1.524` n `236`; crypto_major avg `-0.9323` n `8`; equity avg `-1.6598` n `151`; fx avg `-0.0212` n `6`; index avg `-0.3429` n `26`; metal avg `-0.1307` n `20`; unknown avg `5.862` n `1140`
- 24h: commodity avg `0.3407` n `13`; crypto_alt avg `-2.3268` n `236`; crypto_major avg `-2.0325` n `8`; equity avg `-3.9994` n `151`; fx avg `0.0081` n `6`; index avg `-0.6701` n `26`; metal avg `-0.021` n `20`; unknown avg `5.8175` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.072`, n `666`, weak_sample_signal
