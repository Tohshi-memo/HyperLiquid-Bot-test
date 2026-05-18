# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T09:37:15.819804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0936` n `12`; crypto_alt avg `0.0053` n `228`; crypto_major avg `-0.0924` n `8`; equity avg `-0.074` n `66`; fx avg `0.0133` n `5`; index avg `0.0027` n `23`; metal avg `-0.0994` n `18`; unknown avg `-0.0667` n `383`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `0.0591` n `228`; crypto_major avg `-0.0315` n `8`; equity avg `-0.0197` n `66`; fx avg `0.0378` n `5`; index avg `-0.0037` n `23`; metal avg `-0.1783` n `18`; unknown avg `-0.105` n `383`
- 4h: commodity avg `-0.1323` n `12`; crypto_alt avg `-0.6246` n `228`; crypto_major avg `-0.6456` n `8`; equity avg `0.6336` n `66`; fx avg `-0.0192` n `5`; index avg `0.22` n `23`; metal avg `0.2459` n `18`; unknown avg `-0.248` n `363`
- 24h: commodity avg `0.6535` n `12`; crypto_alt avg `-2.8601` n `228`; crypto_major avg `-1.3998` n `8`; equity avg `0.4619` n `65`; fx avg `0.0605` n `5`; index avg `0.2971` n `23`; metal avg `0.062` n `18`; unknown avg `-0.6789` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
