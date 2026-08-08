# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T10:47:57.753005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0479` n `230`; crypto_major avg `0.0333` n `8`; equity avg `-0.0269` n `112`; fx avg `-0.0191` n `6`; index avg `0.0115` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0573` n `784`
- 1h: commodity avg `0.0524` n `12`; crypto_alt avg `0.0968` n `230`; crypto_major avg `0.1287` n `8`; equity avg `0.035` n `112`; fx avg `-0.0306` n `6`; index avg `0.003` n `25`; metal avg `-0.0071` n `20`; unknown avg `1.1628` n `784`
- 4h: commodity avg `0.0761` n `12`; crypto_alt avg `0.2515` n `230`; crypto_major avg `0.2173` n `8`; equity avg `0.186` n `112`; fx avg `-0.0284` n `6`; index avg `0.0189` n `25`; metal avg `0.0416` n `20`; unknown avg `1.2671` n `784`
- 24h: commodity avg `0.1875` n `12`; crypto_alt avg `0.2193` n `230`; crypto_major avg `0.1951` n `8`; equity avg `0.8888` n `112`; fx avg `-0.0394` n `6`; index avg `0.0522` n `25`; metal avg `-0.0479` n `20`; unknown avg `1.0976` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
