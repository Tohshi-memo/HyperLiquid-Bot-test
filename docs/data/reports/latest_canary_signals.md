# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T21:37:32.642376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.3168` n `232`; crypto_major avg `0.3239` n `8`; equity avg `0.0394` n `129`; fx avg `0.0065` n `6`; index avg `-0.0112` n `26`; metal avg `0.0197` n `20`; unknown avg `1.5771` n `793`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `0.3208` n `232`; crypto_major avg `0.3295` n `8`; equity avg `0.0258` n `129`; fx avg `0.0067` n `6`; index avg `0.0083` n `26`; metal avg `0.0112` n `20`; unknown avg `0.1269` n `785`
- 4h: commodity avg `0.1003` n `12`; crypto_alt avg `0.4705` n `232`; crypto_major avg `0.4823` n `8`; equity avg `0.4655` n `129`; fx avg `0.0159` n `6`; index avg `0.0825` n `26`; metal avg `0.0945` n `20`; unknown avg `0.5958` n `773`
- 24h: commodity avg `0.1636` n `12`; crypto_alt avg `-0.1877` n `231`; crypto_major avg `0.0876` n `8`; equity avg `0.1224` n `129`; fx avg `-0.0894` n `6`; index avg `-0.1342` n `26`; metal avg `-0.3768` n `20`; unknown avg `0.0757` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
