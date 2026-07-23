# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T14:07:39.142128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `0.0276` n `230`; crypto_major avg `-0.0074` n `8`; equity avg `0.4008` n `100`; fx avg `-0.0063` n `6`; index avg `0.0136` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.0149` n `772`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.0347` n `230`; crypto_major avg `-0.2948` n `8`; equity avg `0.9642` n `100`; fx avg `-0.013` n `6`; index avg `0.0702` n `25`; metal avg `0.0226` n `20`; unknown avg `-0.0598` n `772`
- 4h: commodity avg `0.2712` n `12`; crypto_alt avg `-0.5381` n `230`; crypto_major avg `-1.0036` n `8`; equity avg `-0.4969` n `99`; fx avg `-0.001` n `6`; index avg `-0.2178` n `25`; metal avg `-0.3538` n `20`; unknown avg `0.1259` n `772`
- 24h: commodity avg `0.8989` n `12`; crypto_alt avg `-1.2869` n `230`; crypto_major avg `-1.608` n `8`; equity avg `-0.7576` n `99`; fx avg `-0.0792` n `6`; index avg `-0.1893` n `25`; metal avg `-0.9908` n `20`; unknown avg `-0.0688` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0652`, n `666`, weak_sample_signal
