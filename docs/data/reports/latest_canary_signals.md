# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T05:37:29.878410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2989` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0393` n `12`; crypto_alt avg `-0.1528` n `229`; crypto_major avg `-0.1508` n `8`; equity avg `-0.0468` n `88`; fx avg `-0.0113` n `6`; index avg `-0.0348` n `25`; metal avg `0.0845` n `20`; unknown avg `0.1729` n `765`
- 1h: commodity avg `0.0756` n `12`; crypto_alt avg `-0.5262` n `229`; crypto_major avg `-0.3967` n `8`; equity avg `-0.0869` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0365` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.0219` n `765`
- 4h: commodity avg `0.1484` n `12`; crypto_alt avg `-1.4181` n `229`; crypto_major avg `-1.4426` n `8`; equity avg `-0.2971` n `88`; fx avg `-0.0011` n `6`; index avg `-0.1437` n `25`; metal avg `-0.4063` n `20`; unknown avg `0.4243` n `763`
- 24h: commodity avg `-0.1351` n `12`; crypto_alt avg `-0.098` n `229`; crypto_major avg `1.0151` n `8`; equity avg `-0.7614` n `88`; fx avg `0.0541` n `6`; index avg `-0.1117` n `25`; metal avg `-0.2181` n `20`; unknown avg `0.8862` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
