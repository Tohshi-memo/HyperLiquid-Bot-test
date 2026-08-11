# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T06:52:30.503463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `-0.1579` n `230`; crypto_major avg `-0.1506` n `8`; equity avg `-0.0747` n `113`; fx avg `-0.0033` n `6`; index avg `-0.0119` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0434` n `785`
- 1h: commodity avg `0.2012` n `12`; crypto_alt avg `-0.2478` n `230`; crypto_major avg `-0.2601` n `8`; equity avg `-0.2505` n `113`; fx avg `0.0333` n `6`; index avg `-0.0395` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0383` n `753`
- 4h: commodity avg `0.2506` n `12`; crypto_alt avg `-0.4017` n `230`; crypto_major avg `-0.3217` n `8`; equity avg `-0.3477` n `113`; fx avg `0.024` n `6`; index avg `-0.0443` n `25`; metal avg `-0.2872` n `20`; unknown avg `-0.0083` n `753`
- 24h: commodity avg `1.2499` n `12`; crypto_alt avg `-1.1568` n `230`; crypto_major avg `-1.0448` n `8`; equity avg `-1.4011` n `113`; fx avg `0.0604` n `6`; index avg `-0.0405` n `25`; metal avg `0.0545` n `20`; unknown avg `0.1748` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
