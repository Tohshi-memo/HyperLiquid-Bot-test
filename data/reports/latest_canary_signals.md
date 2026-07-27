# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T09:37:29.438319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.2285` n `230`; crypto_major avg `0.2494` n `8`; equity avg `0.0689` n `100`; fx avg `-0.0052` n `6`; index avg `0.0178` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0101` n `775`
- 1h: commodity avg `-0.116` n `12`; crypto_alt avg `-0.031` n `230`; crypto_major avg `0.0444` n `8`; equity avg `0.0614` n `100`; fx avg `-0.0238` n `6`; index avg `0.0133` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0821` n `775`
- 4h: commodity avg `-0.5662` n `12`; crypto_alt avg `-0.3612` n `230`; crypto_major avg `0.0183` n `8`; equity avg `0.4804` n `100`; fx avg `-0.014` n `6`; index avg `0.0538` n `25`; metal avg `0.1532` n `20`; unknown avg `-0.0994` n `759`
- 24h: commodity avg `-0.9697` n `12`; crypto_alt avg `0.5562` n `230`; crypto_major avg `1.321` n `8`; equity avg `1.486` n `100`; fx avg `0.1037` n `6`; index avg `0.2046` n `25`; metal avg `0.4229` n `20`; unknown avg `-0.0621` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
