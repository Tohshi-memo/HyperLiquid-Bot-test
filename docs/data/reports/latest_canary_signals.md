# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:07:23.871796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1165` n `230`; crypto_major avg `0.1081` n `8`; equity avg `-0.0199` n `112`; fx avg `0.0021` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0128` n `20`; unknown avg `0.0193` n `784`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.3228` n `230`; crypto_major avg `0.0978` n `8`; equity avg `0.0291` n `112`; fx avg `-0.0041` n `6`; index avg `0.0187` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0063` n `784`
- 4h: commodity avg `-0.0502` n `12`; crypto_alt avg `0.8059` n `230`; crypto_major avg `0.7797` n `8`; equity avg `0.1825` n `112`; fx avg `-0.0033` n `6`; index avg `0.0538` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.2048` n `784`
- 24h: commodity avg `-0.2578` n `12`; crypto_alt avg `1.1053` n `230`; crypto_major avg `1.0007` n `8`; equity avg `0.2797` n `112`; fx avg `0.0028` n `6`; index avg `0.0352` n `25`; metal avg `0.0438` n `20`; unknown avg `-0.0747` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
