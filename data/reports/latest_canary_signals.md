# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T22:54:45.511365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `-0.1909` n `235`; crypto_major avg `-0.0299` n `8`; equity avg `-0.0007` n `150`; fx avg `-0.0034` n `6`; index avg `0.0001` n `26`; metal avg `-0.0018` n `20`; unknown avg `4.5584` n `1117`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `-0.2302` n `235`; crypto_major avg `-0.0578` n `8`; equity avg `0.0027` n `150`; fx avg `-0.0006` n `6`; index avg `0.0041` n `26`; metal avg `0.0024` n `20`; unknown avg `3.7975` n `1107`
- 4h: commodity avg `0.1979` n `13`; crypto_alt avg `0.1437` n `235`; crypto_major avg `-0.0117` n `8`; equity avg `0.0621` n `150`; fx avg `-0.0029` n `6`; index avg `0.011` n `26`; metal avg `0.0168` n `20`; unknown avg `3.3044` n `1023`
- 24h: commodity avg `0.0735` n `13`; crypto_alt avg `2.2468` n `235`; crypto_major avg `0.7387` n `8`; equity avg `0.1926` n `150`; fx avg `-0.0067` n `6`; index avg `0.0218` n `26`; metal avg `0.0102` n `20`; unknown avg `0.08` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
