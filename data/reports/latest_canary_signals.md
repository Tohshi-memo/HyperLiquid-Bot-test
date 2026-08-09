# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T08:52:37.794366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1913` n `230`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0848` n `112`; fx avg `-0.0006` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.036` n `785`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0545` n `230`; crypto_major avg `-0.1548` n `8`; equity avg `-0.0354` n `112`; fx avg `-0.0005` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0273` n `785`
- 4h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.2994` n `230`; crypto_major avg `-0.0592` n `8`; equity avg `0.0163` n `112`; fx avg `-0.0204` n `6`; index avg `-0.0126` n `25`; metal avg `0.0202` n `20`; unknown avg `-0.0587` n `752`
- 24h: commodity avg `0.2619` n `12`; crypto_alt avg `1.168` n `230`; crypto_major avg `0.2683` n `8`; equity avg `0.5448` n `112`; fx avg `-0.0162` n `6`; index avg `0.0561` n `25`; metal avg `0.0384` n `20`; unknown avg `0.342` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
