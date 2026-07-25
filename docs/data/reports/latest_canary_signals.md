# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T08:52:29.826543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.1436` n `230`; crypto_major avg `-0.1127` n `8`; equity avg `-0.0126` n `100`; fx avg `0.0184` n `6`; index avg `0.0071` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.1383` n `774`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.2372` n `230`; crypto_major avg `-0.148` n `8`; equity avg `-0.0555` n `100`; fx avg `0.0132` n `6`; index avg `0.0024` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0782` n `774`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `-0.6759` n `230`; crypto_major avg `-0.4616` n `8`; equity avg `-0.1372` n `100`; fx avg `0.0359` n `6`; index avg `-0.0026` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.3091` n `758`
- 24h: commodity avg `0.0389` n `12`; crypto_alt avg `-1.976` n `230`; crypto_major avg `-1.7709` n `8`; equity avg `-2.7722` n `100`; fx avg `-0.0143` n `6`; index avg `-0.236` n `25`; metal avg `-0.0577` n `20`; unknown avg `13.251` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.115`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
