# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T01:37:30.608168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0178` n `230`; crypto_major avg `0.0942` n `8`; equity avg `-0.1116` n `113`; fx avg `0.0042` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0137` n `20`; unknown avg `-0.0641` n `785`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.1261` n `230`; crypto_major avg `0.2385` n `8`; equity avg `0.2794` n `113`; fx avg `-0.0136` n `6`; index avg `0.0889` n `25`; metal avg `0.0746` n `20`; unknown avg `-0.17` n `785`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.1479` n `230`; crypto_major avg `-0.1836` n `8`; equity avg `0.2508` n `113`; fx avg `-0.0432` n `6`; index avg `0.0719` n `25`; metal avg `0.1588` n `20`; unknown avg `-0.2431` n `785`
- 24h: commodity avg `0.7723` n `12`; crypto_alt avg `-0.3359` n `230`; crypto_major avg `-0.3706` n `8`; equity avg `-1.1467` n `113`; fx avg `0.1072` n `6`; index avg `-0.0064` n `25`; metal avg `0.74` n `20`; unknown avg `103.7824` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
