# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T19:39:36.035654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.1738` n `228`; crypto_major avg `-0.0991` n `8`; equity avg `-0.0118` n `69`; fx avg `0.0046` n `6`; index avg `-0.0155` n `23`; metal avg `-0.0104` n `18`; unknown avg `-0.6149` n `421`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0795` n `228`; crypto_major avg `0.0159` n `8`; equity avg `0.0872` n `69`; fx avg `0.0098` n `6`; index avg `0.0127` n `23`; metal avg `-0.0215` n `18`; unknown avg `0.3069` n `421`
- 4h: commodity avg `-0.4481` n `12`; crypto_alt avg `0.4851` n `228`; crypto_major avg `0.8334` n `8`; equity avg `0.016` n `69`; fx avg `-0.0118` n `6`; index avg `-0.022` n `23`; metal avg `-0.0016` n `18`; unknown avg `-0.0524` n `421`
- 24h: commodity avg `-0.0321` n `12`; crypto_alt avg `1.5167` n `228`; crypto_major avg `2.4504` n `8`; equity avg `1.1047` n `69`; fx avg `-0.0067` n `6`; index avg `0.0654` n `23`; metal avg `-0.1602` n `18`; unknown avg `0.0485` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
