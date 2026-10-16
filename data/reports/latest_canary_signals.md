# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T13:07:29.806283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `13`; crypto_alt avg `-0.2039` n `236`; crypto_major avg `-0.1012` n `8`; equity avg `-0.0533` n `151`; fx avg `0.0007` n `6`; index avg `0.0014` n `26`; metal avg `-0.0449` n `20`; unknown avg `0.4161` n `1134`
- 1h: commodity avg `-0.2174` n `13`; crypto_alt avg `-0.5488` n `236`; crypto_major avg `-0.4912` n `8`; equity avg `-0.3278` n `151`; fx avg `-0.0206` n `6`; index avg `-0.0284` n `26`; metal avg `-0.0849` n `20`; unknown avg `2.8325` n `1134`
- 4h: commodity avg `-0.0552` n `13`; crypto_alt avg `-0.4443` n `236`; crypto_major avg `-0.502` n `8`; equity avg `-0.7069` n `151`; fx avg `-0.0068` n `6`; index avg `-0.0399` n `26`; metal avg `-0.1533` n `20`; unknown avg `8.9679` n `1128`
- 24h: commodity avg `-0.0598` n `13`; crypto_alt avg `4.5169` n `236`; crypto_major avg `2.5458` n `8`; equity avg `2.3477` n `151`; fx avg `0.0199` n `6`; index avg `0.3163` n `26`; metal avg `0.2113` n `20`; unknown avg `25.0721` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.09`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `666`, weak_sample_signal
