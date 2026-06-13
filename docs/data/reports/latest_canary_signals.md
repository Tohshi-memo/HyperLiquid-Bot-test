# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T17:22:27.747063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0736` n `12`; crypto_alt avg `0.2627` n `228`; crypto_major avg `0.064` n `8`; equity avg `0.0015` n `74`; fx avg `0.0148` n `6`; index avg `-0.0213` n `23`; metal avg `0.2198` n `18`; unknown avg `0.1472` n `644`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `0.1798` n `228`; crypto_major avg `-0.1185` n `8`; equity avg `-0.1512` n `74`; fx avg `0.0093` n `6`; index avg `-0.0274` n `23`; metal avg `0.1076` n `18`; unknown avg `0.0917` n `644`
- 4h: commodity avg `0.0289` n `12`; crypto_alt avg `0.1701` n `228`; crypto_major avg `-0.205` n `8`; equity avg `0.0225` n `74`; fx avg `-0.0098` n `6`; index avg `0.0356` n `23`; metal avg `0.0114` n `18`; unknown avg `-2.1039` n `644`
- 24h: commodity avg `-0.7209` n `12`; crypto_alt avg `1.834` n `228`; crypto_major avg `-0.0713` n `8`; equity avg `-0.3169` n `74`; fx avg `0.0328` n `6`; index avg `0.4271` n `23`; metal avg `0.4695` n `18`; unknown avg `-1.9253` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
