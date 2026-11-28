# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T07:37:23.601534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.0707` n `239`; crypto_major avg `0.1555` n `8`; equity avg `0.0667` n `168`; fx avg `0.0016` n `6`; index avg `0.0015` n `27`; metal avg `0.0059` n `20`; unknown avg `2.4102` n `1269`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `0.0218` n `239`; crypto_major avg `-0.1942` n `8`; equity avg `0.0717` n `168`; fx avg `-0.0148` n `6`; index avg `0.0001` n `27`; metal avg `0.0228` n `20`; unknown avg `372.6609` n `1257`
- 4h: commodity avg `-0.0072` n `13`; crypto_alt avg `-1.1701` n `239`; crypto_major avg `-0.6415` n `8`; equity avg `-0.1192` n `168`; fx avg `-0.0035` n `6`; index avg `-0.0346` n `27`; metal avg `0.0026` n `20`; unknown avg `0.5951` n `1209`
- 24h: commodity avg `-0.7729` n `13`; crypto_alt avg `-2.8007` n `239`; crypto_major avg `-2.5105` n `8`; equity avg `0.2536` n `168`; fx avg `-0.1068` n `6`; index avg `0.0602` n `27`; metal avg `-0.2189` n `20`; unknown avg `215.0874` n `969`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
