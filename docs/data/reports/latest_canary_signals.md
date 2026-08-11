# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T12:37:24.469773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.11` n `230`; crypto_major avg `-0.1059` n `8`; equity avg `0.0167` n `113`; fx avg `0.0115` n `6`; index avg `0.0076` n `25`; metal avg `-0.0773` n `20`; unknown avg `-0.014` n `785`
- 1h: commodity avg `0.1161` n `12`; crypto_alt avg `-0.1462` n `230`; crypto_major avg `-0.0378` n `8`; equity avg `0.044` n `113`; fx avg `0.0117` n `6`; index avg `0.0303` n `25`; metal avg `-0.1014` n `20`; unknown avg `-0.0772` n `785`
- 4h: commodity avg `-0.3334` n `12`; crypto_alt avg `-0.0955` n `230`; crypto_major avg `0.4471` n `8`; equity avg `0.7082` n `113`; fx avg `-0.0506` n `6`; index avg `0.1402` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.1395` n `785`
- 24h: commodity avg `0.5492` n `12`; crypto_alt avg `-1.3685` n `230`; crypto_major avg `-0.3962` n `8`; equity avg `-0.2585` n `113`; fx avg `-0.0072` n `6`; index avg `0.1732` n `25`; metal avg `0.3075` n `20`; unknown avg `0.0009` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
