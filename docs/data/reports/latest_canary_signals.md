# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T05:22:31.029152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1068` n `234`; crypto_major avg `-0.0034` n `8`; equity avg `0.0362` n `140`; fx avg `-0.0039` n `6`; index avg `0.0108` n `26`; metal avg `0.021` n `20`; unknown avg `0.2252` n `919`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.0924` n `234`; crypto_major avg `0.2722` n `8`; equity avg `0.1597` n `140`; fx avg `0.0118` n `6`; index avg `0.0367` n `26`; metal avg `0.1089` n `20`; unknown avg `-0.1082` n `911`
- 4h: commodity avg `-0.0449` n `12`; crypto_alt avg `1.9867` n `234`; crypto_major avg `1.5896` n `8`; equity avg `0.84` n `140`; fx avg `0.1425` n `6`; index avg `0.1376` n `26`; metal avg `0.1341` n `20`; unknown avg `9.5294` n `897`
- 24h: commodity avg `-0.3289` n `12`; crypto_alt avg `5.0694` n `234`; crypto_major avg `3.6633` n `8`; equity avg `2.1326` n `140`; fx avg `0.1731` n `6`; index avg `0.3444` n `26`; metal avg `0.6084` n `20`; unknown avg `2.2908` n `753`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
