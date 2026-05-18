# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T21:07:16.700298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2083` n `12`; crypto_alt avg `0.0933` n `228`; crypto_major avg `0.1217` n `8`; equity avg `-0.0361` n `66`; fx avg `0.0088` n `6`; index avg `0.0084` n `23`; metal avg `0.039` n `18`; unknown avg `0.0519` n `383`
- 1h: commodity avg `0.3117` n `12`; crypto_alt avg `-0.2675` n `228`; crypto_major avg `-0.3074` n `8`; equity avg `0.003` n `66`; fx avg `0.0039` n `6`; index avg `0.001` n `23`; metal avg `0.1476` n `18`; unknown avg `-0.0534` n `383`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `0.4546` n `228`; crypto_major avg `0.4013` n `8`; equity avg `0.0748` n `66`; fx avg `-0.0481` n `6`; index avg `0.052` n `23`; metal avg `0.2434` n `18`; unknown avg `0.3067` n `383`
- 24h: commodity avg `1.0611` n `12`; crypto_alt avg `-2.0065` n `228`; crypto_major avg `-2.2853` n `8`; equity avg `-0.9683` n `66`; fx avg `0.1996` n `6`; index avg `-0.3996` n `23`; metal avg `1.1319` n `18`; unknown avg `-0.0451` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
