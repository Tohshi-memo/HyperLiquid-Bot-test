# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T13:52:27.428746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `0.0324` n `230`; crypto_major avg `0.0484` n `8`; equity avg `-0.2585` n `113`; fx avg `-0.0306` n `6`; index avg `-0.0408` n `25`; metal avg `-0.0253` n `20`; unknown avg `-0.0598` n `785`
- 1h: commodity avg `-0.2292` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `-0.117` n `8`; equity avg `-0.1566` n `113`; fx avg `-0.0293` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0195` n `20`; unknown avg `0.007` n `785`
- 4h: commodity avg `-0.4606` n `12`; crypto_alt avg `-0.2953` n `230`; crypto_major avg `-0.0197` n `8`; equity avg `0.2295` n `113`; fx avg `-0.0733` n `6`; index avg `0.024` n `25`; metal avg `-0.0788` n `20`; unknown avg `-0.2084` n `785`
- 24h: commodity avg `0.1395` n `12`; crypto_alt avg `-1.1926` n `230`; crypto_major avg `0.0767` n `8`; equity avg `-0.19` n `113`; fx avg `-0.0847` n `6`; index avg `0.1026` n `25`; metal avg `0.4271` n `20`; unknown avg `-0.1165` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
