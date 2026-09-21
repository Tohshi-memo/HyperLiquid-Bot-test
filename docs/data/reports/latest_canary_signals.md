# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T04:07:26.471802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1943` n `234`; crypto_major avg `-0.2389` n `8`; equity avg `-0.0888` n `140`; fx avg `0.017` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0463` n `20`; unknown avg `54.9272` n `936`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `0.5646` n `234`; crypto_major avg `-0.1411` n `8`; equity avg `-0.0463` n `140`; fx avg `0.0321` n `6`; index avg `0.0011` n `26`; metal avg `-0.024` n `20`; unknown avg `54.7474` n `936`
- 4h: commodity avg `-0.3057` n `12`; crypto_alt avg `0.5487` n `234`; crypto_major avg `-0.2181` n `8`; equity avg `0.0794` n `140`; fx avg `-0.0445` n `6`; index avg `0.0225` n `26`; metal avg `-0.0597` n `20`; unknown avg `53.6322` n `935`
- 24h: commodity avg `-0.6334` n `12`; crypto_alt avg `3.3229` n `234`; crypto_major avg `2.2454` n `8`; equity avg `1.0258` n `140`; fx avg `-0.0116` n `6`; index avg `0.1977` n `26`; metal avg `-0.0071` n `20`; unknown avg `4.7297` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
