# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T20:37:27.069807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0993` n `228`; crypto_major avg `-0.0613` n `8`; equity avg `0.0071` n `74`; fx avg `-0.0014` n `6`; index avg `0.0147` n `23`; metal avg `-0.0199` n `18`; unknown avg `0.1076` n `516`
- 1h: commodity avg `-0.2655` n `12`; crypto_alt avg `0.7641` n `228`; crypto_major avg `0.7912` n `8`; equity avg `0.1442` n `74`; fx avg `-0.0058` n `6`; index avg `0.0672` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.4562` n `516`
- 4h: commodity avg `0.1686` n `12`; crypto_alt avg `-1.3229` n `228`; crypto_major avg `-0.4555` n `8`; equity avg `-0.7078` n `74`; fx avg `0.0073` n `6`; index avg `-0.2318` n `23`; metal avg `-0.264` n `18`; unknown avg `-2.3927` n `516`
- 24h: commodity avg `0.3698` n `12`; crypto_alt avg `1.9621` n `228`; crypto_major avg `3.2799` n `8`; equity avg `1.0686` n `74`; fx avg `-0.0579` n `6`; index avg `0.28` n `23`; metal avg `0.3279` n `18`; unknown avg `-4.4414` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
