# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T09:22:26.504074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.2721` n `233`; crypto_major avg `-0.1912` n `8`; equity avg `-0.0324` n `134`; fx avg `-0.0126` n `6`; index avg `-0.011` n `26`; metal avg `-0.0271` n `20`; unknown avg `13.5107` n `798`
- 1h: commodity avg `0.0767` n `12`; crypto_alt avg `-0.2573` n `233`; crypto_major avg `-0.2252` n `8`; equity avg `-0.1273` n `134`; fx avg `0.0031` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0452` n `20`; unknown avg `13.6656` n `790`
- 4h: commodity avg `0.1937` n `12`; crypto_alt avg `0.4433` n `233`; crypto_major avg `0.2359` n `8`; equity avg `0.2315` n `134`; fx avg `0.0076` n `6`; index avg `-0.0004` n `26`; metal avg `0.1059` n `20`; unknown avg `2.2259` n `772`
- 24h: commodity avg `-0.1075` n `12`; crypto_alt avg `0.5833` n `232`; crypto_major avg `1.5386` n `8`; equity avg `1.4089` n `134`; fx avg `-0.111` n `6`; index avg `0.0365` n `26`; metal avg `0.0087` n `20`; unknown avg `1.2814` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
