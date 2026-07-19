# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T14:52:27.020258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.0959` n `230`; crypto_major avg `0.1307` n `8`; equity avg `-0.0031` n `96`; fx avg `-0.0001` n `6`; index avg `0.0021` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0421` n `770`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `0.1286` n `230`; crypto_major avg `0.1772` n `8`; equity avg `-0.0385` n `96`; fx avg `-0.0001` n `6`; index avg `0.008` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.0324` n `770`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.1065` n `230`; crypto_major avg `0.1251` n `8`; equity avg `-0.0359` n `96`; fx avg `-0.0037` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0412` n `770`
- 24h: commodity avg `0.2521` n `12`; crypto_alt avg `0.4563` n `230`; crypto_major avg `1.0307` n `8`; equity avg `0.2594` n `96`; fx avg `0.0023` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0408` n `20`; unknown avg `0.1143` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1279`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
