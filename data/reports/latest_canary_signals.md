# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T05:52:28.736810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0711` n `12`; crypto_alt avg `0.0013` n `230`; crypto_major avg `0.0048` n `8`; equity avg `0.0605` n `100`; fx avg `0.0025` n `6`; index avg `-0.0092` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.083` n `775`
- 1h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.0636` n `230`; crypto_major avg `0.0965` n `8`; equity avg `0.1709` n `100`; fx avg `0.0047` n `6`; index avg `0.0484` n `25`; metal avg `0.0149` n `20`; unknown avg `0.064` n `775`
- 4h: commodity avg `-0.1699` n `12`; crypto_alt avg `0.0493` n `230`; crypto_major avg `0.3258` n `8`; equity avg `0.812` n `100`; fx avg `-0.0019` n `6`; index avg `0.1366` n `25`; metal avg `-0.1314` n `20`; unknown avg `-0.4297` n `775`
- 24h: commodity avg `-0.5735` n `12`; crypto_alt avg `0.9566` n `230`; crypto_major avg `1.289` n `8`; equity avg `1.1172` n `100`; fx avg `0.0821` n `6`; index avg `0.158` n `25`; metal avg `0.333` n `20`; unknown avg `-0.024` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
