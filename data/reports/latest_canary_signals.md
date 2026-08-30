# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T05:52:24.866327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.0571` n `231`; crypto_major avg `0.0335` n `8`; equity avg `0.0265` n `128`; fx avg `0.0037` n `6`; index avg `-0.0098` n `26`; metal avg `0.0053` n `20`; unknown avg `0.094` n `793`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.5179` n `231`; crypto_major avg `0.2692` n `8`; equity avg `0.0471` n `128`; fx avg `0.0031` n `6`; index avg `0.0205` n `26`; metal avg `0.0116` n `20`; unknown avg `-0.3355` n `793`
- 4h: commodity avg `0.0001` n `12`; crypto_alt avg `0.4651` n `231`; crypto_major avg `0.0311` n `8`; equity avg `0.06` n `128`; fx avg `0.0089` n `6`; index avg `0.0197` n `26`; metal avg `0.004` n `20`; unknown avg `-0.596` n `793`
- 24h: commodity avg `0.0296` n `12`; crypto_alt avg `0.3321` n `231`; crypto_major avg `0.577` n `8`; equity avg `0.3168` n `128`; fx avg `-0.0091` n `6`; index avg `0.067` n `26`; metal avg `0.0909` n `20`; unknown avg `0.1199` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
