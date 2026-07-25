# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T21:22:25.319098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0545` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `0.0242` n `100`; fx avg `0.0015` n `6`; index avg `0.0024` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.054` n `774`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `-0.1291` n `230`; crypto_major avg `-0.1427` n `8`; equity avg `0.0389` n `100`; fx avg `-0.0009` n `6`; index avg `0.0013` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.0108` n `774`
- 4h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.2046` n `230`; crypto_major avg `-0.214` n `8`; equity avg `0.1437` n `100`; fx avg `-0.0023` n `6`; index avg `0.0461` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0461` n `774`
- 24h: commodity avg `-0.6345` n `12`; crypto_alt avg `0.4385` n `230`; crypto_major avg `1.1437` n `8`; equity avg `0.4036` n `100`; fx avg `0.0129` n `6`; index avg `0.1337` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.3281` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1212`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
