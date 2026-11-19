# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T15:07:27.328382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0676` n `13`; crypto_alt avg `0.048` n `239`; crypto_major avg `0.0991` n `8`; equity avg `-0.1564` n `165`; fx avg `-0.0174` n `6`; index avg `-0.0127` n `27`; metal avg `0.097` n `20`; unknown avg `0.3522` n `1259`
- 1h: commodity avg `-0.0542` n `13`; crypto_alt avg `-0.0863` n `239`; crypto_major avg `0.1627` n `8`; equity avg `0.5807` n `165`; fx avg `-0.038` n `6`; index avg `0.0168` n `27`; metal avg `0.0457` n `20`; unknown avg `3.8558` n `1263`
- 4h: commodity avg `0.1566` n `13`; crypto_alt avg `0.1894` n `239`; crypto_major avg `0.6604` n `8`; equity avg `0.2848` n `165`; fx avg `-0.0684` n `6`; index avg `-0.0369` n `27`; metal avg `-0.0841` n `20`; unknown avg `0.4822` n `1257`
- 24h: commodity avg `0.2772` n `13`; crypto_alt avg `0.8318` n `239`; crypto_major avg `1.3171` n `8`; equity avg `2.4323` n `165`; fx avg `0.0119` n `6`; index avg `0.3564` n `27`; metal avg `-0.1018` n `20`; unknown avg `0.9195` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
