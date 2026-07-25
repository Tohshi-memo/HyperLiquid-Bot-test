# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T07:34:58.230348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `-0.0363` n `8`; equity avg `-0.028` n `100`; fx avg `0.03` n `6`; index avg `-0.0097` n `25`; metal avg `0.0072` n `20`; unknown avg `0.0777` n `774`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `-0.0883` n `230`; crypto_major avg `-0.0455` n `8`; equity avg `-0.0532` n `100`; fx avg `0.0465` n `6`; index avg `-0.0134` n `25`; metal avg `0.012` n `20`; unknown avg `0.0701` n `774`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `-0.2719` n `230`; crypto_major avg `-0.2091` n `8`; equity avg `-0.0346` n `100`; fx avg `0.0455` n `6`; index avg `0.0047` n `25`; metal avg `0.003` n `20`; unknown avg `-0.1041` n `758`
- 24h: commodity avg `-0.1515` n `12`; crypto_alt avg `-2.0414` n `230`; crypto_major avg `-1.9673` n `8`; equity avg `-2.8098` n `100`; fx avg `-0.0511` n `6`; index avg `-0.246` n `25`; metal avg `-0.0229` n `20`; unknown avg `13.5595` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1148`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
