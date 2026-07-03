# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T14:37:27.409586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.2032` n `229`; crypto_major avg `0.2779` n `8`; equity avg `-0.0145` n `88`; fx avg `0.0067` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0207` n `20`; unknown avg `0.6644` n `765`
- 1h: commodity avg `0.0278` n `12`; crypto_alt avg `-0.122` n `229`; crypto_major avg `-0.0706` n `8`; equity avg `-0.0726` n `88`; fx avg `-0.0068` n `6`; index avg `-0.026` n `25`; metal avg `0.0233` n `20`; unknown avg `-0.0078` n `765`
- 4h: commodity avg `0.1314` n `12`; crypto_alt avg `0.6382` n `229`; crypto_major avg `0.4099` n `8`; equity avg `-0.1699` n `88`; fx avg `-0.0069` n `6`; index avg `0.0009` n `25`; metal avg `-0.1146` n `20`; unknown avg `1.5998` n `765`
- 24h: commodity avg `0.5276` n `12`; crypto_alt avg `2.0145` n `229`; crypto_major avg `1.6325` n `8`; equity avg `-0.2484` n `88`; fx avg `-0.1085` n `6`; index avg `0.1587` n `25`; metal avg `0.475` n `20`; unknown avg `7.8341` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
