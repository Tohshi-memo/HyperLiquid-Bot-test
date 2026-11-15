# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T00:07:29.574962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8097` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.7199` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5005` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.3734` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `-0.0842` n `239`; crypto_major avg `-0.2186` n `8`; equity avg `0.0153` n `162`; fx avg `-0.0008` n `6`; index avg `-0.0019` n `27`; metal avg `0.0077` n `20`; unknown avg `0.2524` n `1250`
- 1h: commodity avg `0.0262` n `13`; crypto_alt avg `1.5187` n `239`; crypto_major avg `1.1925` n `8`; equity avg `0.3274` n `162`; fx avg `-0.0112` n `6`; index avg `0.0274` n `27`; metal avg `0.0349` n `20`; unknown avg `0.9915` n `1252`
- 4h: commodity avg `0.0905` n `13`; crypto_alt avg `-1.7251` n `239`; crypto_major avg `-2.7192` n `8`; equity avg `-0.3458` n `162`; fx avg `0.0243` n `6`; index avg `0.0007` n `27`; metal avg `-0.2187` n `20`; unknown avg `0.0752` n `1180`
- 24h: commodity avg `0.029` n `13`; crypto_alt avg `-8.4972` n `239`; crypto_major avg `-8.3755` n `8`; equity avg `-1.4357` n `162`; fx avg `0.0147` n `6`; index avg `-0.2161` n `27`; metal avg `-0.4394` n `20`; unknown avg `46.9839` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
