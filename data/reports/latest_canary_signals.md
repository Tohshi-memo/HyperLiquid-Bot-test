# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T05:52:27.022820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0747` n `230`; crypto_major avg `0.1324` n `8`; equity avg `0.0139` n `96`; fx avg `-0.0021` n `6`; index avg `0.0053` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0241` n `770`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `0.0836` n `230`; crypto_major avg `0.0508` n `8`; equity avg `0.0506` n `96`; fx avg `0.0146` n `6`; index avg `0.0048` n `25`; metal avg `-0.0023` n `20`; unknown avg `1.9389` n `770`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0494` n `230`; crypto_major avg `0.1235` n `8`; equity avg `0.0975` n `96`; fx avg `0.0089` n `6`; index avg `0.0036` n `25`; metal avg `0.019` n `20`; unknown avg `0.8496` n `770`
- 24h: commodity avg `0.3199` n `12`; crypto_alt avg `0.2695` n `230`; crypto_major avg `1.08` n `8`; equity avg `-0.009` n `96`; fx avg `-0.0128` n `6`; index avg `-0.0457` n `25`; metal avg `-0.0223` n `20`; unknown avg `0.1154` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
