# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T04:52:25.093932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `-0.0499` n `230`; crypto_major avg `-0.0202` n `8`; equity avg `0.0521` n `113`; fx avg `-0.0091` n `6`; index avg `0.02` n `25`; metal avg `0.015` n `20`; unknown avg `0.0506` n `787`
- 1h: commodity avg `0.0724` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `0.067` n `8`; equity avg `-0.0146` n `113`; fx avg `-0.0152` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0517` n `20`; unknown avg `0.4892` n `787`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `0.1208` n `230`; crypto_major avg `0.3946` n `8`; equity avg `0.2298` n `113`; fx avg `0.0307` n `6`; index avg `0.0381` n `25`; metal avg `-0.2695` n `20`; unknown avg `0.5219` n `786`
- 24h: commodity avg `-0.1062` n `12`; crypto_alt avg `-1.1088` n `230`; crypto_major avg `-0.0296` n `8`; equity avg `2.455` n `113`; fx avg `-0.0535` n `6`; index avg `0.3214` n `25`; metal avg `-0.1608` n `20`; unknown avg `0.0713` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2418`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
