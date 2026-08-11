# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T12:22:33.880189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.088` n `12`; crypto_alt avg `-0.0923` n `230`; crypto_major avg `-0.0399` n `8`; equity avg `0.0205` n `113`; fx avg `0.0071` n `6`; index avg `0.0107` n `25`; metal avg `-0.0405` n `20`; unknown avg `-0.0152` n `785`
- 1h: commodity avg `0.1157` n `12`; crypto_alt avg `-0.082` n `230`; crypto_major avg `0.1029` n `8`; equity avg `0.0268` n `113`; fx avg `0.013` n `6`; index avg `0.0125` n `25`; metal avg `-0.054` n `20`; unknown avg `-0.0762` n `785`
- 4h: commodity avg `-0.3717` n `12`; crypto_alt avg `0.0505` n `230`; crypto_major avg `0.6139` n `8`; equity avg `0.5515` n `113`; fx avg `-0.0581` n `6`; index avg `0.1286` n `25`; metal avg `0.1597` n `20`; unknown avg `-0.0943` n `785`
- 24h: commodity avg `0.5975` n `12`; crypto_alt avg `-1.3879` n `230`; crypto_major avg `-0.5206` n `8`; equity avg `-0.3742` n `113`; fx avg `-0.0191` n `6`; index avg `0.147` n `25`; metal avg `0.408` n `20`; unknown avg `-0.0073` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
