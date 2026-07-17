# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T00:22:26.826925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1675` n `230`; crypto_major avg `0.1312` n `8`; equity avg `-0.251` n `94`; fx avg `-0.0068` n `6`; index avg `-0.0467` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.007` n `768`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.237` n `230`; crypto_major avg `0.2532` n `8`; equity avg `-0.3265` n `94`; fx avg `0.0149` n `6`; index avg `-0.0988` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0585` n `768`
- 4h: commodity avg `0.0929` n `12`; crypto_alt avg `-0.8258` n `230`; crypto_major avg `-0.798` n `8`; equity avg `-0.9117` n `94`; fx avg `0.0236` n `6`; index avg `-0.1315` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.2994` n `768`
- 24h: commodity avg `-0.0963` n `12`; crypto_alt avg `-1.7988` n `230`; crypto_major avg `-2.6234` n `8`; equity avg `-4.3706` n `94`; fx avg `-0.131` n `6`; index avg `-0.6032` n `25`; metal avg `-0.8591` n `20`; unknown avg `-0.6588` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
