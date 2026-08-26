# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T13:37:32.732604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0725` n `12`; crypto_alt avg `0.1317` n `231`; crypto_major avg `0.4465` n `8`; equity avg `0.6873` n `122`; fx avg `0.0032` n `6`; index avg `0.0786` n `25`; metal avg `0.0125` n `20`; unknown avg `0.1351` n `797`
- 1h: commodity avg `0.1595` n `12`; crypto_alt avg `-0.4507` n `231`; crypto_major avg `-0.0756` n `8`; equity avg `0.5196` n `122`; fx avg `0.0142` n `6`; index avg `0.0627` n `25`; metal avg `-0.0826` n `20`; unknown avg `0.1877` n `797`
- 4h: commodity avg `0.2229` n `12`; crypto_alt avg `-0.0026` n `231`; crypto_major avg `0.0938` n `8`; equity avg `0.221` n `122`; fx avg `-0.0008` n `6`; index avg `0.0388` n `25`; metal avg `-0.0926` n `20`; unknown avg `0.016` n `797`
- 24h: commodity avg `0.052` n `12`; crypto_alt avg `-1.4086` n `231`; crypto_major avg `-1.1173` n `8`; equity avg `0.2094` n `122`; fx avg `-0.0583` n `6`; index avg `-0.0023` n `25`; metal avg `0.1768` n `20`; unknown avg `0.6596` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
