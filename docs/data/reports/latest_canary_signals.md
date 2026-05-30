# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T18:07:24.650261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `0.1426` n `228`; crypto_major avg `0.0049` n `8`; equity avg `0.022` n `69`; fx avg `-0.0018` n `6`; index avg `0.0041` n `23`; metal avg `-0.0037` n `18`; unknown avg `-0.0004` n `421`
- 1h: commodity avg `-0.0541` n `12`; crypto_alt avg `0.1768` n `228`; crypto_major avg `0.3314` n `8`; equity avg `0.0503` n `69`; fx avg `0.0236` n `6`; index avg `0.0161` n `23`; metal avg `0.001` n `18`; unknown avg `-0.3229` n `421`
- 4h: commodity avg `-0.4179` n `12`; crypto_alt avg `0.1828` n `228`; crypto_major avg `0.7945` n `8`; equity avg `-0.101` n `69`; fx avg `-0.0151` n `6`; index avg `-0.1244` n `23`; metal avg `0.0361` n `18`; unknown avg `-0.1093` n `421`
- 24h: commodity avg `0.0451` n `12`; crypto_alt avg `0.6425` n `228`; crypto_major avg `1.9415` n `8`; equity avg `0.9097` n `69`; fx avg `0.0055` n `6`; index avg `0.1413` n `23`; metal avg `-0.0408` n `18`; unknown avg `-0.0941` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
