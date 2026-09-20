# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T13:37:26.731420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0617` n `12`; crypto_alt avg `-0.1874` n `234`; crypto_major avg `-0.1499` n `8`; equity avg `-0.0207` n `140`; fx avg `0.0009` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0009` n `20`; unknown avg `1.1745` n `943`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.1628` n `234`; crypto_major avg `-0.0386` n `8`; equity avg `0.0087` n `140`; fx avg `-0.0029` n `6`; index avg `0.0094` n `26`; metal avg `-0.0038` n `20`; unknown avg `1.3282` n `941`
- 4h: commodity avg `0.0133` n `12`; crypto_alt avg `-0.7394` n `234`; crypto_major avg `-0.3364` n `8`; equity avg `-0.0161` n `140`; fx avg `-0.0134` n `6`; index avg `0.0217` n `26`; metal avg `-0.0383` n `20`; unknown avg `0.7241` n `935`
- 24h: commodity avg `0.2216` n `12`; crypto_alt avg `-2.4155` n `234`; crypto_major avg `-2.4759` n `8`; equity avg `-0.29` n `140`; fx avg `-0.0546` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0342` n `20`; unknown avg `1.489` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
