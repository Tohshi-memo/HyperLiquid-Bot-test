# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T12:07:34.645115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `0.3691` n `235`; crypto_major avg `0.2629` n `8`; equity avg `0.1704` n `151`; fx avg `0.0066` n `6`; index avg `0.0295` n `26`; metal avg `0.0635` n `20`; unknown avg `0.126` n `1128`
- 1h: commodity avg `-0.0759` n `13`; crypto_alt avg `0.684` n `235`; crypto_major avg `0.3968` n `8`; equity avg `0.168` n `151`; fx avg `0.0103` n `6`; index avg `0.0357` n `26`; metal avg `0.0909` n `20`; unknown avg `0.2796` n `1128`
- 4h: commodity avg `0.0686` n `13`; crypto_alt avg `-0.8482` n `235`; crypto_major avg `-0.4103` n `8`; equity avg `-0.3062` n `151`; fx avg `0.0237` n `6`; index avg `-0.001` n `26`; metal avg `-0.0227` n `20`; unknown avg `1181.8875` n `1047`
- 24h: commodity avg `0.9699` n `13`; crypto_alt avg `0.8985` n `235`; crypto_major avg `0.783` n `8`; equity avg `0.0486` n `151`; fx avg `0.0179` n `6`; index avg `0.0455` n `26`; metal avg `-0.376` n `20`; unknown avg `1269.1119` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1501`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1281`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0783`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.076`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
