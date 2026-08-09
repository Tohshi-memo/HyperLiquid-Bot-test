# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T00:52:23.500953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0258` n `230`; crypto_major avg `-0.0289` n `8`; equity avg `0.0156` n `112`; fx avg `-0.0076` n `6`; index avg `-0.0002` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.1384` n `784`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.01` n `8`; equity avg `0.0413` n `112`; fx avg `-0.0049` n `6`; index avg `-0.003` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.1768` n `784`
- 4h: commodity avg `-0.033` n `12`; crypto_alt avg `-0.0099` n `230`; crypto_major avg `-0.2484` n `8`; equity avg `0.0492` n `112`; fx avg `-0.0023` n `6`; index avg `0.0065` n `25`; metal avg `0.0261` n `20`; unknown avg `-0.0964` n `784`
- 24h: commodity avg `0.1469` n `12`; crypto_alt avg `1.8992` n `230`; crypto_major avg `1.2021` n `8`; equity avg `0.5603` n `112`; fx avg `-0.011` n `6`; index avg `0.0605` n `25`; metal avg `0.0046` n `20`; unknown avg `0.2267` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
