# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T01:37:30.649865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.5992` n `234`; crypto_major avg `0.5821` n `8`; equity avg `0.1485` n `137`; fx avg `-0.0128` n `6`; index avg `0.0104` n `27`; metal avg `0.0824` n `20`; unknown avg `0.4249` n `919`
- 1h: commodity avg `0.1616` n `12`; crypto_alt avg `0.6008` n `234`; crypto_major avg `0.6206` n `8`; equity avg `0.1626` n `137`; fx avg `0.0144` n `6`; index avg `0.0343` n `27`; metal avg `0.2589` n `20`; unknown avg `0.1942` n `917`
- 4h: commodity avg `0.0358` n `12`; crypto_alt avg `1.7491` n `234`; crypto_major avg `1.0694` n `8`; equity avg `0.809` n `137`; fx avg `0.0116` n `6`; index avg `0.1809` n `27`; metal avg `0.3906` n `20`; unknown avg `1.3134` n `813`
- 24h: commodity avg `-0.5075` n `12`; crypto_alt avg `2.5901` n `234`; crypto_major avg `1.9926` n `8`; equity avg `1.8965` n `137`; fx avg `-0.0525` n `6`; index avg `0.2039` n `27`; metal avg `0.1293` n `20`; unknown avg `0.5206` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
