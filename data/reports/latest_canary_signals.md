# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T08:37:28.931093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `-0.5607` n `234`; crypto_major avg `-0.5983` n `8`; equity avg `-0.1293` n `141`; fx avg `-0.0227` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0594` n `20`; unknown avg `1.5742` n `963`
- 1h: commodity avg `-0.094` n `12`; crypto_alt avg `-0.0908` n `234`; crypto_major avg `-0.3264` n `8`; equity avg `0.1187` n `141`; fx avg `0.003` n `6`; index avg `-0.0098` n `26`; metal avg `-0.052` n `20`; unknown avg `0.2265` n `945`
- 4h: commodity avg `-0.3147` n `12`; crypto_alt avg `1.7888` n `234`; crypto_major avg `1.0568` n `8`; equity avg `0.9371` n `141`; fx avg `-0.0539` n `6`; index avg `0.1293` n `26`; metal avg `0.0489` n `20`; unknown avg `1.3691` n `927`
- 24h: commodity avg `-0.3591` n `12`; crypto_alt avg `1.0691` n `234`; crypto_major avg `0.9217` n `8`; equity avg `-0.134` n `141`; fx avg `-0.0384` n `6`; index avg `-0.0259` n `26`; metal avg `-0.1917` n `20`; unknown avg `55.5152` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
