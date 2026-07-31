# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T01:37:31.793915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0847` n `12`; crypto_alt avg `-0.1468` n `230`; crypto_major avg `-0.183` n `8`; equity avg `-0.391` n `102`; fx avg `-0.0037` n `6`; index avg `-0.1158` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.1402` n `779`
- 1h: commodity avg `-0.3286` n `12`; crypto_alt avg `0.3061` n `230`; crypto_major avg `0.1386` n `8`; equity avg `0.0616` n `102`; fx avg `0.0651` n `6`; index avg `-0.0017` n `25`; metal avg `-0.1738` n `20`; unknown avg `0.0443` n `779`
- 4h: commodity avg `-0.2619` n `12`; crypto_alt avg `0.3271` n `230`; crypto_major avg `0.1713` n `8`; equity avg `1.1992` n `102`; fx avg `0.2292` n `6`; index avg `0.3547` n `25`; metal avg `-0.2239` n `20`; unknown avg `0.0383` n `779`
- 24h: commodity avg `-0.185` n `12`; crypto_alt avg `0.5405` n `230`; crypto_major avg `1.2197` n `8`; equity avg `6.762` n `102`; fx avg `-0.1914` n `6`; index avg `0.8523` n `25`; metal avg `0.2058` n `20`; unknown avg `0.0897` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
