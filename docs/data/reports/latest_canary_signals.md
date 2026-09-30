# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T00:52:30.833649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.0127` n `234`; crypto_major avg `-0.0667` n `8`; equity avg `-0.1684` n `142`; fx avg `0.0073` n `6`; index avg `-0.0399` n `26`; metal avg `-0.0112` n `20`; unknown avg `1.3573` n `963`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.0307` n `234`; crypto_major avg `-0.2154` n `8`; equity avg `-0.1874` n `142`; fx avg `0.0727` n `6`; index avg `-0.0533` n `26`; metal avg `-0.0571` n `20`; unknown avg `1.32` n `955`
- 4h: commodity avg `0.1072` n `12`; crypto_alt avg `-0.7205` n `234`; crypto_major avg `-0.3331` n `8`; equity avg `-0.0548` n `142`; fx avg `0.0595` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0014` n `20`; unknown avg `2.1659` n `926`
- 24h: commodity avg `-0.8858` n `12`; crypto_alt avg `0.1662` n `234`; crypto_major avg `-0.1803` n `8`; equity avg `0.8923` n `142`; fx avg `-0.1101` n `6`; index avg `0.13` n `26`; metal avg `0.2954` n `20`; unknown avg `3099.6579` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
