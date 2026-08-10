# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T18:22:28.776393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1294` n `12`; crypto_alt avg `-0.0192` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `-0.1058` n `113`; fx avg `-0.0011` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.1331` n `785`
- 1h: commodity avg `0.1925` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `0.0561` n `8`; equity avg `-0.0923` n `113`; fx avg `0.0067` n `6`; index avg `-0.0334` n `25`; metal avg `-0.0231` n `20`; unknown avg `-0.1746` n `785`
- 4h: commodity avg `0.4144` n `12`; crypto_alt avg `-0.4287` n `230`; crypto_major avg `-0.5094` n `8`; equity avg `-0.5364` n `113`; fx avg `0.0151` n `6`; index avg `-0.0662` n `25`; metal avg `0.1773` n `20`; unknown avg `0.036` n `784`
- 24h: commodity avg `1.3725` n `12`; crypto_alt avg `-0.7498` n `230`; crypto_major avg `-1.2523` n `8`; equity avg `-1.4617` n `113`; fx avg `0.2459` n `6`; index avg `-0.0868` n `25`; metal avg `-0.009` n `20`; unknown avg `103.3698` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
