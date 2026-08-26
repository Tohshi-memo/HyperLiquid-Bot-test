# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T09:10:22.937693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `-0.0921` n `231`; crypto_major avg `0.0199` n `8`; equity avg `-0.0479` n `122`; fx avg `-0.0037` n `6`; index avg `-0.0084` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0005` n `797`
- 1h: commodity avg `-0.0565` n `12`; crypto_alt avg `0.0848` n `231`; crypto_major avg `-0.0024` n `8`; equity avg `0.0113` n `122`; fx avg `-0.0101` n `6`; index avg `0.0011` n `25`; metal avg `-0.0181` n `20`; unknown avg `0.0796` n `797`
- 4h: commodity avg `-0.1037` n `12`; crypto_alt avg `0.3846` n `231`; crypto_major avg `0.3683` n `8`; equity avg `-0.2794` n `122`; fx avg `-0.0116` n `6`; index avg `-0.0417` n `25`; metal avg `-0.119` n `20`; unknown avg `0.1416` n `781`
- 24h: commodity avg `-0.4368` n `12`; crypto_alt avg `-1.7071` n `231`; crypto_major avg `-1.7708` n `8`; equity avg `0.277` n `122`; fx avg `-0.0462` n `6`; index avg `-0.0152` n `25`; metal avg `0.2609` n `20`; unknown avg `0.9346` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
