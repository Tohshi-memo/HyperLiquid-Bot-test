# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T14:17:24.480642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.18` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.2211` n `228`; crypto_major avg `0.2027` n `8`; equity avg `0.1255` n `74`; fx avg `-0.0031` n `6`; index avg `0.0101` n `23`; metal avg `0.0432` n `18`; unknown avg `0.0754` n `516`
- 1h: commodity avg `-0.0702` n `12`; crypto_alt avg `0.5534` n `228`; crypto_major avg `0.5141` n `8`; equity avg `0.5545` n `74`; fx avg `-0.0051` n `6`; index avg `0.1937` n `23`; metal avg `0.1053` n `18`; unknown avg `0.1396` n `516`
- 4h: commodity avg `0.1684` n `12`; crypto_alt avg `-0.5755` n `228`; crypto_major avg `-0.646` n `8`; equity avg `0.4993` n `74`; fx avg `0.0101` n `6`; index avg `0.3364` n `23`; metal avg `-0.0909` n `18`; unknown avg `0.0914` n `516`
- 24h: commodity avg `0.0848` n `12`; crypto_alt avg `1.495` n `228`; crypto_major avg `1.798` n `8`; equity avg `1.654` n `74`; fx avg `0.0215` n `6`; index avg `0.3649` n `23`; metal avg `0.6218` n `18`; unknown avg `-2.7715` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
