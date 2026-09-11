# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T01:13:25.367827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1624` n `12`; crypto_alt avg `0.3271` n `233`; crypto_major avg `0.3334` n `8`; equity avg `0.1531` n `136`; fx avg `-0.0257` n `6`; index avg `0.037` n `26`; metal avg `0.0137` n `20`; unknown avg `121.2146` n `794`
- 1h: commodity avg `-0.0952` n `12`; crypto_alt avg `0.3944` n `233`; crypto_major avg `0.3514` n `8`; equity avg `0.2932` n `136`; fx avg `-0.015` n `6`; index avg `0.0711` n `26`; metal avg `0.0658` n `20`; unknown avg `0.9129` n `788`
- 4h: commodity avg `-0.2812` n `12`; crypto_alt avg `-0.6978` n `233`; crypto_major avg `-0.5912` n `8`; equity avg `0.0308` n `136`; fx avg `-0.0248` n `6`; index avg `0.0447` n `26`; metal avg `0.0549` n `20`; unknown avg `0.9376` n `750`
- 24h: commodity avg `0.9897` n `12`; crypto_alt avg `-1.9499` n `233`; crypto_major avg `-2.146` n `8`; equity avg `-1.5641` n `136`; fx avg `0.1112` n `6`; index avg `-0.2281` n `26`; metal avg `-1.2207` n `20`; unknown avg `-0.6321` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
