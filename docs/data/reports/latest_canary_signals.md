# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T04:07:27.748482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.3434` n `234`; crypto_major avg `0.1771` n `8`; equity avg `0.0579` n `142`; fx avg `0.0013` n `6`; index avg `0.01` n `26`; metal avg `-0.0007` n `20`; unknown avg `2.8788` n `955`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `-0.0097` n `234`; crypto_major avg `-0.0907` n `8`; equity avg `0.0476` n `142`; fx avg `0.0046` n `6`; index avg `0.0249` n `26`; metal avg `-0.0717` n `20`; unknown avg `1.4969` n `955`
- 4h: commodity avg `0.0544` n `12`; crypto_alt avg `0.2342` n `234`; crypto_major avg `-0.0009` n `8`; equity avg `-0.3553` n `142`; fx avg `-0.0207` n `6`; index avg `-0.0574` n `26`; metal avg `-0.1517` n `20`; unknown avg `3.1555` n `955`
- 24h: commodity avg `-0.9383` n `12`; crypto_alt avg `2.0269` n `234`; crypto_major avg `0.4825` n `8`; equity avg `1.1343` n `142`; fx avg `-0.1551` n `6`; index avg `0.1891` n `26`; metal avg `0.225` n `20`; unknown avg `3229.3676` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
