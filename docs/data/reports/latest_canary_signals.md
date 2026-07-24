# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T01:07:30.756359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1044` n `12`; crypto_alt avg `0.2463` n `230`; crypto_major avg `0.1952` n `8`; equity avg `0.2192` n `100`; fx avg `-0.0196` n `6`; index avg `0.0383` n `25`; metal avg `-0.0461` n `20`; unknown avg `-0.0976` n `772`
- 1h: commodity avg `-0.1449` n `12`; crypto_alt avg `0.2168` n `230`; crypto_major avg `0.1733` n `8`; equity avg `0.1508` n `100`; fx avg `-0.0471` n `6`; index avg `-0.0105` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.1231` n `772`
- 4h: commodity avg `-0.1558` n `12`; crypto_alt avg `-0.4378` n `230`; crypto_major avg `-0.3053` n `8`; equity avg `-0.5145` n `100`; fx avg `-0.07` n `6`; index avg `-0.1139` n `25`; metal avg `-0.0844` n `20`; unknown avg `-0.7469` n `772`
- 24h: commodity avg `0.5271` n `12`; crypto_alt avg `-1.8262` n `230`; crypto_major avg `-2.4152` n `8`; equity avg `-1.8664` n `99`; fx avg `-0.0944` n `6`; index avg `-0.4651` n `25`; metal avg `-0.8277` n `20`; unknown avg `-0.3765` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
