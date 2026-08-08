# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T09:52:30.383222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.0235` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `-0.0004` n `112`; fx avg `0.0025` n `6`; index avg `0.0029` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0344` n `784`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.0524` n `230`; crypto_major avg `0.0476` n `8`; equity avg `0.0422` n `112`; fx avg `0.0108` n `6`; index avg `0.0014` n `25`; metal avg `0.033` n `20`; unknown avg `-0.0325` n `784`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `0.2574` n `230`; crypto_major avg `0.2527` n `8`; equity avg `0.0483` n `112`; fx avg `0.0054` n `6`; index avg `0.0108` n `25`; metal avg `0.0348` n `20`; unknown avg `0.1497` n `752`
- 24h: commodity avg `0.0054` n `12`; crypto_alt avg `0.0113` n `230`; crypto_major avg `0.0772` n `8`; equity avg `0.6981` n `112`; fx avg `-0.0123` n `6`; index avg `0.0398` n `25`; metal avg `-0.1704` n `20`; unknown avg `-0.0448` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
