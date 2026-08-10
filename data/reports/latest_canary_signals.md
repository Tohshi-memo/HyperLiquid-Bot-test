# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T17:37:32.384718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.1123` n `8`; equity avg `0.021` n `113`; fx avg `0.0029` n `6`; index avg `-0.0195` n `25`; metal avg `0.0201` n `20`; unknown avg `0.0307` n `785`
- 1h: commodity avg `0.0855` n `12`; crypto_alt avg `0.1297` n `230`; crypto_major avg `0.1684` n `8`; equity avg `-0.0309` n `113`; fx avg `-0.001` n `6`; index avg `-0.0098` n `25`; metal avg `0.0232` n `20`; unknown avg `0.0478` n `785`
- 4h: commodity avg `0.355` n `12`; crypto_alt avg `-0.4439` n `230`; crypto_major avg `-0.4587` n `8`; equity avg `-0.1655` n `113`; fx avg `0.0119` n `6`; index avg `0.003` n `25`; metal avg `0.2417` n `20`; unknown avg `1.8968` n `784`
- 24h: commodity avg `1.2394` n `12`; crypto_alt avg `-0.6808` n `230`; crypto_major avg `-1.311` n `8`; equity avg `-1.314` n `113`; fx avg `0.2509` n `6`; index avg `-0.0557` n `25`; metal avg `0.0371` n `20`; unknown avg `103.3618` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
