# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T10:07:27.795422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `13`; crypto_alt avg `-0.2858` n `236`; crypto_major avg `-0.2978` n `8`; equity avg `-0.2114` n `151`; fx avg `-0.0084` n `6`; index avg `-0.0216` n `26`; metal avg `-0.013` n `20`; unknown avg `0.7953` n `1134`
- 1h: commodity avg `0.0756` n `13`; crypto_alt avg `-0.3899` n `236`; crypto_major avg `-0.4614` n `8`; equity avg `-0.2246` n `151`; fx avg `-0.0214` n `6`; index avg `-0.0434` n `26`; metal avg `-0.0949` n `20`; unknown avg `0.9511` n `1134`
- 4h: commodity avg `0.1167` n `13`; crypto_alt avg `0.033` n `236`; crypto_major avg `0.0026` n `8`; equity avg `-0.397` n `151`; fx avg `0.0044` n `6`; index avg `-0.0614` n `26`; metal avg `0.0133` n `20`; unknown avg `0.3442` n `1066`
- 24h: commodity avg `0.0387` n `13`; crypto_alt avg `3.8227` n `236`; crypto_major avg `1.7594` n `8`; equity avg `2.3934` n `151`; fx avg `0.0034` n `6`; index avg `0.3016` n `26`; metal avg `0.2073` n `20`; unknown avg `26.2631` n `896`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0977`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
