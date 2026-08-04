# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T22:37:26.527846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `0.066` n `8`; equity avg `0.0443` n `108`; fx avg `0.006` n `6`; index avg `0.0015` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0657` n `781`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.026` n `8`; equity avg `0.1746` n `108`; fx avg `-0.0038` n `6`; index avg `0.0067` n `25`; metal avg `0.0449` n `20`; unknown avg `0.0161` n `781`
- 4h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.1071` n `230`; crypto_major avg `-0.1276` n `8`; equity avg `-0.3654` n `108`; fx avg `0.0292` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0101` n `20`; unknown avg `0.0303` n `781`
- 24h: commodity avg `-1.2437` n `12`; crypto_alt avg `0.2052` n `230`; crypto_major avg `0.8377` n `8`; equity avg `3.0669` n `107`; fx avg `0.1129` n `6`; index avg `0.7112` n `25`; metal avg `0.9404` n `20`; unknown avg `0.4484` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
