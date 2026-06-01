# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T22:22:23.548528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0602` n `12`; crypto_alt avg `0.2279` n `228`; crypto_major avg `0.3969` n `8`; equity avg `0.0137` n `69`; fx avg `-0.0071` n `6`; index avg `0.0557` n `23`; metal avg `0.013` n `18`; unknown avg `1.011` n `422`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `-0.0364` n `228`; crypto_major avg `0.1646` n `8`; equity avg `-0.0782` n `69`; fx avg `-0.0302` n `6`; index avg `-0.0802` n `23`; metal avg `-0.0171` n `18`; unknown avg `0.8909` n `422`
- 4h: commodity avg `0.2349` n `12`; crypto_alt avg `-0.581` n `228`; crypto_major avg `0.1617` n `8`; equity avg `-0.7996` n `69`; fx avg `-0.0329` n `6`; index avg `-0.4959` n `23`; metal avg `-0.3214` n `18`; unknown avg `0.5161` n `422`
- 24h: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.351` n `228`; crypto_major avg `-1.3388` n `8`; equity avg `-0.1999` n `69`; fx avg `0.0324` n `6`; index avg `0.0163` n `23`; metal avg `-0.0441` n `18`; unknown avg `3.028` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
