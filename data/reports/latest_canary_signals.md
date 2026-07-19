# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T15:52:31.187674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0158` n `230`; crypto_major avg `-0.0491` n `8`; equity avg `-0.0191` n `96`; fx avg `0.0015` n `6`; index avg `-0.0042` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0012` n `770`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.0332` n `230`; crypto_major avg `-0.1451` n `8`; equity avg `-0.0668` n `96`; fx avg `0.0032` n `6`; index avg `-0.0149` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0009` n `770`
- 4h: commodity avg `0.0443` n `12`; crypto_alt avg `0.1635` n `230`; crypto_major avg `0.0509` n `8`; equity avg `-0.0507` n `96`; fx avg `0.0119` n `6`; index avg `-0.0212` n `25`; metal avg `0.01` n `20`; unknown avg `-0.023` n `770`
- 24h: commodity avg `0.25` n `12`; crypto_alt avg `0.4552` n `230`; crypto_major avg `0.9778` n `8`; equity avg `0.2341` n `96`; fx avg `0.005` n `6`; index avg `-0.0424` n `25`; metal avg `-0.0232` n `20`; unknown avg `0.0902` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1363`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1303`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
