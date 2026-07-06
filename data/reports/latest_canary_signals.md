# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T05:07:31.405423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0037` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `-0.3266` n `229`; crypto_major avg `-0.2994` n `8`; equity avg `0.0409` n `88`; fx avg `0.0086` n `6`; index avg `0.0037` n `25`; metal avg `-0.0243` n `20`; unknown avg `0.4201` n `765`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.3462` n `229`; crypto_major avg `-0.1187` n `8`; equity avg `0.3348` n `88`; fx avg `-0.0104` n `6`; index avg `0.1172` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.2198` n `765`
- 4h: commodity avg `0.0456` n `12`; crypto_alt avg `-0.9494` n `229`; crypto_major avg `-1.1141` n `8`; equity avg `-0.4993` n `88`; fx avg `0.04` n `6`; index avg `-0.1104` n `25`; metal avg `-0.3249` n `20`; unknown avg `0.3492` n `763`
- 24h: commodity avg `-0.1976` n `12`; crypto_alt avg `0.1848` n `229`; crypto_major avg `1.254` n `8`; equity avg `-0.5965` n `88`; fx avg `0.0672` n `6`; index avg `-0.0724` n `25`; metal avg `-0.2616` n `20`; unknown avg `1.1878` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
