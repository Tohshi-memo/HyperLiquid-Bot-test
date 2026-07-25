# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T23:07:26.245688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.0478` n `230`; crypto_major avg `-0.0218` n `8`; equity avg `-0.0061` n `100`; fx avg `-0.0167` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0206` n `774`
- 1h: commodity avg `-0.0577` n `12`; crypto_alt avg `-0.0703` n `230`; crypto_major avg `0.0199` n `8`; equity avg `0.0235` n `100`; fx avg `-0.0194` n `6`; index avg `0.0048` n `25`; metal avg `-0.0176` n `20`; unknown avg `-0.0989` n `774`
- 4h: commodity avg `-0.0477` n `12`; crypto_alt avg `-0.0676` n `230`; crypto_major avg `-0.2439` n `8`; equity avg `0.0937` n `100`; fx avg `-0.0143` n `6`; index avg `0.0296` n `25`; metal avg `-0.0206` n `20`; unknown avg `-0.0942` n `774`
- 24h: commodity avg `-0.6591` n `12`; crypto_alt avg `0.517` n `230`; crypto_major avg `1.0743` n `8`; equity avg `0.4095` n `100`; fx avg `-0.0688` n `6`; index avg `0.1499` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.2981` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
