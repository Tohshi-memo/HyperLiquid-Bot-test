# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T08:52:31.032749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.213` n `230`; crypto_major avg `-0.0251` n `8`; equity avg `0.0298` n `113`; fx avg `-0.0043` n `6`; index avg `0.0242` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.0933` n `786`
- 1h: commodity avg `-0.0872` n `12`; crypto_alt avg `-0.33` n `230`; crypto_major avg `-0.0364` n `8`; equity avg `0.2685` n `113`; fx avg `-0.0142` n `6`; index avg `0.0647` n `25`; metal avg `-0.0457` n `20`; unknown avg `-0.1004` n `786`
- 4h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.8111` n `230`; crypto_major avg `-0.1328` n `8`; equity avg `0.3885` n `113`; fx avg `0.0054` n `6`; index avg `0.0777` n `25`; metal avg `0.0596` n `20`; unknown avg `-0.1839` n `770`
- 24h: commodity avg `-0.1683` n `12`; crypto_alt avg `-1.461` n `230`; crypto_major avg `0.5533` n `8`; equity avg `2.6043` n `113`; fx avg `-0.0014` n `6`; index avg `0.262` n `25`; metal avg `0.1163` n `20`; unknown avg `-0.2574` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
