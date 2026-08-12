# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T06:22:28.266377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.0833` n `230`; crypto_major avg `-0.1012` n `8`; equity avg `-0.1287` n `113`; fx avg `0.0075` n `6`; index avg `-0.0212` n `25`; metal avg `0.0235` n `20`; unknown avg `-0.0072` n `786`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.2026` n `230`; crypto_major avg `-0.233` n `8`; equity avg `0.0292` n `113`; fx avg `0.0206` n `6`; index avg `0.024` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0383` n `770`
- 4h: commodity avg `0.0421` n `12`; crypto_alt avg `-0.2594` n `230`; crypto_major avg `-0.2217` n `8`; equity avg `0.156` n `113`; fx avg `-0.0009` n `6`; index avg `0.0413` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0356` n `770`
- 24h: commodity avg `0.1474` n `12`; crypto_alt avg `-1.0717` n `230`; crypto_major avg `0.5431` n `8`; equity avg `1.7397` n `113`; fx avg `0.0037` n `6`; index avg `0.1461` n `25`; metal avg `0.1128` n `20`; unknown avg `-0.1015` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2136`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
