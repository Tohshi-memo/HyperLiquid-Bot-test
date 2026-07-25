# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T05:37:25.208993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.1328` n `230`; crypto_major avg `-0.1675` n `8`; equity avg `-0.0046` n `100`; fx avg `0.0057` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0028` n `20`; unknown avg `2.5594` n `774`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.1756` n `230`; crypto_major avg `-0.1608` n `8`; equity avg `-0.036` n `100`; fx avg `0.0087` n `6`; index avg `0.0048` n `25`; metal avg `0.0025` n `20`; unknown avg `0.8482` n `774`
- 4h: commodity avg `-0.1278` n `12`; crypto_alt avg `-0.1602` n `230`; crypto_major avg `-0.127` n `8`; equity avg `0.1732` n `100`; fx avg `-0.0241` n `6`; index avg `0.0489` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.134` n `774`
- 24h: commodity avg `-0.4309` n `12`; crypto_alt avg `-1.2816` n `230`; crypto_major avg `-1.1156` n `8`; equity avg `-2.5168` n `100`; fx avg `-0.0592` n `6`; index avg `-0.1684` n `25`; metal avg `0.1708` n `20`; unknown avg `13.6894` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1148`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1033`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1001`, n `666`, weak_sample_signal
