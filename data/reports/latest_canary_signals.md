# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T12:52:31.119422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.2265` n `234`; crypto_major avg `0.1567` n `8`; equity avg `0.0078` n `140`; fx avg `0.0016` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.0272` n `943`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.0411` n `234`; crypto_major avg `-0.107` n `8`; equity avg `-0.0114` n `140`; fx avg `-0.0208` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.2636` n `935`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `0.1469` n `234`; crypto_major avg `0.3184` n `8`; equity avg `0.0298` n `140`; fx avg `-0.01` n `6`; index avg `0.0105` n `26`; metal avg `-0.0147` n `20`; unknown avg `0.1093` n `935`
- 24h: commodity avg `0.2771` n `12`; crypto_alt avg `-2.2649` n `234`; crypto_major avg `-2.3261` n `8`; equity avg `-0.2837` n `140`; fx avg `-0.0511` n `6`; index avg `-0.0576` n `26`; metal avg `-0.0369` n `20`; unknown avg `0.1352` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
