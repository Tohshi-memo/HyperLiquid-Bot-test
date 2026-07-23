# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T14:52:32.060570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `12`; crypto_alt avg `-0.3046` n `230`; crypto_major avg `-0.3553` n `8`; equity avg `-0.6288` n `100`; fx avg `-0.0086` n `6`; index avg `-0.1015` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.1008` n `772`
- 1h: commodity avg `0.0585` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `-0.0844` n `8`; equity avg `-0.447` n `100`; fx avg `-0.0233` n `6`; index avg `-0.1153` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0772` n `772`
- 4h: commodity avg `0.2843` n `12`; crypto_alt avg `-0.5137` n `230`; crypto_major avg `-1.1327` n `8`; equity avg `-1.4548` n `99`; fx avg `-0.0143` n `6`; index avg `-0.3858` n `25`; metal avg `-0.3505` n `20`; unknown avg `0.1011` n `772`
- 24h: commodity avg `0.9814` n `12`; crypto_alt avg `-0.8524` n `230`; crypto_major avg `-1.192` n `8`; equity avg `-1.2743` n `99`; fx avg `-0.081` n `6`; index avg `-0.2895` n `25`; metal avg `-0.786` n `20`; unknown avg `-0.3111` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0616`, n `666`, weak_sample_signal
