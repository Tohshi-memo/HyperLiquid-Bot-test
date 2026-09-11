# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T23:37:30.060111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `0.0506` n `233`; crypto_major avg `0.0251` n `8`; equity avg `-0.0137` n `136`; fx avg `-0.0068` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.019` n `834`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `0.251` n `233`; crypto_major avg `0.164` n `8`; equity avg `0.0084` n `136`; fx avg `-0.003` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0184` n `20`; unknown avg `1.0472` n `828`
- 4h: commodity avg `-0.1431` n `12`; crypto_alt avg `-0.3538` n `233`; crypto_major avg `-0.3576` n `8`; equity avg `-0.0444` n `136`; fx avg `-0.0293` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0237` n `20`; unknown avg `1.143` n `788`
- 24h: commodity avg `-0.7958` n `12`; crypto_alt avg `0.7937` n `233`; crypto_major avg `1.3611` n `8`; equity avg `0.908` n `136`; fx avg `-0.2077` n `6`; index avg `0.3238` n `26`; metal avg `0.2707` n `20`; unknown avg `2.2876` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
