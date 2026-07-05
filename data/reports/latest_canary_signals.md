# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T05:33:05.645121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.1245` n `229`; crypto_major avg `0.0123` n `8`; equity avg `0.0165` n `88`; fx avg `-0.0036` n `6`; index avg `0.0043` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0483` n `765`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.3211` n `229`; crypto_major avg `-0.3177` n `8`; equity avg `-0.0002` n `88`; fx avg `-0.0046` n `6`; index avg `0.046` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.8145` n `765`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `-0.4204` n `229`; crypto_major avg `-0.3511` n `8`; equity avg `0.1531` n `88`; fx avg `-0.0064` n `6`; index avg `0.0747` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.3671` n `765`
- 24h: commodity avg `0.0751` n `12`; crypto_alt avg `-0.9388` n `229`; crypto_major avg `-1.1046` n `8`; equity avg `0.1684` n `88`; fx avg `-0.0145` n `6`; index avg `0.0698` n `25`; metal avg `0.0813` n `20`; unknown avg `-0.8648` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
