# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T20:37:35.260799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `-0.0111` n `228`; crypto_major avg `-0.0003` n `8`; equity avg `0.0009` n `74`; fx avg `-0.0053` n `6`; index avg `0.0052` n `23`; metal avg `-0.0987` n `18`; unknown avg `0.1536` n `644`
- 1h: commodity avg `0.107` n `12`; crypto_alt avg `-0.1528` n `228`; crypto_major avg `0.0237` n `8`; equity avg `0.019` n `74`; fx avg `-0.0164` n `6`; index avg `0.1077` n `23`; metal avg `-0.0971` n `18`; unknown avg `0.1383` n `644`
- 4h: commodity avg `-0.1412` n `12`; crypto_alt avg `0.0434` n `228`; crypto_major avg `0.1677` n `8`; equity avg `0.1655` n `74`; fx avg `0.0155` n `6`; index avg `-0.0136` n `23`; metal avg `-0.1829` n `18`; unknown avg `-0.2521` n `644`
- 24h: commodity avg `-0.7115` n `12`; crypto_alt avg `1.7393` n `228`; crypto_major avg `0.4458` n `8`; equity avg `0.4544` n `74`; fx avg `0.053` n `6`; index avg `0.5631` n `23`; metal avg `0.1685` n `18`; unknown avg `-1.5865` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
