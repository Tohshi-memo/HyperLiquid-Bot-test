# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T05:11:13.655961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `13`; crypto_alt avg `0.3169` n `236`; crypto_major avg `0.4006` n `8`; equity avg `0.0253` n `151`; fx avg `-0.0197` n `6`; index avg `0.0057` n `26`; metal avg `-0.0261` n `20`; unknown avg `3.8862` n `1134`
- 1h: commodity avg `0.0203` n `13`; crypto_alt avg `0.5808` n `236`; crypto_major avg `0.491` n `8`; equity avg `0.1203` n `151`; fx avg `-0.019` n `6`; index avg `0.004` n `26`; metal avg `-0.0697` n `20`; unknown avg `1.0176` n `1132`
- 4h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.0324` n `236`; crypto_major avg `0.1675` n `8`; equity avg `0.7992` n `151`; fx avg `-0.0087` n `6`; index avg `0.1089` n `26`; metal avg `0.2426` n `20`; unknown avg `0.0381` n `1124`
- 24h: commodity avg `0.0085` n `13`; crypto_alt avg `3.6069` n `236`; crypto_major avg `1.8286` n `8`; equity avg `2.2671` n `151`; fx avg `0.0174` n `6`; index avg `0.3412` n `26`; metal avg `0.4738` n `20`; unknown avg `25.5043` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0647`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
