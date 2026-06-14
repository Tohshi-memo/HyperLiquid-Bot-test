# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T10:07:33.901575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0499` n `12`; crypto_alt avg `-0.0817` n `228`; crypto_major avg `-0.0359` n `8`; equity avg `0.0305` n `74`; fx avg `0.0029` n `6`; index avg `0.051` n `23`; metal avg `-0.0031` n `18`; unknown avg `0.0703` n `645`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `0.1224` n `228`; crypto_major avg `0.1926` n `8`; equity avg `0.15` n `74`; fx avg `-0.0048` n `6`; index avg `0.0111` n `23`; metal avg `-0.0069` n `18`; unknown avg `-0.0045` n `629`
- 4h: commodity avg `-0.1836` n `12`; crypto_alt avg `-0.2427` n `228`; crypto_major avg `-0.0629` n `8`; equity avg `0.3185` n `74`; fx avg `-0.0228` n `6`; index avg `0.0404` n `23`; metal avg `0.0169` n `18`; unknown avg `1.926` n `625`
- 24h: commodity avg `-0.6933` n `12`; crypto_alt avg `0.2375` n `228`; crypto_major avg `0.993` n `8`; equity avg `0.9105` n `74`; fx avg `-0.0278` n `6`; index avg `0.2463` n `23`; metal avg `0.2933` n `18`; unknown avg `25.1647` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
