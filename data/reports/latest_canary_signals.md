# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T03:37:24.998781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.1288` n `231`; crypto_major avg `0.1096` n `8`; equity avg `0.0077` n `128`; fx avg `0.0` n `6`; index avg `0.0056` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.1517` n `793`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.3171` n `231`; crypto_major avg `0.0657` n `8`; equity avg `-0.0071` n `128`; fx avg `0.0033` n `6`; index avg `0.0002` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0775` n `793`
- 4h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.1567` n `231`; crypto_major avg `-0.0483` n `8`; equity avg `0.0102` n `128`; fx avg `0.0177` n `6`; index avg `0.0031` n `26`; metal avg `-0.0012` n `20`; unknown avg `3.4702` n `793`
- 24h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.5952` n `231`; crypto_major avg `0.809` n `8`; equity avg `0.3376` n `128`; fx avg `-0.0032` n `6`; index avg `0.0666` n `26`; metal avg `0.0973` n `20`; unknown avg `0.1324` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
