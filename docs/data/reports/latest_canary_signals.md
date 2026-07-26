# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T12:37:29.505817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0294` n `12`; crypto_alt avg `0.0781` n `230`; crypto_major avg `0.0197` n `8`; equity avg `0.0006` n `100`; fx avg `-0.0007` n `6`; index avg `0.014` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0777` n `775`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `0.0051` n `230`; crypto_major avg `-0.012` n `8`; equity avg `-0.0367` n `100`; fx avg `0.0083` n `6`; index avg `0.0065` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.1207` n `775`
- 4h: commodity avg `-0.2761` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `0.1443` n `8`; equity avg `0.2684` n `100`; fx avg `0.0063` n `6`; index avg `0.0512` n `25`; metal avg `0.093` n `20`; unknown avg `-0.1449` n `775`
- 24h: commodity avg `-0.8203` n `12`; crypto_alt avg `1.6871` n `230`; crypto_major avg `1.7243` n `8`; equity avg `0.7368` n `100`; fx avg `0.026` n `6`; index avg `0.1813` n `25`; metal avg `0.1712` n `20`; unknown avg `0.0973` n `758`

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
