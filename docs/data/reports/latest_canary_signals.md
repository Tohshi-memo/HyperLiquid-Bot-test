# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T12:37:21.105673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3354` n `12`; crypto_alt avg `0.1124` n `228`; crypto_major avg `0.0866` n `8`; equity avg `0.1861` n `66`; fx avg `-0.0159` n `5`; index avg `0.1704` n `23`; metal avg `0.169` n `18`; unknown avg `0.0394` n `383`
- 1h: commodity avg `-0.2844` n `12`; crypto_alt avg `1.1626` n `228`; crypto_major avg `1.0474` n `8`; equity avg `0.5681` n `66`; fx avg `-0.0347` n `5`; index avg `0.3714` n `23`; metal avg `0.3886` n `18`; unknown avg `0.5698` n `383`
- 4h: commodity avg `-0.3788` n `12`; crypto_alt avg `1.0334` n `228`; crypto_major avg `0.8821` n `8`; equity avg `0.1148` n `66`; fx avg `0.0446` n `5`; index avg `0.0725` n `23`; metal avg `0.3461` n `18`; unknown avg `0.2167` n `383`
- 24h: commodity avg `0.2663` n `12`; crypto_alt avg `-1.9886` n `228`; crypto_major avg `-1.0913` n `8`; equity avg `0.3736` n `65`; fx avg `0.0831` n `5`; index avg `0.3339` n `23`; metal avg `0.5867` n `18`; unknown avg `-0.3651` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
