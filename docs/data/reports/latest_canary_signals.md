# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T22:22:27.058609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0314` n `230`; crypto_major avg `0.0604` n `8`; equity avg `-0.0374` n `113`; fx avg `0.0012` n `6`; index avg `-0.0113` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0336` n `786`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `-0.7953` n `230`; crypto_major avg `-0.348` n `8`; equity avg `-0.1134` n `113`; fx avg `0.0039` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0447` n `20`; unknown avg `-0.1293` n `786`
- 4h: commodity avg `-0.1007` n `12`; crypto_alt avg `-1.0823` n `230`; crypto_major avg `-0.4574` n `8`; equity avg `-0.437` n `113`; fx avg `-0.0235` n `6`; index avg `-0.0063` n `25`; metal avg `-0.1034` n `20`; unknown avg `-0.2608` n `786`
- 24h: commodity avg `-0.049` n `12`; crypto_alt avg `-1.7499` n `230`; crypto_major avg `-0.6569` n `8`; equity avg `2.7907` n `113`; fx avg `0.0126` n `6`; index avg `0.3952` n `25`; metal avg `0.0741` n `20`; unknown avg `-0.0986` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
