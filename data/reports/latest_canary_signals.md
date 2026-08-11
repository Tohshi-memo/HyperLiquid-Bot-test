# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T16:22:25.637947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.2243` n `230`; crypto_major avg `0.175` n `8`; equity avg `0.0182` n `113`; fx avg `0.0012` n `6`; index avg `0.0044` n `25`; metal avg `0.0398` n `20`; unknown avg `0.1104` n `785`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `-0.4589` n `230`; crypto_major avg `-0.1243` n `8`; equity avg `-0.2737` n `113`; fx avg `0.0022` n `6`; index avg `-0.039` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.1133` n `785`
- 4h: commodity avg `0.0281` n `12`; crypto_alt avg `-1.2397` n `230`; crypto_major avg `-0.8082` n `8`; equity avg `0.07` n `113`; fx avg `0.0142` n `6`; index avg `-0.0581` n `25`; metal avg `-0.1241` n `20`; unknown avg `0.1446` n `785`
- 24h: commodity avg `0.1972` n `12`; crypto_alt avg `-1.8002` n `230`; crypto_major avg `-0.0607` n `8`; equity avg `0.0613` n `113`; fx avg `-0.0471` n `6`; index avg `0.0738` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.2432` n `753`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
