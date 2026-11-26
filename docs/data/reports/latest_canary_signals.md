# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T00:52:38.594209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `13`; crypto_alt avg `-0.0221` n `239`; crypto_major avg `-0.2266` n `8`; equity avg `0.0498` n `168`; fx avg `0.001` n `6`; index avg `0.0133` n `27`; metal avg `-0.1107` n `20`; unknown avg `158.0321` n `1267`
- 1h: commodity avg `-0.0021` n `13`; crypto_alt avg `0.6988` n `239`; crypto_major avg `0.2465` n `8`; equity avg `0.9396` n `168`; fx avg `-0.0165` n `6`; index avg `0.1046` n `27`; metal avg `-0.1066` n `20`; unknown avg `0.1193` n `1249`
- 4h: commodity avg `0.0098` n `13`; crypto_alt avg `1.1214` n `239`; crypto_major avg `0.3359` n `8`; equity avg `1.7586` n `168`; fx avg `-0.0281` n `6`; index avg `0.1594` n `27`; metal avg `0.0049` n `20`; unknown avg `469.4865` n `1155`
- 24h: commodity avg `0.347` n `13`; crypto_alt avg `3.4604` n `239`; crypto_major avg `1.8032` n `8`; equity avg `1.4999` n `168`; fx avg `-0.0111` n `6`; index avg `0.1254` n `27`; metal avg `0.2159` n `20`; unknown avg `770.5924` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
