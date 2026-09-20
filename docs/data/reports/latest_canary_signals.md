# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T13:08:02.852566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.0835` n `234`; crypto_major avg `0.1073` n `8`; equity avg `0.0284` n `140`; fx avg `-0.0002` n `6`; index avg `0.0075` n `26`; metal avg `0.0024` n `20`; unknown avg `0.1338` n `941`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `-0.0828` n `234`; crypto_major avg `-0.0597` n `8`; equity avg `0.0143` n `140`; fx avg `-0.0186` n `6`; index avg `0.0003` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.2895` n `941`
- 4h: commodity avg `0.0571` n `12`; crypto_alt avg `0.1054` n `234`; crypto_major avg `0.3237` n `8`; equity avg `0.0457` n `140`; fx avg `-0.01` n `6`; index avg `0.0168` n `26`; metal avg `-0.0251` n `20`; unknown avg `0.8977` n `935`
- 24h: commodity avg `0.2828` n `12`; crypto_alt avg `-2.0128` n `234`; crypto_major avg `-2.1995` n `8`; equity avg `-0.24` n `140`; fx avg `-0.0494` n `6`; index avg `-0.0471` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.2823` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
