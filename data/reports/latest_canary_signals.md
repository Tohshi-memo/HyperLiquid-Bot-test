# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T09:07:36.922186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `13`; crypto_alt avg `-0.2034` n `235`; crypto_major avg `-0.1066` n `8`; equity avg `-0.0676` n `151`; fx avg `0.0038` n `6`; index avg `0.0017` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2204` n `1101`
- 1h: commodity avg `0.0037` n `13`; crypto_alt avg `-1.0074` n `235`; crypto_major avg `-0.7816` n `8`; equity avg `-0.2163` n `151`; fx avg `0.0008` n `6`; index avg `0.0003` n `26`; metal avg `-0.084` n `20`; unknown avg `1115.4331` n `1053`
- 4h: commodity avg `-0.0995` n `13`; crypto_alt avg `-0.7593` n `235`; crypto_major avg `-0.3368` n `8`; equity avg `-0.5265` n `151`; fx avg `-0.0168` n `6`; index avg `-0.0627` n `26`; metal avg `-0.1826` n `20`; unknown avg `1149.404` n `1021`
- 24h: commodity avg `1.023` n `13`; crypto_alt avg `-0.8691` n `235`; crypto_major avg `-0.2706` n `8`; equity avg `-0.5745` n `151`; fx avg `0.0365` n `6`; index avg `-0.0239` n `26`; metal avg `-0.5029` n `20`; unknown avg `1203.2554` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1327`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
