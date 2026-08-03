# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T11:07:28.554515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0451` n `230`; crypto_major avg `-0.0637` n `8`; equity avg `-0.1535` n `102`; fx avg `-0.017` n `6`; index avg `-0.0342` n `25`; metal avg `0.0136` n `20`; unknown avg `0.2078` n `785`
- 1h: commodity avg `-0.1105` n `12`; crypto_alt avg `-0.2314` n `230`; crypto_major avg `-0.2298` n `8`; equity avg `-0.5667` n `102`; fx avg `-0.0247` n `6`; index avg `-0.0623` n `25`; metal avg `-0.074` n `20`; unknown avg `0.1566` n `784`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `0.0628` n `230`; crypto_major avg `0.1204` n `8`; equity avg `-1.3495` n `102`; fx avg `-0.0318` n `6`; index avg `-0.1704` n `25`; metal avg `-0.1003` n `20`; unknown avg `0.1485` n `784`
- 24h: commodity avg `-0.369` n `12`; crypto_alt avg `-0.8373` n `230`; crypto_major avg `-0.3409` n `8`; equity avg `-0.8344` n `102`; fx avg `-0.1599` n `6`; index avg `-0.1836` n `25`; metal avg `-0.2204` n `20`; unknown avg `1.2318` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
