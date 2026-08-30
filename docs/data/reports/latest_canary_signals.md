# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T07:52:26.101087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.1084` n `231`; crypto_major avg `-0.0835` n `8`; equity avg `-0.0137` n `128`; fx avg `-0.0009` n `6`; index avg `-0.0114` n `26`; metal avg `0.0018` n `20`; unknown avg `0.0717` n `793`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.3371` n `231`; crypto_major avg `-0.218` n `8`; equity avg `-0.0346` n `128`; fx avg `-0.0031` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.0635` n `793`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.0326` n `231`; crypto_major avg `-0.088` n `8`; equity avg `-0.0021` n `128`; fx avg `0.0041` n `6`; index avg `0.0069` n `26`; metal avg `0.0083` n `20`; unknown avg `0.0888` n `759`
- 24h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.6328` n `231`; crypto_major avg `0.8104` n `8`; equity avg `0.2306` n `128`; fx avg `-0.0026` n `6`; index avg `0.0549` n `26`; metal avg `0.0972` n `20`; unknown avg `0.7498` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
