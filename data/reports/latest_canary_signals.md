# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T03:52:27.252120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.0215` n `112`; fx avg `-0.0052` n `6`; index avg `0.0031` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.5337` n `784`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.1048` n `230`; crypto_major avg `0.0199` n `8`; equity avg `-0.0423` n `112`; fx avg `0.0007` n `6`; index avg `0.0004` n `25`; metal avg `0.005` n `20`; unknown avg `0.2945` n `784`
- 4h: commodity avg `0.0637` n `12`; crypto_alt avg `0.0804` n `230`; crypto_major avg `-0.2311` n `8`; equity avg `-0.0414` n `112`; fx avg `0.0036` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.0072` n `784`
- 24h: commodity avg `0.2162` n `12`; crypto_alt avg `1.4649` n `230`; crypto_major avg `0.4087` n `8`; equity avg `0.537` n `112`; fx avg `-0.007` n `6`; index avg `0.0349` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.0042` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
