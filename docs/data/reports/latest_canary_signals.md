# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T08:37:25.531298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `-0.0594` n `230`; crypto_major avg `0.0072` n `8`; equity avg `-0.0286` n `92`; fx avg `-0.0044` n `6`; index avg `0.0097` n `25`; metal avg `-0.0373` n `20`; unknown avg `0.0206` n `766`
- 1h: commodity avg `-0.1183` n `12`; crypto_alt avg `-0.1833` n `230`; crypto_major avg `-0.1517` n `8`; equity avg `0.2427` n `92`; fx avg `-0.0144` n `6`; index avg `0.071` n `25`; metal avg `0.1473` n `20`; unknown avg `0.0156` n `766`
- 4h: commodity avg `-0.2002` n `12`; crypto_alt avg `0.6596` n `230`; crypto_major avg `0.2825` n `8`; equity avg `0.2873` n `92`; fx avg `-0.0373` n `6`; index avg `0.1207` n `25`; metal avg `0.3226` n `20`; unknown avg `0.0388` n `750`
- 24h: commodity avg `-0.1427` n `12`; crypto_alt avg `-1.2792` n `230`; crypto_major avg `-1.0255` n `8`; equity avg `-2.0955` n `92`; fx avg `0.0011` n `6`; index avg `-0.4266` n `25`; metal avg `-0.1603` n `20`; unknown avg `-0.016` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
