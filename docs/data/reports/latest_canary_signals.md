# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T18:37:29.128993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0545` n `228`; crypto_major avg `0.157` n `8`; equity avg `0.0763` n `74`; fx avg `-0.001` n `6`; index avg `0.0222` n `23`; metal avg `0.2393` n `18`; unknown avg `-0.0484` n `644`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `-0.214` n `228`; crypto_major avg `0.1013` n `8`; equity avg `0.1996` n `74`; fx avg `0.0174` n `6`; index avg `0.0026` n `23`; metal avg `0.0595` n `18`; unknown avg `-0.0177` n `644`
- 4h: commodity avg `-0.2479` n `12`; crypto_alt avg `0.2976` n `228`; crypto_major avg `-0.1618` n `8`; equity avg `0.1595` n `74`; fx avg `0.0403` n `6`; index avg `-0.0392` n `23`; metal avg `0.1435` n `18`; unknown avg `-2.059` n `644`
- 24h: commodity avg `-0.8523` n `12`; crypto_alt avg `1.926` n `228`; crypto_major avg `0.0766` n `8`; equity avg `0.2141` n `74`; fx avg `0.0451` n `6`; index avg `0.4587` n `23`; metal avg `0.1572` n `18`; unknown avg `-1.7512` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
