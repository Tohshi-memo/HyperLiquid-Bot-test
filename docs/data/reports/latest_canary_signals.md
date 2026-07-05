# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T19:52:25.526949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `-0.0712` n `229`; crypto_major avg `-0.0416` n `8`; equity avg `0.0253` n `88`; fx avg `-0.0094` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.0981` n `765`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0693` n `229`; crypto_major avg `-0.1493` n `8`; equity avg `0.0177` n `88`; fx avg `0.0031` n `6`; index avg `-0.0033` n `25`; metal avg `-0.009` n `20`; unknown avg `0.7822` n `765`
- 4h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.3024` n `229`; crypto_major avg `0.0931` n `8`; equity avg `0.139` n `88`; fx avg `0.0043` n `6`; index avg `0.0171` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.8225` n `713`
- 24h: commodity avg `-0.0052` n `12`; crypto_alt avg `-1.1795` n `229`; crypto_major avg `-0.5863` n `8`; equity avg `0.3471` n `88`; fx avg `-0.0294` n `6`; index avg `0.0881` n `25`; metal avg `0.0355` n `20`; unknown avg `0.9996` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
