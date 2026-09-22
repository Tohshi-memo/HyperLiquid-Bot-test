# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T17:37:36.946396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.041` n `12`; crypto_alt avg `-0.0475` n `234`; crypto_major avg `-0.0339` n `8`; equity avg `0.0067` n `140`; fx avg `-0.0079` n `6`; index avg `0.0065` n `26`; metal avg `0.0049` n `20`; unknown avg `0.9055` n `942`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.8563` n `234`; crypto_major avg `0.7288` n `8`; equity avg `0.2533` n `140`; fx avg `-0.0128` n `6`; index avg `0.0296` n `26`; metal avg `0.0686` n `20`; unknown avg `1.3255` n `908`
- 4h: commodity avg `0.3926` n `12`; crypto_alt avg `0.9759` n `234`; crypto_major avg `0.5321` n `8`; equity avg `0.3332` n `140`; fx avg `-0.0569` n `6`; index avg `0.0368` n `26`; metal avg `-0.0315` n `20`; unknown avg `1.4316` n `858`
- 24h: commodity avg `0.1764` n `12`; crypto_alt avg `2.2119` n `234`; crypto_major avg `1.2073` n `8`; equity avg `0.9195` n `140`; fx avg `-0.2774` n `6`; index avg `0.116` n `26`; metal avg `0.118` n `20`; unknown avg `0.2849` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
