# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T11:52:29.664399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0458` n `13`; crypto_alt avg `-0.1482` n `236`; crypto_major avg `-0.2024` n `8`; equity avg `-0.1685` n `151`; fx avg `-0.0001` n `6`; index avg `-0.013` n `26`; metal avg `-0.0067` n `20`; unknown avg `2.9029` n `1136`
- 1h: commodity avg `0.0816` n `13`; crypto_alt avg `0.3137` n `236`; crypto_major avg `0.2622` n `8`; equity avg `-0.4195` n `151`; fx avg `0.0003` n `6`; index avg `-0.0374` n `26`; metal avg `0.004` n `20`; unknown avg `11.7468` n `1134`
- 4h: commodity avg `0.0891` n `13`; crypto_alt avg `0.3726` n `236`; crypto_major avg `0.4633` n `8`; equity avg `-0.5605` n `151`; fx avg `0.0363` n `6`; index avg `-0.0355` n `26`; metal avg `-0.044` n `20`; unknown avg `0.8996` n `1066`
- 24h: commodity avg `0.0676` n `13`; crypto_alt avg `4.5203` n `236`; crypto_major avg `2.6789` n `8`; equity avg `2.0089` n `151`; fx avg `0.0293` n `6`; index avg `0.2645` n `26`; metal avg `0.2996` n `20`; unknown avg `24.8457` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.073`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
