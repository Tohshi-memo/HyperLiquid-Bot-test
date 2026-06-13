# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T14:52:35.246724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1487` n `12`; crypto_alt avg `0.1487` n `228`; crypto_major avg `0.06` n `8`; equity avg `0.0578` n `74`; fx avg `-0.001` n `6`; index avg `0.0216` n `23`; metal avg `0.0694` n `18`; unknown avg `0.0295` n `644`
- 1h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.1181` n `228`; crypto_major avg `0.3439` n `8`; equity avg `0.1099` n `74`; fx avg `-0.0097` n `6`; index avg `0.0289` n `23`; metal avg `0.1271` n `18`; unknown avg `0.0272` n `644`
- 4h: commodity avg `-0.2918` n `12`; crypto_alt avg `0.5868` n `228`; crypto_major avg `0.9657` n `8`; equity avg `0.2741` n `74`; fx avg `-0.0168` n `6`; index avg `0.2955` n `23`; metal avg `0.0535` n `18`; unknown avg `0.4277` n `644`
- 24h: commodity avg `-1.0792` n `12`; crypto_alt avg `1.0255` n `228`; crypto_major avg `0.1294` n `8`; equity avg `0.1997` n `74`; fx avg `0.0168` n `6`; index avg `0.8917` n `23`; metal avg `1.0936` n `18`; unknown avg `0.2585` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
