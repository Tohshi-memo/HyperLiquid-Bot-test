# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T09:22:32.151756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.037` n `12`; crypto_alt avg `-0.1013` n `230`; crypto_major avg `-0.0959` n `8`; equity avg `0.0713` n `92`; fx avg `-0.0017` n `6`; index avg `0.035` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.0389` n `766`
- 1h: commodity avg `-0.1526` n `12`; crypto_alt avg `0.0346` n `230`; crypto_major avg `0.0106` n `8`; equity avg `0.1457` n `92`; fx avg `-0.0335` n `6`; index avg `0.0288` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.0668` n `766`
- 4h: commodity avg `-0.4171` n `12`; crypto_alt avg `0.3673` n `230`; crypto_major avg `0.1568` n `8`; equity avg `0.4733` n `92`; fx avg `-0.0494` n `6`; index avg `0.1434` n `25`; metal avg `0.2677` n `20`; unknown avg `0.0061` n `750`
- 24h: commodity avg `-0.3859` n `12`; crypto_alt avg `-0.8518` n `230`; crypto_major avg `-0.6991` n `8`; equity avg `-1.9191` n `92`; fx avg `-0.0314` n `6`; index avg `-0.3962` n `25`; metal avg `-0.136` n `20`; unknown avg `0.0083` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
