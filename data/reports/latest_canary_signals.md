# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T12:52:19.508870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4939` n `12`; crypto_alt avg `-0.0189` n `228`; crypto_major avg `0.0169` n `8`; equity avg `0.4031` n `66`; fx avg `-0.0159` n `5`; index avg `0.3244` n `23`; metal avg `0.1636` n `18`; unknown avg `-0.0845` n `383`
- 1h: commodity avg `-0.5041` n `12`; crypto_alt avg `0.6285` n `228`; crypto_major avg `0.5186` n `8`; equity avg `0.6817` n `66`; fx avg `-0.0144` n `5`; index avg `0.5125` n `23`; metal avg `0.2991` n `18`; unknown avg `0.1327` n `383`
- 4h: commodity avg `-0.8136` n `12`; crypto_alt avg `0.8849` n `228`; crypto_major avg `0.8197` n `8`; equity avg `0.4391` n `66`; fx avg `0.0166` n `5`; index avg `0.3461` n `23`; metal avg `0.4342` n `18`; unknown avg `-0.1092` n `383`
- 24h: commodity avg `-0.2468` n `12`; crypto_alt avg `-1.8669` n `228`; crypto_major avg `-1.0168` n `8`; equity avg `0.7877` n `65`; fx avg `0.0687` n `5`; index avg `0.5822` n `23`; metal avg `0.738` n `18`; unknown avg `-0.4408` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
