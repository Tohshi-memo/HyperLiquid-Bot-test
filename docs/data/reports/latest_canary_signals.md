# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T11:26:15.064601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.0022` n `230`; crypto_major avg `-0.1381` n `8`; equity avg `-0.0993` n `113`; fx avg `-0.0089` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.494` n `787`
- 1h: commodity avg `-0.0582` n `12`; crypto_alt avg `-0.0618` n `230`; crypto_major avg `-0.2627` n `8`; equity avg `-0.0635` n `113`; fx avg `-0.0134` n `6`; index avg `-0.0009` n `25`; metal avg `0.0112` n `20`; unknown avg `0.504` n `787`
- 4h: commodity avg `-0.3088` n `12`; crypto_alt avg `-0.0987` n `230`; crypto_major avg `-0.6457` n `8`; equity avg `-0.0361` n `113`; fx avg `-0.0059` n `6`; index avg `0.0039` n `25`; metal avg `0.098` n `20`; unknown avg `0.4733` n `787`
- 24h: commodity avg `-0.3452` n `12`; crypto_alt avg `-0.733` n `230`; crypto_major avg `-0.7422` n `8`; equity avg `1.3454` n `113`; fx avg `0.0358` n `6`; index avg `0.1618` n `25`; metal avg `-0.5327` n `20`; unknown avg `0.7031` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
