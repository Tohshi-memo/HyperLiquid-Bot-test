# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T09:07:30.095077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `12`; crypto_alt avg `-0.0177` n `231`; crypto_major avg `0.061` n `8`; equity avg `-0.0269` n `122`; fx avg `-0.0011` n `6`; index avg `-0.0064` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0015` n `797`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.1592` n `231`; crypto_major avg `0.0386` n `8`; equity avg `0.0322` n `122`; fx avg `-0.0075` n `6`; index avg `0.0031` n `25`; metal avg `-0.02` n `20`; unknown avg `0.0807` n `797`
- 4h: commodity avg `-0.0763` n `12`; crypto_alt avg `0.4601` n `231`; crypto_major avg `0.4096` n `8`; equity avg `-0.2586` n `122`; fx avg `-0.009` n `6`; index avg `-0.0397` n `25`; metal avg `-0.121` n `20`; unknown avg `0.1414` n `781`
- 24h: commodity avg `-0.4102` n `12`; crypto_alt avg `-1.6352` n `231`; crypto_major avg `-1.7309` n `8`; equity avg `0.298` n `122`; fx avg `-0.0436` n `6`; index avg `-0.0132` n `25`; metal avg `0.2589` n `20`; unknown avg `0.9351` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
