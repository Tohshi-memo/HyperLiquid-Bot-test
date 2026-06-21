# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T05:37:27.714045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `0.0496` n `228`; crypto_major avg `0.0555` n `8`; equity avg `0.0061` n `78`; fx avg `0.0022` n `6`; index avg `-0.0002` n `23`; metal avg `0.0065` n `18`; unknown avg `6.8222` n `702`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.1797` n `228`; crypto_major avg `-0.3501` n `8`; equity avg `0.0147` n `78`; fx avg `0.004` n `6`; index avg `0.005` n `23`; metal avg `-0.0011` n `18`; unknown avg `4.708` n `678`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `-0.2021` n `228`; crypto_major avg `-0.2794` n `8`; equity avg `0.1831` n `78`; fx avg `-0.0061` n `6`; index avg `0.0223` n `23`; metal avg `0.0373` n `18`; unknown avg `-0.2153` n `678`
- 24h: commodity avg `0.145` n `12`; crypto_alt avg `1.0255` n `228`; crypto_major avg `0.3882` n `8`; equity avg `0.2442` n `78`; fx avg `0.3611` n `6`; index avg `-0.0159` n `23`; metal avg `-0.043` n `18`; unknown avg `-0.3043` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
