# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T17:37:28.162775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.0849` n `230`; crypto_major avg `-0.107` n `8`; equity avg `-0.1121` n `100`; fx avg `0.0019` n `6`; index avg `-0.0323` n `25`; metal avg `-0.0477` n `20`; unknown avg `-0.2078` n `772`
- 1h: commodity avg `0.0387` n `12`; crypto_alt avg `-0.1504` n `230`; crypto_major avg `-0.0607` n `8`; equity avg `-0.2022` n `100`; fx avg `0.0033` n `6`; index avg `-0.0699` n `25`; metal avg `-0.0236` n `20`; unknown avg `-0.2847` n `772`
- 4h: commodity avg `0.2425` n `12`; crypto_alt avg `-0.5358` n `230`; crypto_major avg `-0.7513` n `8`; equity avg `-0.2259` n `100`; fx avg `0.0011` n `6`; index avg `-0.1537` n `25`; metal avg `-0.1707` n `20`; unknown avg `-0.414` n `772`
- 24h: commodity avg `0.9963` n `12`; crypto_alt avg `-1.6017` n `230`; crypto_major avg `-2.1417` n `8`; equity avg `-1.3113` n `99`; fx avg `-0.0799` n `6`; index avg `-0.3863` n `25`; metal avg `-0.8157` n `20`; unknown avg `-0.4979` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
