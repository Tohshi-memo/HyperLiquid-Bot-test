# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T08:52:22.018091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.0457` n `228`; crypto_major avg `0.01` n `8`; equity avg `0.0335` n `69`; fx avg `0.1805` n `6`; index avg `0.0695` n `23`; metal avg `0.0613` n `18`; unknown avg `-0.0125` n `421`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.0207` n `228`; crypto_major avg `0.0288` n `8`; equity avg `-0.0037` n `69`; fx avg `-0.0025` n `6`; index avg `-0.0276` n `23`; metal avg `-0.0047` n `18`; unknown avg `-0.2227` n `421`
- 4h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.3322` n `228`; crypto_major avg `0.6771` n `8`; equity avg `0.2059` n `69`; fx avg `0.0041` n `6`; index avg `0.0845` n `23`; metal avg `0.0149` n `18`; unknown avg `-0.0761` n `401`
- 24h: commodity avg `-0.8511` n `12`; crypto_alt avg `1.3928` n `228`; crypto_major avg `1.7482` n `8`; equity avg `1.1578` n `69`; fx avg `0.0834` n `6`; index avg `0.1979` n `23`; metal avg `0.3625` n `18`; unknown avg `0.1158` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
