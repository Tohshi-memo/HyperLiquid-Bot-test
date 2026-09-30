# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T01:07:28.835277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.5154` n `234`; crypto_major avg `0.1947` n `8`; equity avg `0.0655` n `142`; fx avg `-0.0146` n `6`; index avg `0.0085` n `26`; metal avg `-0.0337` n `20`; unknown avg `2.6282` n `961`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.3849` n `234`; crypto_major avg `-0.0134` n `8`; equity avg `-0.2259` n `142`; fx avg `0.0539` n `6`; index avg `-0.0543` n `26`; metal avg `-0.0742` n `20`; unknown avg `2.9184` n `961`
- 4h: commodity avg `0.12` n `12`; crypto_alt avg `-0.1608` n `234`; crypto_major avg `-0.0917` n `8`; equity avg `0.006` n `142`; fx avg `0.0421` n `6`; index avg `0.0098` n `26`; metal avg `-0.0459` n `20`; unknown avg `2.6293` n `928`
- 24h: commodity avg `-0.8717` n `12`; crypto_alt avg `1.0611` n `234`; crypto_major avg `0.2489` n `8`; equity avg `1.0129` n `142`; fx avg `-0.0849` n `6`; index avg `0.1303` n `26`; metal avg `0.2635` n `20`; unknown avg `3100.276` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
