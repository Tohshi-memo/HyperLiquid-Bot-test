# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T20:37:20.175782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.0142` n `228`; crypto_major avg `0.0223` n `8`; equity avg `0.0439` n `69`; fx avg `-0.0014` n `6`; index avg `0.0164` n `23`; metal avg `0.0066` n `18`; unknown avg `0.0555` n `421`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.2452` n `228`; crypto_major avg `0.0113` n `8`; equity avg `0.0984` n `69`; fx avg `0.0003` n `6`; index avg `-0.0301` n `23`; metal avg `0.0115` n `18`; unknown avg `-0.246` n `421`
- 4h: commodity avg `0.0073` n `12`; crypto_alt avg `0.3205` n `228`; crypto_major avg `0.3246` n `8`; equity avg `0.2548` n `69`; fx avg `0.0008` n `6`; index avg `-0.0123` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.3554` n `421`
- 24h: commodity avg `-0.0795` n `12`; crypto_alt avg `1.4338` n `228`; crypto_major avg `2.4392` n `8`; equity avg `0.9378` n `69`; fx avg `0.0043` n `6`; index avg `0.03` n `23`; metal avg `-0.0028` n `18`; unknown avg `0.2483` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
