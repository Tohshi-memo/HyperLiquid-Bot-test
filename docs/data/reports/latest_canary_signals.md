# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T14:48:36.343731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `0.1198` n `230`; crypto_major avg `0.1714` n `8`; equity avg `0.0041` n `96`; fx avg `-0.0001` n `6`; index avg `0.0015` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0191` n `770`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `0.1527` n `230`; crypto_major avg `0.2179` n `8`; equity avg `-0.0313` n `96`; fx avg `-0.0001` n `6`; index avg `0.0075` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0114` n `770`
- 4h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0829` n `230`; crypto_major avg `0.1658` n `8`; equity avg `-0.0286` n `96`; fx avg `-0.0037` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.054` n `770`
- 24h: commodity avg `0.2568` n `12`; crypto_alt avg `0.4797` n `230`; crypto_major avg `1.0721` n `8`; equity avg `0.2668` n `96`; fx avg `0.0023` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0389` n `20`; unknown avg `0.116` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1279`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
