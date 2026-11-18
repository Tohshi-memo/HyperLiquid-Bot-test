# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T03:37:25.009556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0545` n `13`; crypto_alt avg `0.3501` n `239`; crypto_major avg `0.3586` n `8`; equity avg `0.3116` n `163`; fx avg `0.0001` n `6`; index avg `0.0451` n `27`; metal avg `0.1313` n `20`; unknown avg `2.614` n `1266`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.2943` n `239`; crypto_major avg `0.2241` n `8`; equity avg `0.1607` n `163`; fx avg `0.0196` n `6`; index avg `0.0307` n `27`; metal avg `-0.0359` n `20`; unknown avg `2.1964` n `1264`
- 4h: commodity avg `-0.2665` n `13`; crypto_alt avg `-0.7954` n `239`; crypto_major avg `-0.7249` n `8`; equity avg `-1.5935` n `163`; fx avg `-0.0775` n `6`; index avg `-0.1917` n `27`; metal avg `-0.5451` n `20`; unknown avg `5.9837` n `1257`
- 24h: commodity avg `0.1982` n `13`; crypto_alt avg `-0.2471` n `239`; crypto_major avg `0.0555` n `8`; equity avg `-0.9402` n `163`; fx avg `-0.096` n `6`; index avg `-0.1258` n `27`; metal avg `-0.7537` n `20`; unknown avg `239.9828` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
