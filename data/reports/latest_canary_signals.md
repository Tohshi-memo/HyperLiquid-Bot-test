# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T01:58:35.590060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `0.121` n `228`; crypto_major avg `0.0235` n `8`; equity avg `0.0087` n `88`; fx avg `-0.0069` n `6`; index avg `0.003` n `23`; metal avg `0.0123` n `20`; unknown avg `8.3779` n `764`
- 1h: commodity avg `0.1255` n `12`; crypto_alt avg `0.0603` n `228`; crypto_major avg `0.0954` n `8`; equity avg `-0.0573` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0198` n `23`; metal avg `0.0126` n `20`; unknown avg `28.8665` n `764`
- 4h: commodity avg `0.3351` n `12`; crypto_alt avg `0.2881` n `228`; crypto_major avg `-0.0708` n `8`; equity avg `-0.1087` n `88`; fx avg `-0.0284` n `6`; index avg `-0.0879` n `23`; metal avg `0.0427` n `20`; unknown avg `-0.6421` n `764`
- 24h: commodity avg `0.4749` n `12`; crypto_alt avg `-0.3773` n `228`; crypto_major avg `-0.6768` n `8`; equity avg `0.1621` n `88`; fx avg `-0.0088` n `6`; index avg `-0.1099` n `23`; metal avg `-0.0409` n `20`; unknown avg `-0.4496` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
