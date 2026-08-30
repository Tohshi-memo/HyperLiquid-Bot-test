# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T09:22:25.276226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0334` n `231`; crypto_major avg `-0.0375` n `8`; equity avg `-0.0121` n `128`; fx avg `-0.0036` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0334` n `793`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.0059` n `231`; crypto_major avg `-0.0686` n `8`; equity avg `-0.0031` n `128`; fx avg `-0.0006` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.0533` n `793`
- 4h: commodity avg `0.0024` n `12`; crypto_alt avg `0.126` n `231`; crypto_major avg `-0.0604` n `8`; equity avg `-0.0052` n `128`; fx avg `0.0051` n `6`; index avg `-0.0302` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0923` n `759`
- 24h: commodity avg `-0.0025` n `12`; crypto_alt avg `1.1134` n `231`; crypto_major avg `0.9272` n `8`; equity avg `0.2669` n `128`; fx avg `-0.0075` n `6`; index avg `0.0486` n `26`; metal avg `0.0723` n `20`; unknown avg `0.7354` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
