# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T20:07:36.912608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.2988` n `228`; crypto_major avg `-0.1746` n `8`; equity avg `-0.003` n `74`; fx avg `0.004` n `6`; index avg `0.0907` n `23`; metal avg `0.213` n `18`; unknown avg `0.2385` n `644`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1024` n `228`; crypto_major avg `0.0077` n `8`; equity avg `0.1018` n `74`; fx avg `-0.0035` n `6`; index avg `0.0701` n `23`; metal avg `0.0111` n `18`; unknown avg `-0.3778` n `644`
- 4h: commodity avg `-0.1583` n `12`; crypto_alt avg `-0.1558` n `228`; crypto_major avg `-0.1455` n `8`; equity avg `0.1381` n `74`; fx avg `0.0286` n `6`; index avg `-0.0164` n `23`; metal avg `0.1122` n `18`; unknown avg `-0.3515` n `644`
- 24h: commodity avg `-0.7843` n `12`; crypto_alt avg `1.9599` n `228`; crypto_major avg `0.5201` n `8`; equity avg `0.5525` n `74`; fx avg `0.0557` n `6`; index avg `0.5934` n `23`; metal avg `0.3494` n `18`; unknown avg `-1.6416` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
