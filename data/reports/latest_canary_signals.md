# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T11:52:29.058521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.2025` n `230`; crypto_major avg `-0.1378` n `8`; equity avg `-0.0169` n `96`; fx avg `-0.0105` n `6`; index avg `-0.0003` n `25`; metal avg `0.0023` n `20`; unknown avg `0.0048` n `770`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.2983` n `230`; crypto_major avg `-0.0709` n `8`; equity avg `-0.0522` n `96`; fx avg `-0.0124` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0197` n `770`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.1581` n `230`; crypto_major avg `0.0052` n `8`; equity avg `-0.0582` n `96`; fx avg `-0.0191` n `6`; index avg `0.0212` n `25`; metal avg `-0.0374` n `20`; unknown avg `-0.0362` n `770`
- 24h: commodity avg `0.1834` n `12`; crypto_alt avg `0.2342` n `230`; crypto_major avg `1.061` n `8`; equity avg `0.1658` n `96`; fx avg `-0.0138` n `6`; index avg `-0.0423` n `25`; metal avg `-0.0892` n `20`; unknown avg `0.1204` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1142`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1131`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
