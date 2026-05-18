# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T18:07:19.305789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0788` n `12`; crypto_alt avg `-0.4157` n `228`; crypto_major avg `-0.2704` n `8`; equity avg `-0.2507` n `66`; fx avg `-0.0213` n `5`; index avg `-0.1538` n `23`; metal avg `-0.1315` n `18`; unknown avg `0.7759` n `384`
- 1h: commodity avg `0.2086` n `12`; crypto_alt avg `-0.4387` n `228`; crypto_major avg `-0.306` n `8`; equity avg `-0.3918` n `66`; fx avg `-0.0342` n `5`; index avg `-0.2826` n `23`; metal avg `-0.2857` n `18`; unknown avg `0.7683` n `384`
- 4h: commodity avg `1.1917` n `12`; crypto_alt avg `-0.7803` n `228`; crypto_major avg `-0.6684` n `8`; equity avg `-1.6098` n `66`; fx avg `-0.042` n `5`; index avg `-0.7342` n `23`; metal avg `-0.2065` n `18`; unknown avg `-1.008` n `384`
- 24h: commodity avg `1.2324` n `12`; crypto_alt avg `-2.5587` n `228`; crypto_major avg `-2.0489` n `8`; equity avg `-1.106` n `66`; fx avg `-0.0085` n `5`; index avg `-0.6418` n `23`; metal avg `0.5058` n `18`; unknown avg `0.353` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
