# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T10:07:26.912508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.6599` n `234`; crypto_major avg `-0.3284` n `8`; equity avg `-0.0475` n `140`; fx avg `-0.0043` n `6`; index avg `0.0018` n `26`; metal avg `-0.0084` n `20`; unknown avg `2.2921` n `941`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.4307` n `234`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0168` n `140`; fx avg `-0.0064` n `6`; index avg `0.0098` n `26`; metal avg `0.0058` n `20`; unknown avg `1.5245` n `941`
- 4h: commodity avg `-0.0136` n `12`; crypto_alt avg `-1.1738` n `234`; crypto_major avg `-0.2471` n `8`; equity avg `-0.071` n `140`; fx avg `-0.0133` n `6`; index avg `-0.0045` n `26`; metal avg `0.0151` n `20`; unknown avg `1.7595` n `935`
- 24h: commodity avg `0.2262` n `12`; crypto_alt avg `-1.9567` n `234`; crypto_major avg `-2.0161` n `8`; equity avg `-0.2933` n `140`; fx avg `-0.0778` n `6`; index avg `-0.0551` n `26`; metal avg `0.0221` n `20`; unknown avg `2.2875` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
