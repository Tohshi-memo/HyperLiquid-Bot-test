# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T23:37:26.153736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `-0.1219` n `100`; fx avg `-0.0004` n `6`; index avg `-0.0079` n `25`; metal avg `0.011` n `20`; unknown avg `-0.0723` n `772`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0471` n `230`; crypto_major avg `-0.0004` n `8`; equity avg `-0.0436` n `100`; fx avg `0.0051` n `6`; index avg `0.0327` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.0989` n `772`
- 4h: commodity avg `0.0388` n `12`; crypto_alt avg `-0.1211` n `230`; crypto_major avg `0.077` n `8`; equity avg `0.0189` n `100`; fx avg `-0.0111` n `6`; index avg `0.0491` n `25`; metal avg `0.0228` n `20`; unknown avg `0.1086` n `772`
- 24h: commodity avg `0.6527` n `12`; crypto_alt avg `-1.4393` n `230`; crypto_major avg `-1.9712` n `8`; equity avg `-1.2383` n `99`; fx avg `-0.0705` n `6`; index avg `-0.2429` n `25`; metal avg `-0.686` n `20`; unknown avg `-0.2696` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
