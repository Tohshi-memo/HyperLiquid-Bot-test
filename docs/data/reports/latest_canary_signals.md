# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T09:07:29.744032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0396` n `230`; crypto_major avg `0.0847` n `8`; equity avg `0.0328` n `112`; fx avg `0.0007` n `6`; index avg `-0.0059` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0171` n `785`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.2074` n `230`; crypto_major avg `-0.2167` n `8`; equity avg `-0.0045` n `112`; fx avg `-0.002` n `6`; index avg `-0.0226` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.0147` n `785`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.2481` n `230`; crypto_major avg `0.0196` n `8`; equity avg `0.052` n `112`; fx avg `-0.0208` n `6`; index avg `-0.0273` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.0636` n `752`
- 24h: commodity avg `0.2634` n `12`; crypto_alt avg `1.185` n `230`; crypto_major avg `0.3131` n `8`; equity avg `0.5759` n `112`; fx avg `-0.0204` n `6`; index avg `0.0418` n `25`; metal avg `0.0323` n `20`; unknown avg `0.3191` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
