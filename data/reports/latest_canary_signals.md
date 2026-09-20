# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T14:22:26.369626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.376` n `234`; crypto_major avg `-0.2865` n `8`; equity avg `-0.0445` n `140`; fx avg `0.0016` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.7144` n `943`
- 1h: commodity avg `-0.0262` n `12`; crypto_alt avg `-0.1468` n `234`; crypto_major avg `-0.0462` n `8`; equity avg `-0.0351` n `140`; fx avg `0.0025` n `6`; index avg `-0.0085` n `26`; metal avg `0.0078` n `20`; unknown avg `1.6613` n `941`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.0252` n `234`; crypto_major avg `0.1267` n `8`; equity avg `0.0195` n `140`; fx avg `-0.0115` n `6`; index avg `0.0039` n `26`; metal avg `-0.0064` n `20`; unknown avg `2.1211` n `935`
- 24h: commodity avg `0.2505` n `12`; crypto_alt avg `-2.7562` n `234`; crypto_major avg `-2.759` n `8`; equity avg `-0.3195` n `140`; fx avg `-0.0561` n `6`; index avg `-0.0536` n `26`; metal avg `-0.0287` n `20`; unknown avg `2.1071` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
