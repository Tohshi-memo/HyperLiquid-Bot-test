# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T02:52:30.488979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.1659` n `234`; crypto_major avg `0.07` n `8`; equity avg `0.073` n `140`; fx avg `0.0146` n `6`; index avg `0.0014` n `26`; metal avg `-0.009` n `20`; unknown avg `0.215` n `945`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.6403` n `234`; crypto_major avg `0.4329` n `8`; equity avg `-0.0429` n `140`; fx avg `0.0462` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0865` n `20`; unknown avg `0.2029` n `943`
- 4h: commodity avg `0.021` n `12`; crypto_alt avg `0.4393` n `234`; crypto_major avg `0.4159` n `8`; equity avg `-0.3157` n `140`; fx avg `-0.051` n `6`; index avg `-0.1048` n `26`; metal avg `-0.2754` n `20`; unknown avg `0.3251` n `937`
- 24h: commodity avg `-0.0228` n `12`; crypto_alt avg `3.3033` n `234`; crypto_major avg `1.8974` n `8`; equity avg `0.2378` n `140`; fx avg `-0.1858` n `6`; index avg `-0.009` n `26`; metal avg `0.0427` n `20`; unknown avg `2.3067` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
