# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T01:22:37.313977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `-0.0829` n `8`; equity avg `-0.034` n `112`; fx avg `-0.001` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0866` n `784`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.0384` n `230`; crypto_major avg `-0.0275` n `8`; equity avg `0.0338` n `112`; fx avg `-0.0081` n `6`; index avg `0.0016` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.1463` n `784`
- 4h: commodity avg `0.0107` n `12`; crypto_alt avg `0.0063` n `230`; crypto_major avg `-0.2927` n `8`; equity avg `0.0401` n `112`; fx avg `0.0049` n `6`; index avg `0.0007` n `25`; metal avg `0.0206` n `20`; unknown avg `-0.1865` n `784`
- 24h: commodity avg `0.2044` n `12`; crypto_alt avg `1.8523` n `230`; crypto_major avg `1.0774` n `8`; equity avg `0.5636` n `112`; fx avg `-0.0064` n `6`; index avg `0.0644` n `25`; metal avg `-0.0187` n `20`; unknown avg `0.1972` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
