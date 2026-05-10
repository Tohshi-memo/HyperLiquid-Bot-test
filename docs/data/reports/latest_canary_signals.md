# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T02:22:17.880988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.1972` n `228`; crypto_major avg `0.0979` n `8`; equity avg `0.0214` n `65`; fx avg `0.0` n `5`; index avg `0.0143` n `23`; metal avg `0.001` n `18`; unknown avg `0.5806` n `376`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.4151` n `228`; crypto_major avg `0.2694` n `8`; equity avg `0.0169` n `65`; fx avg `0.0` n `5`; index avg `0.0469` n `23`; metal avg `0.023` n `18`; unknown avg `0.7883` n `376`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.829` n `228`; crypto_major avg `-0.4176` n `8`; equity avg `0.0235` n `65`; fx avg `0.0002` n `5`; index avg `0.1226` n `23`; metal avg `0.0468` n `18`; unknown avg `0.1656` n `376`
- 24h: commodity avg `0.4155` n `12`; crypto_alt avg `-1.8269` n `228`; crypto_major avg `-0.84` n `8`; equity avg `0.67` n `65`; fx avg `-0.0346` n `5`; index avg `0.3405` n `23`; metal avg `0.1795` n `18`; unknown avg `-0.5334` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
