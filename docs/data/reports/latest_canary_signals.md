# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T12:52:33.762673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0198` n `230`; crypto_major avg `0.0814` n `8`; equity avg `0.0313` n `112`; fx avg `0.0043` n `6`; index avg `0.01` n `25`; metal avg `0.0069` n `20`; unknown avg `0.0155` n `784`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `0.1691` n `230`; crypto_major avg `0.1028` n `8`; equity avg `0.0334` n `112`; fx avg `0.0032` n `6`; index avg `-0.002` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.0609` n `784`
- 4h: commodity avg `0.0647` n `12`; crypto_alt avg `0.3388` n `230`; crypto_major avg `0.3054` n `8`; equity avg `0.1631` n `112`; fx avg `0.0007` n `6`; index avg `0.0241` n `25`; metal avg `-0.004` n `20`; unknown avg `0.5543` n `784`
- 24h: commodity avg `0.1855` n `12`; crypto_alt avg `0.2672` n `230`; crypto_major avg `-0.0817` n `8`; equity avg `-0.3206` n `112`; fx avg `0.0398` n `6`; index avg `-0.139` n `25`; metal avg `-0.2022` n `20`; unknown avg `0.4633` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
