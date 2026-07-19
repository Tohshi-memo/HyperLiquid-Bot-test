# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T08:37:25.316418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.01` n `230`; crypto_major avg `-0.0057` n `8`; equity avg `-0.0175` n `96`; fx avg `-0.0154` n `6`; index avg `0.0016` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0396` n `770`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `-0.0729` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `0.0939` n `96`; fx avg `-0.0069` n `6`; index avg `0.0165` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0293` n `770`
- 4h: commodity avg `0.0545` n `12`; crypto_alt avg `-0.0089` n `230`; crypto_major avg `0.001` n `8`; equity avg `0.1377` n `96`; fx avg `0.0245` n `6`; index avg `0.0282` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.0295` n `752`
- 24h: commodity avg `0.3332` n `12`; crypto_alt avg `0.2388` n `230`; crypto_major avg `0.9171` n `8`; equity avg `0.1984` n `96`; fx avg `-0.0032` n `6`; index avg `-0.0262` n `25`; metal avg `-0.059` n `20`; unknown avg `-0.0186` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
