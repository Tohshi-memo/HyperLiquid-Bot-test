# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T09:07:32.546234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `0.0461` n `230`; crypto_major avg `0.0192` n `8`; equity avg `-0.022` n `100`; fx avg `-0.0043` n `6`; index avg `-0.0103` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.4328` n `774`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.0352` n `230`; crypto_major avg `0.0242` n `8`; equity avg `-0.0508` n `100`; fx avg `0.0091` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.4179` n `774`
- 4h: commodity avg `0.0593` n `12`; crypto_alt avg `-0.6328` n `230`; crypto_major avg `-0.4686` n `8`; equity avg `-0.1305` n `100`; fx avg `0.0332` n `6`; index avg `-0.0201` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.2439` n `758`
- 24h: commodity avg `0.0931` n `12`; crypto_alt avg `-1.8399` n `230`; crypto_major avg `-1.5615` n `8`; equity avg `-2.8714` n `100`; fx avg `-0.0141` n `6`; index avg `-0.257` n `25`; metal avg `-0.0995` n `20`; unknown avg `13.29` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1155`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
