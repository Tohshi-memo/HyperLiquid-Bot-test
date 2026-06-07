# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T02:37:19.395279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0514` n `12`; crypto_alt avg `-0.2818` n `228`; crypto_major avg `-0.1185` n `8`; equity avg `-0.0782` n `74`; fx avg `-0.0007` n `6`; index avg `0.0025` n `23`; metal avg `0.0119` n `18`; unknown avg `0.0512` n `516`
- 1h: commodity avg `-0.1061` n `12`; crypto_alt avg `-0.7754` n `228`; crypto_major avg `-0.5109` n `8`; equity avg `-0.1621` n `74`; fx avg `-0.0001` n `6`; index avg `-0.0065` n `23`; metal avg `0.0925` n `18`; unknown avg `-0.1587` n `516`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `1.7679` n `228`; crypto_major avg `1.605` n `8`; equity avg `0.6156` n `74`; fx avg `-0.012` n `6`; index avg `0.1052` n `23`; metal avg `0.3437` n `18`; unknown avg `0.7916` n `515`
- 24h: commodity avg `-0.0332` n `12`; crypto_alt avg `0.7285` n `228`; crypto_major avg `0.0221` n `8`; equity avg `1.3911` n `74`; fx avg `0.0393` n `6`; index avg `0.611` n `23`; metal avg `0.3825` n `18`; unknown avg `-0.011` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
