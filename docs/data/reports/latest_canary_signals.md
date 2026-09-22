# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T13:07:30.284049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0698` n `12`; crypto_alt avg `0.6352` n `234`; crypto_major avg `0.3633` n `8`; equity avg `0.0729` n `140`; fx avg `0.0006` n `6`; index avg `0.0168` n `26`; metal avg `0.0566` n `20`; unknown avg `0.0462` n `942`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `1.4278` n `234`; crypto_major avg `0.6533` n `8`; equity avg `0.0776` n `140`; fx avg `0.034` n `6`; index avg `0.0115` n `26`; metal avg `0.1715` n `20`; unknown avg `-0.1257` n `942`
- 4h: commodity avg `-0.1935` n `12`; crypto_alt avg `1.0459` n `234`; crypto_major avg `0.8085` n `8`; equity avg `0.2667` n `140`; fx avg `0.0252` n `6`; index avg `0.0572` n `26`; metal avg `0.2667` n `20`; unknown avg `2.4476` n `934`
- 24h: commodity avg `-0.4595` n `12`; crypto_alt avg `0.8876` n `234`; crypto_major avg `1.5581` n `8`; equity avg `0.8211` n `140`; fx avg `-0.2419` n `6`; index avg `0.2521` n `26`; metal avg `-0.1414` n `20`; unknown avg `1108.3473` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
