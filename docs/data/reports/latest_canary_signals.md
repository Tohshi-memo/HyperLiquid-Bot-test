# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T00:07:26.562772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.0148` n `8`; equity avg `-0.014` n `112`; fx avg `-0.0019` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0092` n `20`; unknown avg `0.1249` n `784`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.1383` n `230`; crypto_major avg `0.0859` n `8`; equity avg `-0.0366` n `112`; fx avg `-0.0018` n `6`; index avg `0.0066` n `25`; metal avg `0.0134` n `20`; unknown avg `0.0268` n `784`
- 4h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0318` n `230`; crypto_major avg `-0.2533` n `8`; equity avg `-0.0031` n `112`; fx avg `0.0036` n `6`; index avg `0.0081` n `25`; metal avg `0.023` n `20`; unknown avg `-0.139` n `784`
- 24h: commodity avg `0.1754` n `12`; crypto_alt avg `1.8648` n `230`; crypto_major avg `1.1702` n `8`; equity avg `0.4602` n `112`; fx avg `-0.0052` n `6`; index avg `0.0344` n `25`; metal avg `-0.004` n `20`; unknown avg `0.212` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
