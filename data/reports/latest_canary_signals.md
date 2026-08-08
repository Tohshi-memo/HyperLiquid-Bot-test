# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:52:27.607587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0242` n `230`; crypto_major avg `0.0904` n `8`; equity avg `0.0276` n `112`; fx avg `0.0003` n `6`; index avg `0.0121` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.0005` n `784`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `0.2572` n `230`; crypto_major avg `0.0583` n `8`; equity avg `0.0391` n `112`; fx avg `0.0053` n `6`; index avg `-0.0029` n `25`; metal avg `0.0151` n `20`; unknown avg `0.0659` n `784`
- 4h: commodity avg `-0.0212` n `12`; crypto_alt avg `0.866` n `230`; crypto_major avg `0.5991` n `8`; equity avg `0.2048` n `112`; fx avg `-0.0096` n `6`; index avg `0.0315` n `25`; metal avg `0.0275` n `20`; unknown avg `-0.1756` n `784`
- 24h: commodity avg `-0.2501` n `12`; crypto_alt avg `1.4507` n `230`; crypto_major avg `1.2932` n `8`; equity avg `0.7569` n `112`; fx avg `0.0128` n `6`; index avg `0.0632` n `25`; metal avg `0.1841` n `20`; unknown avg `0.1381` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
