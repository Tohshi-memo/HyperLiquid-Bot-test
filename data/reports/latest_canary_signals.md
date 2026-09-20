# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T08:37:32.760151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.0764` n `234`; crypto_major avg `-0.0237` n `8`; equity avg `-0.02` n `140`; fx avg `0.0059` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.8499` n `943`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.1059` n `234`; crypto_major avg `-0.1002` n `8`; equity avg `-0.024` n `140`; fx avg `-0.007` n `6`; index avg `-0.0049` n `26`; metal avg `0.007` n `20`; unknown avg `0.621` n `935`
- 4h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.7245` n `234`; crypto_major avg `-0.2617` n `8`; equity avg `-0.0413` n `140`; fx avg `0.0042` n `6`; index avg `-0.0243` n `26`; metal avg `0.0274` n `20`; unknown avg `8.7611` n `905`
- 24h: commodity avg `0.2373` n `12`; crypto_alt avg `-1.0839` n `234`; crypto_major avg `-2.119` n `8`; equity avg `-0.255` n `140`; fx avg `-0.0357` n `6`; index avg `-0.0774` n `26`; metal avg `0.006` n `20`; unknown avg `1.0914` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
