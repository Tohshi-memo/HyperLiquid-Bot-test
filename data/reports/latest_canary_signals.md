# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T01:52:31.356963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0624` n `12`; crypto_alt avg `0.3122` n `234`; crypto_major avg `0.0977` n `8`; equity avg `0.043` n `140`; fx avg `0.0026` n `6`; index avg `-0.0002` n `26`; metal avg `0.0076` n `20`; unknown avg `-0.0457` n `943`
- 1h: commodity avg `0.0974` n `12`; crypto_alt avg `-0.4253` n `234`; crypto_major avg `-0.4282` n `8`; equity avg `0.0156` n `140`; fx avg `-0.0048` n `6`; index avg `0.0079` n `26`; metal avg `0.0182` n `20`; unknown avg `0.1029` n `941`
- 4h: commodity avg `0.2113` n `12`; crypto_alt avg `0.6056` n `234`; crypto_major avg `-0.1928` n `8`; equity avg `0.044` n `140`; fx avg `-0.0046` n `6`; index avg `-0.0222` n `26`; metal avg `0.0166` n `20`; unknown avg `0.3217` n `911`
- 24h: commodity avg `0.0959` n `12`; crypto_alt avg `0.9187` n `234`; crypto_major avg `-0.9279` n `8`; equity avg `0.1227` n `140`; fx avg `-0.06` n `6`; index avg `0.0125` n `26`; metal avg `0.0262` n `20`; unknown avg `0.4767` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
