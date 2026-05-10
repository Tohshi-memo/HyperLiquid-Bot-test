# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T01:07:16.956564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.2436` n `228`; crypto_major avg `-0.1316` n `8`; equity avg `-0.078` n `65`; fx avg `0.0` n `5`; index avg `0.0213` n `23`; metal avg `-0.0018` n `18`; unknown avg `-0.0951` n `376`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `-0.2373` n `228`; crypto_major avg `-0.1932` n `8`; equity avg `-0.0706` n `65`; fx avg `-0.0295` n `5`; index avg `0.0318` n `23`; metal avg `0.0022` n `18`; unknown avg `-0.2088` n `376`
- 4h: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.9476` n `228`; crypto_major avg `-0.5725` n `8`; equity avg `0.0609` n `65`; fx avg `-0.0287` n `5`; index avg `0.1362` n `23`; metal avg `0.0767` n `18`; unknown avg `-0.3227` n `376`
- 24h: commodity avg `0.6278` n `12`; crypto_alt avg `-1.4963` n `228`; crypto_major avg `-0.4893` n `8`; equity avg `0.632` n `65`; fx avg `-0.0083` n `5`; index avg `0.3972` n `23`; metal avg `0.2428` n `18`; unknown avg `-0.2938` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
