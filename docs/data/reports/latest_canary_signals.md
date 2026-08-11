# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T13:36:35.073732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.1303` n `8`; equity avg `-0.0379` n `113`; fx avg `0.0001` n `6`; index avg `-0.0187` n `25`; metal avg `-0.0391` n `20`; unknown avg `0.0416` n `785`
- 1h: commodity avg `-0.1008` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `-0.1977` n `8`; equity avg `0.0182` n `113`; fx avg `-0.0016` n `6`; index avg `-0.0298` n `25`; metal avg `0.0101` n `20`; unknown avg `0.0719` n `785`
- 4h: commodity avg `-0.3956` n `12`; crypto_alt avg `-0.2169` n `230`; crypto_major avg `0.0486` n `8`; equity avg `0.5862` n `113`; fx avg `-0.0471` n `6`; index avg `0.0646` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.1816` n `785`
- 24h: commodity avg `0.3328` n `12`; crypto_alt avg `-1.4091` n `230`; crypto_major avg `-0.2877` n `8`; equity avg `-0.0137` n `113`; fx avg `-0.043` n `6`; index avg `0.1449` n `25`; metal avg `0.3297` n `20`; unknown avg `0.0526` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
