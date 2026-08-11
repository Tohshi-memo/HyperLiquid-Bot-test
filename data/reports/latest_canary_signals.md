# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T08:37:28.915998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0356` n `230`; crypto_major avg `0.0599` n `8`; equity avg `-0.1373` n `113`; fx avg `0.004` n `6`; index avg `-0.0039` n `25`; metal avg `0.0823` n `20`; unknown avg `0.006` n `785`
- 1h: commodity avg `0.0524` n `12`; crypto_alt avg `0.0314` n `230`; crypto_major avg `0.0738` n `8`; equity avg `-0.3078` n `113`; fx avg `0.0138` n `6`; index avg `-0.032` n `25`; metal avg `0.1033` n `20`; unknown avg `0.0233` n `785`
- 4h: commodity avg `0.4054` n `12`; crypto_alt avg `-0.3951` n `230`; crypto_major avg `-0.2193` n `8`; equity avg `-0.6582` n `113`; fx avg `0.037` n `6`; index avg `-0.1109` n `25`; metal avg `-0.1725` n `20`; unknown avg `-0.0425` n `753`
- 24h: commodity avg `1.1694` n `12`; crypto_alt avg `-1.3537` n `230`; crypto_major avg `-1.0069` n `8`; equity avg `-1.7253` n `113`; fx avg `0.0338` n `6`; index avg `-0.0835` n `25`; metal avg `0.2435` n `20`; unknown avg `0.1235` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
