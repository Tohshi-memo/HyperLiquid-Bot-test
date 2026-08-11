# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T15:07:39.086022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.1958` n `230`; crypto_major avg `-0.003` n `8`; equity avg `-0.2739` n `113`; fx avg `-0.0021` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.027` n `785`
- 1h: commodity avg `0.0664` n `12`; crypto_alt avg `-0.7308` n `230`; crypto_major avg `-0.5403` n `8`; equity avg `-0.2155` n `113`; fx avg `0.002` n `6`; index avg `-0.0186` n `25`; metal avg `0.0422` n `20`; unknown avg `0.026` n `785`
- 4h: commodity avg `0.1426` n `12`; crypto_alt avg `-0.9804` n `230`; crypto_major avg `-0.709` n `8`; equity avg `0.1298` n `113`; fx avg `0.0118` n `6`; index avg `-0.0274` n `25`; metal avg `-0.1568` n `20`; unknown avg `-0.0698` n `785`
- 24h: commodity avg `0.198` n `12`; crypto_alt avg `-1.737` n `230`; crypto_major avg `-0.5718` n `8`; equity avg `0.1411` n `113`; fx avg `-0.0672` n `6`; index avg `0.1196` n `25`; metal avg `0.1785` n `20`; unknown avg `-0.2589` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
