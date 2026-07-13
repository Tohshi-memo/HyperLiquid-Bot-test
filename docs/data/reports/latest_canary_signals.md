# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T14:07:31.484529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.2104` n `230`; crypto_major avg `0.2612` n `8`; equity avg `0.0267` n `92`; fx avg `0.0022` n `6`; index avg `0.0448` n `25`; metal avg `-0.1137` n `20`; unknown avg `0.048` n `766`
- 1h: commodity avg `-0.1513` n `12`; crypto_alt avg `-0.006` n `230`; crypto_major avg `-0.146` n `8`; equity avg `-0.6344` n `92`; fx avg `-0.0041` n `6`; index avg `-0.0404` n `25`; metal avg `-0.1769` n `20`; unknown avg `-0.0216` n `766`
- 4h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.3425` n `230`; crypto_major avg `-0.7463` n `8`; equity avg `-0.7554` n `92`; fx avg `0.0149` n `6`; index avg `-0.0377` n `25`; metal avg `-0.1875` n `20`; unknown avg `0.1887` n `766`
- 24h: commodity avg `-0.2031` n `12`; crypto_alt avg `-1.34` n `230`; crypto_major avg `-2.1892` n `8`; equity avg `-2.7632` n `92`; fx avg `-0.064` n `6`; index avg `-0.4639` n `25`; metal avg `-0.3471` n `20`; unknown avg `-0.2345` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
