# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T00:37:23.574226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0967` n `12`; crypto_alt avg `-0.002` n `230`; crypto_major avg `-0.0677` n `8`; equity avg `-0.2312` n `92`; fx avg `0.0184` n `6`; index avg `-0.0659` n `25`; metal avg `-0.0192` n `20`; unknown avg `0.058` n `768`
- 1h: commodity avg `0.2196` n `12`; crypto_alt avg `0.0031` n `230`; crypto_major avg `-0.1583` n `8`; equity avg `0.1074` n `92`; fx avg `0.0766` n `6`; index avg `0.0197` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.2994` n `768`
- 4h: commodity avg `0.1274` n `12`; crypto_alt avg `0.3859` n `230`; crypto_major avg `0.2462` n `8`; equity avg `0.4383` n `92`; fx avg `0.0442` n `6`; index avg `0.0851` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.5687` n `766`
- 24h: commodity avg `0.1489` n `12`; crypto_alt avg `1.8415` n `230`; crypto_major avg `3.1479` n `8`; equity avg `1.7407` n `92`; fx avg `0.0429` n `6`; index avg `0.5346` n `25`; metal avg `0.6265` n `20`; unknown avg `0.1532` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
