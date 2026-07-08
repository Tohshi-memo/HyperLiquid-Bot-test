# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T07:11:51.033617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.1161` n `229`; crypto_major avg `-0.0784` n `8`; equity avg `-0.1176` n `91`; fx avg `0.0337` n `6`; index avg `-0.0214` n `25`; metal avg `-0.1102` n `20`; unknown avg `0.0133` n `763`
- 1h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.2031` n `229`; crypto_major avg `-0.1515` n `8`; equity avg `-0.2485` n `91`; fx avg `-0.0347` n `6`; index avg `-0.0555` n `25`; metal avg `-0.0611` n `20`; unknown avg `-0.1499` n `763`
- 4h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.4515` n `229`; crypto_major avg `-0.6798` n `8`; equity avg `-0.6947` n `91`; fx avg `-0.0467` n `6`; index avg `-0.2788` n `25`; metal avg `-0.0407` n `20`; unknown avg `-0.2492` n `743`
- 24h: commodity avg `0.7759` n `12`; crypto_alt avg `-3.0775` n `229`; crypto_major avg `-2.7067` n `8`; equity avg `-2.0556` n `91`; fx avg `-0.2805` n `6`; index avg `-0.4032` n `25`; metal avg `-0.0431` n `20`; unknown avg `-0.6608` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
