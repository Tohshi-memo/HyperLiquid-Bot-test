# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T09:07:29.540956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.0188` n `228`; crypto_major avg `0.0057` n `8`; equity avg `0.0001` n `88`; fx avg `-0.022` n `6`; index avg `-0.0037` n `23`; metal avg `0.0003` n `20`; unknown avg `-0.0917` n `764`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `-0.1283` n `228`; crypto_major avg `-0.2017` n `8`; equity avg `-0.0201` n `88`; fx avg `-0.0091` n `6`; index avg `-0.0096` n `23`; metal avg `-0.0033` n `20`; unknown avg `-0.0525` n `764`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `0.007` n `228`; crypto_major avg `0.1173` n `8`; equity avg `0.1915` n `88`; fx avg `-0.0081` n `6`; index avg `0.0092` n `23`; metal avg `-0.0058` n `20`; unknown avg `-0.0869` n `716`
- 24h: commodity avg `0.0826` n `12`; crypto_alt avg `1.1268` n `228`; crypto_major avg `1.1402` n `8`; equity avg `1.8175` n `87`; fx avg `0.0158` n `6`; index avg `0.0713` n `23`; metal avg `0.573` n `20`; unknown avg `-0.1938` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
