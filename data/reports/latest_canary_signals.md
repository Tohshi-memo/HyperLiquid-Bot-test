# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T05:37:20.225291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0668` n `12`; crypto_alt avg `-0.0336` n `228`; crypto_major avg `-0.1727` n `8`; equity avg `-0.1746` n `69`; fx avg `-0.0073` n `6`; index avg `0.0128` n `23`; metal avg `-0.123` n `18`; unknown avg `-0.3415` n `417`
- 1h: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1737` n `228`; crypto_major avg `0.0559` n `8`; equity avg `-0.0145` n `69`; fx avg `0.0248` n `6`; index avg `0.0329` n `23`; metal avg `-0.0766` n `18`; unknown avg `-0.1376` n `417`
- 4h: commodity avg `-0.1903` n `12`; crypto_alt avg `-0.1791` n `228`; crypto_major avg `-0.0601` n `8`; equity avg `0.3612` n `69`; fx avg `0.0003` n `6`; index avg `0.2154` n `23`; metal avg `-0.2593` n `18`; unknown avg `-0.55` n `417`
- 24h: commodity avg `-0.0722` n `12`; crypto_alt avg `1.4615` n `228`; crypto_major avg `1.8814` n `8`; equity avg `4.0204` n `69`; fx avg `0.1449` n `6`; index avg `1.5146` n `23`; metal avg `2.1069` n `18`; unknown avg `0.8851` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
