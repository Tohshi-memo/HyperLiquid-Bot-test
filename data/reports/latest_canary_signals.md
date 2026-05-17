# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T23:07:16.001080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1857` n `228`; crypto_major avg `-0.1531` n `8`; equity avg `-0.3925` n `66`; fx avg `-0.0016` n `5`; index avg `-0.0895` n `23`; metal avg `-0.1873` n `18`; unknown avg `-0.0164` n `383`
- 1h: commodity avg `0.1253` n `12`; crypto_alt avg `-0.9038` n `228`; crypto_major avg `-0.9157` n `8`; equity avg `-0.1484` n `66`; fx avg `-0.002` n `5`; index avg `-0.1244` n `23`; metal avg `0.0206` n `18`; unknown avg `0.0077` n `383`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `-0.7131` n `228`; crypto_major avg `-0.5327` n `8`; equity avg `0.2163` n `66`; fx avg `-0.0199` n `5`; index avg `0.0429` n `23`; metal avg `0.4881` n `18`; unknown avg `-0.2127` n `383`
- 24h: commodity avg `1.8492` n `12`; crypto_alt avg `-9.9011` n `228`; crypto_major avg `-2.1795` n `8`; equity avg `-2.5612` n `65`; fx avg `-0.175` n `5`; index avg `-1.5455` n `23`; metal avg `-5.4456` n `18`; unknown avg `550.419` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
