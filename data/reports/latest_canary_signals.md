# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:49:35.086286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.0103` n `230`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0121` n `112`; fx avg `0.0016` n `6`; index avg `-0.0015` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0052` n `784`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.0079` n `8`; equity avg `0.0384` n `112`; fx avg `0.0074` n `6`; index avg `0.021` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.0002` n `784`
- 4h: commodity avg `0.0445` n `12`; crypto_alt avg `0.2585` n `230`; crypto_major avg `0.2815` n `8`; equity avg `0.1929` n `112`; fx avg `-0.0055` n `6`; index avg `0.0392` n `25`; metal avg `0.0032` n `20`; unknown avg `1.2413` n `784`
- 24h: commodity avg `0.2065` n `12`; crypto_alt avg `0.126` n `230`; crypto_major avg `0.1628` n `8`; equity avg `0.8164` n `112`; fx avg `-0.0377` n `6`; index avg `0.0459` n `25`; metal avg `0.0418` n `20`; unknown avg `1.076` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
