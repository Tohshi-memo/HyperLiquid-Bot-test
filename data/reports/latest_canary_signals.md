# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T14:00:17.893145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.0519` n `237`; crypto_major avg `0.0059` n `8`; equity avg `-0.0108` n `151`; fx avg `0.005` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0161` n `1191`
- 1h: commodity avg `0.0209` n `13`; crypto_alt avg `-0.8472` n `237`; crypto_major avg `-0.7033` n `8`; equity avg `-0.2798` n `151`; fx avg `0.0026` n `6`; index avg `-0.0612` n `26`; metal avg `-0.0318` n `20`; unknown avg `-0.5331` n `1189`
- 4h: commodity avg `-0.0428` n `13`; crypto_alt avg `-0.791` n `237`; crypto_major avg `-0.8941` n `8`; equity avg `-0.3731` n `151`; fx avg `0.011` n `6`; index avg `-0.0909` n `26`; metal avg `-0.0291` n `20`; unknown avg `3.9318` n `1183`
- 24h: commodity avg `-0.1182` n `13`; crypto_alt avg `-2.4319` n `236`; crypto_major avg `-0.7158` n `8`; equity avg `-0.8421` n `151`; fx avg `-0.0349` n `6`; index avg `-0.1138` n `26`; metal avg `-0.0637` n `20`; unknown avg `1.3683` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2069`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
