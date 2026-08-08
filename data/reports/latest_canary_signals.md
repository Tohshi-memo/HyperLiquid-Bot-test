# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:22:30.124135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `0.0075` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `0.0366` n `112`; fx avg `0.0045` n `6`; index avg `0.0183` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0006` n `784`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.0012` n `230`; crypto_major avg `0.0414` n `8`; equity avg `0.0791` n `112`; fx avg `-0.0103` n `6`; index avg `0.0154` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0598` n `784`
- 4h: commodity avg `0.0467` n `12`; crypto_alt avg `0.2003` n `230`; crypto_major avg `0.2487` n `8`; equity avg `0.22` n `112`; fx avg `-0.0059` n `6`; index avg `0.0238` n `25`; metal avg `0.0211` n `20`; unknown avg `1.2914` n `784`
- 24h: commodity avg `0.1827` n `12`; crypto_alt avg `-0.0552` n `230`; crypto_major avg `0.0471` n `8`; equity avg `0.7349` n `112`; fx avg `-0.0368` n `6`; index avg `0.0464` n `25`; metal avg `0.003` n `20`; unknown avg `1.0619` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
