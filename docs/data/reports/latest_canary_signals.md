# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T13:07:29.559691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0494` n `12`; crypto_alt avg `-0.312` n `234`; crypto_major avg `-0.2249` n `8`; equity avg `-0.1604` n `141`; fx avg `-0.0137` n `6`; index avg `-0.0281` n `26`; metal avg `-0.0243` n `20`; unknown avg `0.1674` n `960`
- 1h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.027` n `234`; crypto_major avg `-0.0238` n `8`; equity avg `-0.1216` n `141`; fx avg `0.0233` n `6`; index avg `-0.0055` n `26`; metal avg `-0.1842` n `20`; unknown avg `245.3928` n `960`
- 4h: commodity avg `-0.1826` n `12`; crypto_alt avg `1.7242` n `234`; crypto_major avg `1.4504` n `8`; equity avg `0.4631` n `141`; fx avg `-0.023` n `6`; index avg `0.0937` n `26`; metal avg `0.0262` n `20`; unknown avg `42.9719` n `954`
- 24h: commodity avg `-0.285` n `12`; crypto_alt avg `-2.1978` n `234`; crypto_major avg `-1.6833` n `8`; equity avg `-2.4477` n `141`; fx avg `0.0051` n `6`; index avg `-0.1841` n `26`; metal avg `-0.9487` n `20`; unknown avg `3.836` n `814`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
