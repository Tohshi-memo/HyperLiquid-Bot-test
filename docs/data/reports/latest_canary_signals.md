# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T18:07:38.354403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `12`; crypto_alt avg `0.041` n `230`; crypto_major avg `0.0358` n `8`; equity avg `0.0215` n `113`; fx avg `0.0038` n `6`; index avg `-0.0137` n `25`; metal avg `-0.0786` n `20`; unknown avg `0.0678` n `785`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `0.0192` n `230`; crypto_major avg `0.2853` n `8`; equity avg `0.1006` n `113`; fx avg `0.0088` n `6`; index avg `0.0042` n `25`; metal avg `-0.1095` n `20`; unknown avg `0.1097` n `785`
- 4h: commodity avg `0.23` n `12`; crypto_alt avg `-1.1506` n `230`; crypto_major avg `-0.4041` n `8`; equity avg `-0.4149` n `113`; fx avg `0.0118` n `6`; index avg `-0.1157` n `25`; metal avg `-0.1472` n `20`; unknown avg `0.0105` n `785`
- 24h: commodity avg `0.1565` n `12`; crypto_alt avg `-2.0217` n `230`; crypto_major avg `-0.1021` n `8`; equity avg `0.1459` n `113`; fx avg `-0.0569` n `6`; index avg `0.0601` n `25`; metal avg `-0.0694` n `20`; unknown avg `-0.3367` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
