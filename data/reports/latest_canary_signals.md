# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T00:37:23.700237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `12`; crypto_alt avg `-0.0933` n `228`; crypto_major avg `-0.0417` n `8`; equity avg `0.0241` n `69`; fx avg `-0.0016` n `6`; index avg `-0.0012` n `23`; metal avg `0.0049` n `18`; unknown avg `-0.2313` n `421`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.4475` n `228`; crypto_major avg `0.4108` n `8`; equity avg `0.0609` n `69`; fx avg `0.0065` n `6`; index avg `-0.0373` n `23`; metal avg `0.0057` n `18`; unknown avg `-0.3695` n `421`
- 4h: commodity avg `0.0412` n `12`; crypto_alt avg `-0.5703` n `228`; crypto_major avg `0.1089` n `8`; equity avg `0.1707` n `69`; fx avg `-0.0116` n `6`; index avg `0.0173` n `23`; metal avg `-0.0215` n `18`; unknown avg `-0.3159` n `421`
- 24h: commodity avg `-0.3269` n `12`; crypto_alt avg `0.8324` n `228`; crypto_major avg `2.6443` n `8`; equity avg `1.1019` n `69`; fx avg `0.0288` n `6`; index avg `0.0414` n `23`; metal avg `0.0191` n `18`; unknown avg `0.3146` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
