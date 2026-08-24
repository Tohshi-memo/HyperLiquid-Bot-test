# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T10:22:28.427851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.0284` n `231`; crypto_major avg `0.1113` n `8`; equity avg `-0.1254` n `122`; fx avg `-0.0036` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.1052` n `793`
- 1h: commodity avg `-0.0563` n `12`; crypto_alt avg `0.2574` n `231`; crypto_major avg `0.4299` n `8`; equity avg `0.0756` n `122`; fx avg `0.0026` n `6`; index avg `0.009` n `25`; metal avg `0.063` n `20`; unknown avg `0.0117` n `793`
- 4h: commodity avg `0.1122` n `12`; crypto_alt avg `0.1658` n `231`; crypto_major avg `0.1605` n `8`; equity avg `0.1712` n `122`; fx avg `0.0159` n `6`; index avg `0.0368` n `25`; metal avg `-0.0481` n `20`; unknown avg `0.3117` n `793`
- 24h: commodity avg `-0.2184` n `12`; crypto_alt avg `1.787` n `231`; crypto_major avg `0.4339` n `8`; equity avg `-1.2701` n `122`; fx avg `-0.1434` n `6`; index avg `-0.1272` n `25`; metal avg `0.1747` n `20`; unknown avg `5.4303` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
