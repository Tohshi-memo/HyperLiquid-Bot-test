# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T00:07:29.258816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.2395` n `239`; crypto_major avg `0.1451` n `8`; equity avg `0.1631` n `168`; fx avg `-0.0087` n `6`; index avg `0.0085` n `27`; metal avg `-0.0218` n `20`; unknown avg `0.1852` n `1249`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `0.691` n `239`; crypto_major avg `0.6138` n `8`; equity avg `0.7423` n `168`; fx avg `-0.0075` n `6`; index avg `0.0617` n `27`; metal avg `0.0785` n `20`; unknown avg `241.6202` n `1253`
- 4h: commodity avg `0.0904` n `13`; crypto_alt avg `0.7758` n `239`; crypto_major avg `0.4326` n `8`; equity avg `0.8879` n `168`; fx avg `-0.0275` n `6`; index avg `0.0551` n `27`; metal avg `0.176` n `20`; unknown avg `6.1713` n `1143`
- 24h: commodity avg `0.3874` n `13`; crypto_alt avg `2.902` n `239`; crypto_major avg `1.5952` n `8`; equity avg `0.6132` n `168`; fx avg `-0.0161` n `6`; index avg `0.0353` n `27`; metal avg `0.318` n `20`; unknown avg `770.7163` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
