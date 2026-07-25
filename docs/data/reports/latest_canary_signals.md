# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T10:51:22.213824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `0.0544` n `230`; crypto_major avg `0.0362` n `8`; equity avg `0.0195` n `100`; fx avg `-0.0053` n `6`; index avg `0.0035` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0056` n `774`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.0925` n `230`; crypto_major avg `-0.1047` n `8`; equity avg `0.0328` n `100`; fx avg `0.0037` n `6`; index avg `0.0025` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.005` n `774`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `0.0735` n `230`; crypto_major avg `0.1587` n `8`; equity avg `-0.0767` n `100`; fx avg `0.0091` n `6`; index avg `0.0039` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.1802` n `774`
- 24h: commodity avg `-0.0956` n `12`; crypto_alt avg `-1.3129` n `230`; crypto_major avg `-1.0643` n `8`; equity avg `-2.8381` n `100`; fx avg `-0.0162` n `6`; index avg `-0.2312` n `25`; metal avg `-0.1336` n `20`; unknown avg `13.1866` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1008`, n `666`, weak_sample_signal
