# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T23:37:27.275777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0007` n `231`; crypto_major avg `-0.0147` n `8`; equity avg `0.0122` n `128`; fx avg `0.0` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.073` n `793`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.0639` n `231`; crypto_major avg `0.0925` n `8`; equity avg `0.0031` n `128`; fx avg `0.0094` n `6`; index avg `0.0128` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.0929` n `793`
- 4h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0522` n `231`; crypto_major avg `0.0022` n `8`; equity avg `0.085` n `128`; fx avg `0.009` n `6`; index avg `0.0273` n `26`; metal avg `0.0037` n `20`; unknown avg `0.1736` n `774`
- 24h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.3001` n `231`; crypto_major avg `0.8737` n `8`; equity avg `0.445` n `128`; fx avg `-0.0262` n `6`; index avg `0.1003` n `26`; metal avg `0.0994` n `20`; unknown avg `0.0867` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
