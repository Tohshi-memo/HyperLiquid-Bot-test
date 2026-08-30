# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T06:07:26.557531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0016` n `231`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0039` n `128`; fx avg `0.0051` n `6`; index avg `-0.006` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0548` n `761`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1419` n `231`; crypto_major avg `-0.0488` n `8`; equity avg `0.0185` n `128`; fx avg `0.0088` n `6`; index avg `0.0028` n `26`; metal avg `0.0026` n `20`; unknown avg `0.061` n `761`
- 4h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.4986` n `231`; crypto_major avg `0.0378` n `8`; equity avg `0.044` n `128`; fx avg `0.0142` n `6`; index avg `0.0045` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.0256` n `761`
- 24h: commodity avg `0.019` n `12`; crypto_alt avg `0.6884` n `231`; crypto_major avg `0.8299` n `8`; equity avg `0.3165` n `128`; fx avg `-0.0025` n `6`; index avg `0.0606` n `26`; metal avg `0.0946` n `20`; unknown avg `0.2576` n `712`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
