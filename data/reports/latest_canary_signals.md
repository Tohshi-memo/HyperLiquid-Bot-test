# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T07:26:26.144156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0396` n `230`; crypto_major avg `-0.0277` n `8`; equity avg `0.1361` n `98`; fx avg `0.0129` n `6`; index avg `0.0334` n `25`; metal avg `0.0742` n `20`; unknown avg `-0.0228` n `772`
- 1h: commodity avg `0.1196` n `12`; crypto_alt avg `-0.0048` n `230`; crypto_major avg `0.0012` n `8`; equity avg `0.1329` n `98`; fx avg `-0.0051` n `6`; index avg `0.0282` n `25`; metal avg `-0.0522` n `20`; unknown avg `-0.0193` n `772`
- 4h: commodity avg `0.2245` n `12`; crypto_alt avg `-0.8204` n `230`; crypto_major avg `-1.0367` n `8`; equity avg `-0.9884` n `98`; fx avg `-0.0271` n `6`; index avg `-0.2157` n `25`; metal avg `-0.1995` n `20`; unknown avg `-0.2521` n `739`
- 24h: commodity avg `0.6596` n `12`; crypto_alt avg `-1.1197` n `230`; crypto_major avg `-1.5407` n `8`; equity avg `0.8459` n `98`; fx avg `0.013` n `6`; index avg `0.044` n `25`; metal avg `0.328` n `20`; unknown avg `-0.0094` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0698`, n `666`, weak_sample_signal
