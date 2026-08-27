# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T00:37:27.684140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.526` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.2448` n `231`; crypto_major avg `-0.3396` n `8`; equity avg `-0.32` n `124`; fx avg `-0.0259` n `6`; index avg `-0.0642` n `25`; metal avg `-0.0293` n `20`; unknown avg `-0.1251` n `795`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.1435` n `231`; crypto_major avg `-0.3512` n `8`; equity avg `-0.531` n `124`; fx avg `-0.0723` n `6`; index avg `-0.114` n `25`; metal avg `-0.0467` n `20`; unknown avg `-0.0905` n `795`
- 4h: commodity avg `0.0155` n `12`; crypto_alt avg `2.2286` n `231`; crypto_major avg `1.7071` n `8`; equity avg `0.858` n `124`; fx avg `-0.0704` n `6`; index avg `0.1646` n `25`; metal avg `0.1811` n `20`; unknown avg `0.5935` n `795`
- 24h: commodity avg `0.2985` n `12`; crypto_alt avg `1.7018` n `231`; crypto_major avg `1.3311` n `8`; equity avg `1.4722` n `124`; fx avg `-0.1497` n `6`; index avg `0.3004` n `25`; metal avg `-0.1802` n `20`; unknown avg `1.002` n `778`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
