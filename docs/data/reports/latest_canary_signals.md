# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T12:37:31.289696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0101` n `230`; crypto_major avg `0.103` n `8`; equity avg `0.049` n `96`; fx avg `0.0` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0018` n `770`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `-0.2138` n `230`; crypto_major avg `-0.1957` n `8`; equity avg `-0.0359` n `96`; fx avg `-0.0057` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0275` n `770`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `-0.184` n `230`; crypto_major avg `-0.0602` n `8`; equity avg `-0.1425` n `96`; fx avg `-0.0019` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0532` n `20`; unknown avg `0.0006` n `770`
- 24h: commodity avg `0.2336` n `12`; crypto_alt avg `0.2668` n `230`; crypto_major avg `0.9987` n `8`; equity avg `0.2347` n `96`; fx avg `-0.0098` n `6`; index avg `-0.0326` n `25`; metal avg `-0.0961` n `20`; unknown avg `0.1257` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1161`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1149`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
