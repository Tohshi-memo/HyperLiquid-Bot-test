# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T09:22:27.882992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.0846` n `237`; crypto_major avg `-0.1348` n `8`; equity avg `-0.002` n `151`; fx avg `0.0088` n `6`; index avg `0.0131` n `26`; metal avg `-0.0067` n `20`; unknown avg `-0.0384` n `1161`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `0.2001` n `237`; crypto_major avg `0.167` n `8`; equity avg `0.1435` n `151`; fx avg `-0.0006` n `6`; index avg `0.0278` n `26`; metal avg `0.0017` n `20`; unknown avg `1.5135` n `1095`
- 4h: commodity avg `0.0026` n `13`; crypto_alt avg `-0.0222` n `237`; crypto_major avg `0.0016` n `8`; equity avg `0.3007` n `151`; fx avg `-0.0019` n `6`; index avg `0.0551` n `26`; metal avg `-0.0102` n `20`; unknown avg `1.2738` n `1063`
- 24h: commodity avg `0.0255` n `13`; crypto_alt avg `-2.3476` n `236`; crypto_major avg `-0.7041` n `8`; equity avg `-0.5896` n `151`; fx avg `-0.0274` n `6`; index avg `-0.0593` n `26`; metal avg `-0.0638` n `20`; unknown avg `4.8417` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1862`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
