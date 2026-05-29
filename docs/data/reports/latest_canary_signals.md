# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T22:37:21.511083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `12`; crypto_alt avg `-0.1047` n `228`; crypto_major avg `-0.1607` n `8`; equity avg `0.0059` n `69`; fx avg `-0.0018` n `6`; index avg `0.0173` n `23`; metal avg `0.0114` n `18`; unknown avg `-0.2527` n `419`
- 1h: commodity avg `0.1462` n `12`; crypto_alt avg `0.004` n `228`; crypto_major avg `-0.0214` n `8`; equity avg `-0.0408` n `69`; fx avg `0.002` n `6`; index avg `0.0883` n `23`; metal avg `0.074` n `18`; unknown avg `0.0123` n `419`
- 4h: commodity avg `0.3118` n `12`; crypto_alt avg `-0.6825` n `228`; crypto_major avg `-0.629` n `8`; equity avg `0.1657` n `69`; fx avg `-0.0273` n `6`; index avg `0.0509` n `23`; metal avg `-0.2226` n `18`; unknown avg `-0.2669` n `419`
- 24h: commodity avg `-0.5774` n `12`; crypto_alt avg `0.783` n `228`; crypto_major avg `0.8396` n `8`; equity avg `1.0216` n `69`; fx avg `0.183` n `6`; index avg `0.1644` n `23`; metal avg `0.0825` n `18`; unknown avg `0.439` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
