# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T16:36:23.409053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.0263` n `228`; crypto_major avg `0.0351` n `8`; equity avg `0.011` n `65`; fx avg `0.0` n `5`; index avg `0.0372` n `23`; metal avg `0.0003` n `18`; unknown avg `0.7631` n `384`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `0.1408` n `228`; crypto_major avg `0.1369` n `8`; equity avg `0.0719` n `65`; fx avg `0.0` n `5`; index avg `0.0599` n `23`; metal avg `-0.0058` n `18`; unknown avg `0.7761` n `384`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.2824` n `228`; crypto_major avg `-0.3632` n `8`; equity avg `-0.0117` n `65`; fx avg `0.0183` n `5`; index avg `0.1876` n `23`; metal avg `0.0162` n `18`; unknown avg `0.6984` n `383`
- 24h: commodity avg `1.7867` n `12`; crypto_alt avg `-9.1529` n `228`; crypto_major avg `-2.3615` n `8`; equity avg `-2.5325` n `65`; fx avg `-0.1657` n `5`; index avg `-1.5381` n `23`; metal avg `-5.836` n `18`; unknown avg `550.7834` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
