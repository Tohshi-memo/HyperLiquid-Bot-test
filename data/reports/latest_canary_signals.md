# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T02:22:28.001113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0872` n `230`; crypto_major avg `0.0235` n `8`; equity avg `0.0234` n `112`; fx avg `-0.0019` n `6`; index avg `0.0031` n `25`; metal avg `0.0035` n `20`; unknown avg `0.1742` n `784`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `-0.0114` n `230`; crypto_major avg `-0.1439` n `8`; equity avg `-0.0328` n `112`; fx avg `0.0008` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.0862` n `784`
- 4h: commodity avg `0.0446` n `12`; crypto_alt avg `0.0235` n `230`; crypto_major avg `-0.2323` n `8`; equity avg `-0.0057` n `112`; fx avg `0.006` n `6`; index avg `0.0007` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.1299` n `784`
- 24h: commodity avg `0.2381` n `12`; crypto_alt avg `1.6928` n `230`; crypto_major avg `0.9047` n `8`; equity avg `0.4572` n `112`; fx avg `-0.007` n `6`; index avg `0.03` n `25`; metal avg `0.0263` n `20`; unknown avg `0.154` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
