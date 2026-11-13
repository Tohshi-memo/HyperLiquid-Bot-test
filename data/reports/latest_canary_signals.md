# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T09:52:25.414334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0472` n `13`; crypto_alt avg `-0.001` n `239`; crypto_major avg `-0.0263` n `8`; equity avg `-0.1458` n `162`; fx avg `-0.0045` n `6`; index avg `-0.0128` n `27`; metal avg `-0.0556` n `20`; unknown avg `3.4743` n `1262`
- 1h: commodity avg `-0.1001` n `13`; crypto_alt avg `-0.0684` n `239`; crypto_major avg `0.1934` n `8`; equity avg `0.3255` n `162`; fx avg `-0.0323` n `6`; index avg `0.0443` n `27`; metal avg `0.0156` n `20`; unknown avg `3.7495` n `1260`
- 4h: commodity avg `0.0464` n `13`; crypto_alt avg `1.3545` n `239`; crypto_major avg `1.0509` n `8`; equity avg `0.3044` n `162`; fx avg `0.0272` n `6`; index avg `0.0243` n `27`; metal avg `-0.0461` n `20`; unknown avg `0.5929` n `1166`
- 24h: commodity avg `0.7044` n `13`; crypto_alt avg `-1.0781` n `239`; crypto_major avg `-3.0173` n `8`; equity avg `-1.5591` n `162`; fx avg `-0.0276` n `6`; index avg `-0.0167` n `27`; metal avg `-0.4446` n `20`; unknown avg `103.1321` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
