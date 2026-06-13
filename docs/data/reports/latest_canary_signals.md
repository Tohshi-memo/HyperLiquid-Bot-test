# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T17:52:29.098600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0466` n `12`; crypto_alt avg `-0.15` n `228`; crypto_major avg `-0.1869` n `8`; equity avg `-0.0048` n `74`; fx avg `-0.0125` n `6`; index avg `-0.0591` n `23`; metal avg `0.1279` n `18`; unknown avg `0.0426` n `644`
- 1h: commodity avg `-0.2545` n `12`; crypto_alt avg `0.2605` n `228`; crypto_major avg `-0.0824` n `8`; equity avg `0.0377` n `74`; fx avg `0.0181` n `6`; index avg `-0.0874` n `23`; metal avg `0.1377` n `18`; unknown avg `0.0426` n `644`
- 4h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.333` n `228`; crypto_major avg `-0.1679` n `8`; equity avg `0.0071` n `74`; fx avg `0.0018` n `6`; index avg `-0.0937` n `23`; metal avg `0.2721` n `18`; unknown avg `-1.9766` n `644`
- 24h: commodity avg `-0.8546` n `12`; crypto_alt avg `1.7558` n `228`; crypto_major avg `-0.3303` n `8`; equity avg `-0.2443` n `74`; fx avg `0.0246` n `6`; index avg `0.3396` n `23`; metal avg `0.3817` n `18`; unknown avg `-1.9202` n `611`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
