# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T19:52:25.638392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0837` n `12`; crypto_alt avg `0.1914` n `228`; crypto_major avg `0.1292` n `8`; equity avg `0.0146` n `74`; fx avg `-0.0073` n `6`; index avg `0.0` n `23`; metal avg `-0.2058` n `18`; unknown avg `-0.1279` n `644`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `0.4046` n `228`; crypto_major avg `0.2484` n `8`; equity avg `0.1094` n `74`; fx avg `-0.0177` n `6`; index avg `-0.0117` n `23`; metal avg `-0.1764` n `18`; unknown avg `-0.4413` n `644`
- 4h: commodity avg `-0.0649` n `12`; crypto_alt avg `-0.1694` n `228`; crypto_major avg `-0.2847` n `8`; equity avg `0.0339` n `74`; fx avg `0.0233` n `6`; index avg `-0.0918` n `23`; metal avg `-0.2409` n `18`; unknown avg `-0.4205` n `644`
- 24h: commodity avg `-0.7351` n `12`; crypto_alt avg `2.3111` n `228`; crypto_major avg `0.7348` n `8`; equity avg `0.5452` n `74`; fx avg `0.0541` n `6`; index avg `0.6194` n `23`; metal avg `0.2655` n `18`; unknown avg `-1.6645` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
