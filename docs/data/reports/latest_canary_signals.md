# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T05:37:28.974950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `-0.1677` n `228`; crypto_major avg `-0.0207` n `8`; equity avg `0.0098` n `78`; fx avg `-0.2966` n `6`; index avg `0.0041` n `23`; metal avg `0.0026` n `18`; unknown avg `4.0002` n `687`
- 1h: commodity avg `0.0767` n `12`; crypto_alt avg `0.3467` n `228`; crypto_major avg `0.64` n `8`; equity avg `0.17` n `78`; fx avg `-0.2975` n `6`; index avg `0.0188` n `23`; metal avg `0.0187` n `18`; unknown avg `0.7075` n `687`
- 4h: commodity avg `0.2322` n `12`; crypto_alt avg `0.1994` n `228`; crypto_major avg `0.7554` n `8`; equity avg `0.3703` n `78`; fx avg `-0.3149` n `6`; index avg `0.0619` n `23`; metal avg `0.0294` n `18`; unknown avg `0.4243` n `687`
- 24h: commodity avg `0.4943` n `12`; crypto_alt avg `-3.2393` n `228`; crypto_major avg `-3.5874` n `8`; equity avg `1.288` n `78`; fx avg `-0.3957` n `6`; index avg `0.333` n `23`; metal avg `-4.1036` n `18`; unknown avg `-0.4822` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
