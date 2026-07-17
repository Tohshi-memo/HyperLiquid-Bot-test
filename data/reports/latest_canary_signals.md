# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T07:07:24.976002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0926` n `12`; crypto_alt avg `-0.0025` n `230`; crypto_major avg `0.0854` n `8`; equity avg `-0.0468` n `96`; fx avg `-0.0322` n `6`; index avg `0.0029` n `25`; metal avg `-0.017` n `20`; unknown avg `0.0034` n `768`
- 1h: commodity avg `0.1368` n `12`; crypto_alt avg `0.1746` n `230`; crypto_major avg `0.1327` n `8`; equity avg `0.1054` n `96`; fx avg `0.005` n `6`; index avg `0.0026` n `25`; metal avg `-0.0236` n `20`; unknown avg `-0.0582` n `768`
- 4h: commodity avg `-0.1082` n `12`; crypto_alt avg `-0.4295` n `230`; crypto_major avg `-0.8482` n `8`; equity avg `-0.8198` n `94`; fx avg `-0.0084` n `6`; index avg `-0.1469` n `25`; metal avg `-0.0872` n `20`; unknown avg `-0.099` n `736`
- 24h: commodity avg `-0.1062` n `12`; crypto_alt avg `-2.2457` n `230`; crypto_major avg `-3.7511` n `8`; equity avg `-5.7247` n `94`; fx avg `-0.0803` n `6`; index avg `-0.7801` n `25`; metal avg `-0.7803` n `20`; unknown avg `-0.6052` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
