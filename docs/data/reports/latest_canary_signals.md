# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T01:07:19.958872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `0.1674` n `228`; crypto_major avg `0.1211` n `8`; equity avg `0.0156` n `69`; fx avg `-0.0028` n `6`; index avg `-0.069` n `23`; metal avg `-0.0151` n `18`; unknown avg `-0.1232` n `419`
- 1h: commodity avg `-0.0756` n `12`; crypto_alt avg `0.6232` n `228`; crypto_major avg `0.4664` n `8`; equity avg `0.2217` n `69`; fx avg `-0.0009` n `6`; index avg `-0.0538` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.3342` n `419`
- 4h: commodity avg `0.0569` n `12`; crypto_alt avg `0.4638` n `228`; crypto_major avg `0.189` n `8`; equity avg `0.1155` n `69`; fx avg `-0.0216` n `6`; index avg `0.0025` n `23`; metal avg `0.1031` n `18`; unknown avg `-0.2951` n `419`
- 24h: commodity avg `-0.1807` n `12`; crypto_alt avg `0.6755` n `228`; crypto_major avg `0.9605` n `8`; equity avg `1.0544` n `69`; fx avg `0.0774` n `6`; index avg `0.2089` n `23`; metal avg `-0.0809` n `18`; unknown avg `0.4448` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
