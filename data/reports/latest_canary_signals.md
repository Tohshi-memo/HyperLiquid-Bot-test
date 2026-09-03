# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T07:22:34.946000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `-0.1238` n `232`; crypto_major avg `-0.107` n `8`; equity avg `0.0457` n `133`; fx avg `0.0169` n `6`; index avg `-0.0083` n `26`; metal avg `0.0159` n `20`; unknown avg `0.4565` n `792`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.2116` n `232`; crypto_major avg `0.2474` n `8`; equity avg `0.1001` n `133`; fx avg `-0.0752` n `6`; index avg `-0.0267` n `26`; metal avg `0.0249` n `20`; unknown avg `0.0134` n `788`
- 4h: commodity avg `-0.1657` n `12`; crypto_alt avg `0.5373` n `232`; crypto_major avg `0.2719` n `8`; equity avg `-0.2662` n `133`; fx avg `-0.1172` n `6`; index avg `-0.1186` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.0174` n `754`
- 24h: commodity avg `0.1117` n `12`; crypto_alt avg `0.6896` n `232`; crypto_major avg `0.6639` n `8`; equity avg `1.1109` n `133`; fx avg `-0.41` n `6`; index avg `0.0556` n `26`; metal avg `0.6994` n `20`; unknown avg `-0.3776` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
