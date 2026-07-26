# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T12:34:15.518348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.0819` n `230`; crypto_major avg `0.02` n `8`; equity avg `-0.002` n `100`; fx avg `-0.0007` n `6`; index avg `0.01` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0741` n `775`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0392` n `100`; fx avg `0.0083` n `6`; index avg `0.0024` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.117` n `775`
- 4h: commodity avg `-0.2861` n `12`; crypto_alt avg `-0.0` n `230`; crypto_major avg `0.1445` n `8`; equity avg `0.2658` n `100`; fx avg `0.0063` n `6`; index avg `0.0471` n `25`; metal avg `0.0981` n `20`; unknown avg `-0.1446` n `775`
- 24h: commodity avg `-0.83` n `12`; crypto_alt avg `1.6904` n `230`; crypto_major avg `1.7249` n `8`; equity avg `0.7342` n `100`; fx avg `0.026` n `6`; index avg `0.1772` n `25`; metal avg `0.1763` n `20`; unknown avg `0.0993` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
