# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T14:07:36.470434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1105` n `12`; crypto_alt avg `0.0801` n `228`; crypto_major avg `0.0453` n `8`; equity avg `-0.0143` n `74`; fx avg `-0.0006` n `6`; index avg `-0.0008` n `23`; metal avg `0.1064` n `18`; unknown avg `0.0116` n `644`
- 1h: commodity avg `0.091` n `12`; crypto_alt avg `-0.0073` n `228`; crypto_major avg `-0.08` n `8`; equity avg `-0.0295` n `74`; fx avg `-0.0042` n `6`; index avg `-0.0089` n `23`; metal avg `0.0156` n `18`; unknown avg `-0.1164` n `644`
- 4h: commodity avg `-0.0977` n `12`; crypto_alt avg `0.3483` n `228`; crypto_major avg `0.7224` n `8`; equity avg `0.146` n `74`; fx avg `-0.0068` n `6`; index avg `0.2021` n `23`; metal avg `0.1364` n `18`; unknown avg `24.0412` n `644`
- 24h: commodity avg `-1.339` n `12`; crypto_alt avg `1.5836` n `228`; crypto_major avg `0.5138` n `8`; equity avg `0.0229` n `74`; fx avg `0.0266` n `6`; index avg `0.7682` n `23`; metal avg `0.9655` n `18`; unknown avg `3.8253` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
