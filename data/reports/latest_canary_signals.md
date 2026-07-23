# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T18:37:27.309696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.121` n `12`; crypto_alt avg `0.1927` n `230`; crypto_major avg `0.1334` n `8`; equity avg `0.0033` n `100`; fx avg `0.0019` n `6`; index avg `0.0038` n `25`; metal avg `0.0269` n `20`; unknown avg `0.0471` n `772`
- 1h: commodity avg `-0.0885` n `12`; crypto_alt avg `-0.2162` n `230`; crypto_major avg `-0.0993` n `8`; equity avg `-0.3138` n `100`; fx avg `0.0027` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.1789` n `772`
- 4h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.9595` n `230`; crypto_major avg `-1.0046` n `8`; equity avg `-0.8223` n `100`; fx avg `0.0012` n `6`; index avg `-0.1093` n `25`; metal avg `-0.1539` n `20`; unknown avg `-0.5143` n `772`
- 24h: commodity avg `0.8683` n `12`; crypto_alt avg `-1.3412` n `230`; crypto_major avg `-1.7959` n `8`; equity avg `-1.1335` n `99`; fx avg `-0.0857` n `6`; index avg `-0.3345` n `25`; metal avg `-0.8085` n `20`; unknown avg `-0.5005` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
