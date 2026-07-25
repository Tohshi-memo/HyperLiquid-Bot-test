# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T07:37:30.945471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.047` n `230`; crypto_major avg `-0.0449` n `8`; equity avg `-0.0039` n `100`; fx avg `-0.0244` n `6`; index avg `0.0128` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.07` n `774`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `0.0677` n `230`; crypto_major avg `0.0223` n `8`; equity avg `-0.0621` n `100`; fx avg `0.0119` n `6`; index avg `-0.0033` n `25`; metal avg `0.0135` n `20`; unknown avg `-0.1704` n `774`
- 4h: commodity avg `0.0306` n `12`; crypto_alt avg `-0.4043` n `230`; crypto_major avg `-0.2897` n `8`; equity avg `-0.0328` n `100`; fx avg `0.0196` n `6`; index avg `0.0167` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.2344` n `758`
- 24h: commodity avg `-0.1288` n `12`; crypto_alt avg `-1.8735` n `230`; crypto_major avg `-1.6861` n `8`; equity avg `-2.8239` n `100`; fx avg `-0.0755` n `6`; index avg `-0.2281` n `25`; metal avg `-0.0362` n `20`; unknown avg `13.4482` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.115`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
