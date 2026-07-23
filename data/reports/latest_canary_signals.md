# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T20:07:26.757983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.4331` n `230`; crypto_major avg `0.5399` n `8`; equity avg `0.612` n `100`; fx avg `-0.0011` n `6`; index avg `0.1319` n `25`; metal avg `0.0173` n `20`; unknown avg `0.5763` n `772`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.1795` n `230`; crypto_major avg `0.1496` n `8`; equity avg `0.5325` n `100`; fx avg `0.0105` n `6`; index avg `0.145` n `25`; metal avg `0.0446` n `20`; unknown avg `0.2801` n `772`
- 4h: commodity avg `-0.1135` n `12`; crypto_alt avg `-0.3606` n `230`; crypto_major avg `-0.2477` n `8`; equity avg `0.1495` n `100`; fx avg `0.0142` n `6`; index avg `0.0736` n `25`; metal avg `-0.0597` n `20`; unknown avg `-0.3162` n `772`
- 24h: commodity avg `0.8605` n `12`; crypto_alt avg `-1.2576` n `230`; crypto_major avg `-1.7839` n `8`; equity avg `-0.6873` n `99`; fx avg `-0.0691` n `6`; index avg `-0.1923` n `25`; metal avg `-0.7686` n `20`; unknown avg `-0.294` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
