# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T09:37:18.513754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0231` n `228`; crypto_major avg `-0.027` n `8`; equity avg `-0.0051` n `69`; fx avg `0.0024` n `6`; index avg `-0.0183` n `23`; metal avg `0.0444` n `18`; unknown avg `-0.0151` n `417`
- 1h: commodity avg `-0.6213` n `12`; crypto_alt avg `0.4913` n `228`; crypto_major avg `0.2047` n `8`; equity avg `0.0596` n `69`; fx avg `-0.0353` n `6`; index avg `0.0247` n `23`; metal avg `0.3061` n `18`; unknown avg `0.1284` n `417`
- 4h: commodity avg `-0.0997` n `12`; crypto_alt avg `0.787` n `228`; crypto_major avg `0.8041` n `8`; equity avg `0.102` n `69`; fx avg `-0.0038` n `6`; index avg `0.0137` n `23`; metal avg `0.0592` n `18`; unknown avg `1.2757` n `407`
- 24h: commodity avg `0.1987` n `12`; crypto_alt avg `1.8583` n `228`; crypto_major avg `2.3118` n `8`; equity avg `3.5011` n `69`; fx avg `0.1374` n `6`; index avg `1.3076` n `23`; metal avg `1.7997` n `18`; unknown avg `1.9916` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
