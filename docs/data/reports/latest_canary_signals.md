# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T07:37:30.001172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `12`; crypto_alt avg `0.0436` n `230`; crypto_major avg `0.0513` n `8`; equity avg `0.0273` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0141` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0087` n `770`
- 1h: commodity avg `0.0552` n `12`; crypto_alt avg `0.0215` n `230`; crypto_major avg `0.0287` n `8`; equity avg `0.0389` n `96`; fx avg `0.0082` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.0526` n `770`
- 4h: commodity avg `0.0065` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `0.1446` n `8`; equity avg `0.1538` n `96`; fx avg `0.013` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0243` n `20`; unknown avg `-0.0005` n `752`
- 24h: commodity avg `0.3396` n `12`; crypto_alt avg `0.3845` n `230`; crypto_major avg `1.0298` n `8`; equity avg `0.07` n `96`; fx avg `-0.0022` n `6`; index avg `0.0024` n `25`; metal avg `-0.0483` n `20`; unknown avg `0.0464` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
