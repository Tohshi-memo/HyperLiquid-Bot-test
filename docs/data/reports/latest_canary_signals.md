# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T11:19:30.834898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.2925` n `231`; crypto_major avg `0.2256` n `8`; equity avg `0.0982` n `122`; fx avg `-0.0002` n `6`; index avg `0.0092` n `25`; metal avg `0.0151` n `20`; unknown avg `0.0603` n `793`
- 1h: commodity avg `0.1052` n `12`; crypto_alt avg `-0.2005` n `231`; crypto_major avg `-0.0861` n `8`; equity avg `-0.2868` n `122`; fx avg `0.0204` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0189` n `20`; unknown avg `1.088` n `793`
- 4h: commodity avg `0.1801` n `12`; crypto_alt avg `-0.0334` n `231`; crypto_major avg `-0.2678` n `8`; equity avg `-0.2296` n `122`; fx avg `-0.0078` n `6`; index avg `-0.0277` n `25`; metal avg `-0.084` n `20`; unknown avg `0.4298` n `793`
- 24h: commodity avg `-0.1109` n `12`; crypto_alt avg `0.8401` n `231`; crypto_major avg `-0.0251` n `8`; equity avg `-1.6426` n `122`; fx avg `-0.1177` n `6`; index avg `-0.169` n `25`; metal avg `0.1332` n `20`; unknown avg `5.0702` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
