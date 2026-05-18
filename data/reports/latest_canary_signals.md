# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T13:22:17.047413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1159` n `12`; crypto_alt avg `0.0211` n `228`; crypto_major avg `-0.0315` n `8`; equity avg `-0.0551` n `66`; fx avg `0.0045` n `5`; index avg `-0.0452` n `23`; metal avg `0.0791` n `18`; unknown avg `0.3299` n `383`
- 1h: commodity avg `-0.8542` n `12`; crypto_alt avg `-0.1231` n `228`; crypto_major avg `0.043` n `8`; equity avg `0.6148` n `66`; fx avg `-0.0363` n `5`; index avg `0.5018` n `23`; metal avg `0.449` n `18`; unknown avg `0.3513` n `383`
- 4h: commodity avg `-1.0133` n `12`; crypto_alt avg `0.7391` n `228`; crypto_major avg `0.7763` n `8`; equity avg `0.4848` n `66`; fx avg `-0.0002` n `5`; index avg `0.407` n `23`; metal avg `0.7067` n `18`; unknown avg `0.4443` n `383`
- 24h: commodity avg `-0.2978` n `12`; crypto_alt avg `-1.734` n `228`; crypto_major avg `-0.6039` n `8`; equity avg `0.8066` n `65`; fx avg `0.065` n `5`; index avg `0.5753` n `23`; metal avg `0.8442` n `18`; unknown avg `-0.0452` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
