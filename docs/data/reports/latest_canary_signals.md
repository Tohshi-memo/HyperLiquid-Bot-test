# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T14:37:30.815349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.0505` n `236`; crypto_major avg `0.0993` n `8`; equity avg `-0.0178` n `151`; fx avg `0.003` n `6`; index avg `0.0106` n `26`; metal avg `0.0066` n `20`; unknown avg `0.3648` n `1191`
- 1h: commodity avg `0.0419` n `13`; crypto_alt avg `0.4109` n `236`; crypto_major avg `0.3291` n `8`; equity avg `0.0461` n `151`; fx avg `-0.0071` n `6`; index avg `0.0019` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.8976` n `1189`
- 4h: commodity avg `0.0328` n `13`; crypto_alt avg `-0.8434` n `236`; crypto_major avg `-0.3414` n `8`; equity avg `-0.1321` n `151`; fx avg `-0.0115` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0107` n `20`; unknown avg `3.1454` n `1183`
- 24h: commodity avg `0.7724` n `13`; crypto_alt avg `-2.8632` n `236`; crypto_major avg `-1.7072` n `8`; equity avg `-2.4527` n `151`; fx avg `-0.0353` n `6`; index avg `-0.4429` n `26`; metal avg `-0.2575` n `20`; unknown avg `3.0767` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1735`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1436`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0702`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
