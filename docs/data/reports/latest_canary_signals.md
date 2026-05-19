# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T10:52:14.646456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1578` n `12`; crypto_alt avg `-0.2711` n `228`; crypto_major avg `-0.2442` n `8`; equity avg `-0.1309` n `66`; fx avg `0.0027` n `6`; index avg `-0.0401` n `23`; metal avg `-0.1751` n `18`; unknown avg `-0.1442` n `383`
- 1h: commodity avg `0.0987` n `12`; crypto_alt avg `-0.2421` n `228`; crypto_major avg `0.0773` n `8`; equity avg `0.0101` n `66`; fx avg `-0.009` n `6`; index avg `0.0197` n `23`; metal avg `-0.0611` n `18`; unknown avg `-0.2914` n `383`
- 4h: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.946` n `228`; crypto_major avg `-0.3798` n `8`; equity avg `-0.5711` n `66`; fx avg `-0.0192` n `6`; index avg `-0.4207` n `23`; metal avg `-0.376` n `18`; unknown avg `-0.5352` n `383`
- 24h: commodity avg `0.5908` n `12`; crypto_alt avg `1.178` n `228`; crypto_major avg `0.6906` n `8`; equity avg `-1.6312` n `66`; fx avg `0.2368` n `6`; index avg `-0.8376` n `23`; metal avg `-0.2404` n `18`; unknown avg `0.5585` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
