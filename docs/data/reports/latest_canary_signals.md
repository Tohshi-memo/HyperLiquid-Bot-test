# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T23:38:06.229079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.1654` n `234`; crypto_major avg `-0.4385` n `8`; equity avg `0.0064` n `140`; fx avg `-0.0096` n `6`; index avg `-0.0001` n `26`; metal avg `0.0232` n `20`; unknown avg `0.8639` n `944`
- 1h: commodity avg `0.0471` n `12`; crypto_alt avg `0.1142` n `234`; crypto_major avg `-0.5225` n `8`; equity avg `0.1558` n `140`; fx avg `-0.0097` n `6`; index avg `0.0069` n `26`; metal avg `0.0748` n `20`; unknown avg `0.8018` n `942`
- 4h: commodity avg `0.0577` n `12`; crypto_alt avg `0.6583` n `234`; crypto_major avg `0.5319` n `8`; equity avg `0.1595` n `140`; fx avg `-0.0288` n `6`; index avg `-0.0111` n `26`; metal avg `0.0669` n `20`; unknown avg `0.3769` n `852`
- 24h: commodity avg `-0.6677` n `12`; crypto_alt avg `3.856` n `234`; crypto_major avg `5.4583` n `8`; equity avg `2.6741` n `140`; fx avg `-0.1361` n `6`; index avg `0.5505` n `26`; metal avg `0.1095` n `20`; unknown avg `8.0697` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
