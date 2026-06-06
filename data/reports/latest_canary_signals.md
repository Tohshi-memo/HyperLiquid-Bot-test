# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T20:37:19.829715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `0.162` n `228`; crypto_major avg `0.164` n `8`; equity avg `0.0925` n `74`; fx avg `-0.0022` n `6`; index avg `0.0463` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.0408` n `515`
- 1h: commodity avg `0.2338` n `12`; crypto_alt avg `-0.0391` n `228`; crypto_major avg `0.036` n `8`; equity avg `0.1731` n `74`; fx avg `-0.0108` n `6`; index avg `0.0558` n `23`; metal avg `-0.0056` n `18`; unknown avg `1.8677` n `515`
- 4h: commodity avg `0.1302` n `12`; crypto_alt avg `-0.1459` n `228`; crypto_major avg `-0.2937` n `8`; equity avg `0.2718` n `74`; fx avg `0.0481` n `6`; index avg `-0.105` n `23`; metal avg `0.0543` n `18`; unknown avg `0.566` n `515`
- 24h: commodity avg `0.4742` n `12`; crypto_alt avg `-2.142` n `228`; crypto_major avg `-2.0983` n `8`; equity avg `-0.4484` n `74`; fx avg `0.0603` n `6`; index avg `0.2673` n `23`; metal avg `-0.4099` n `18`; unknown avg `0.7352` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
