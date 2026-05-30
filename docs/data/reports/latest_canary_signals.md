# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T17:52:24.184569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `0.2746` n `228`; crypto_major avg `0.4367` n `8`; equity avg `0.0109` n `69`; fx avg `0.0` n `6`; index avg `0.0387` n `23`; metal avg `0.0147` n `18`; unknown avg `-0.0255` n `421`
- 1h: commodity avg `-0.0958` n `12`; crypto_alt avg `-0.0369` n `228`; crypto_major avg `0.4068` n `8`; equity avg `0.0431` n `69`; fx avg `-0.0092` n `6`; index avg `0.0218` n `23`; metal avg `0.0164` n `18`; unknown avg `-0.3338` n `421`
- 4h: commodity avg `-0.4544` n `12`; crypto_alt avg `0.3127` n `228`; crypto_major avg `1.0279` n `8`; equity avg `-0.0786` n `69`; fx avg `0.0019` n `6`; index avg `-0.0408` n `23`; metal avg `0.0499` n `18`; unknown avg `0.1095` n `421`
- 24h: commodity avg `0.0751` n `12`; crypto_alt avg `0.5266` n `228`; crypto_major avg `1.9502` n `8`; equity avg `0.8341` n `69`; fx avg `0.0062` n `6`; index avg `0.1199` n `23`; metal avg `0.0393` n `18`; unknown avg `-0.088` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
