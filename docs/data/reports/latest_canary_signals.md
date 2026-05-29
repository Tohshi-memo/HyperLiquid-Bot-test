# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T20:52:18.073859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.2045` n `228`; crypto_major avg `-0.1544` n `8`; equity avg `-0.0065` n `69`; fx avg `-0.0134` n `6`; index avg `-0.0174` n `23`; metal avg `-0.0901` n `18`; unknown avg `0.0446` n `419`
- 1h: commodity avg `-0.0758` n `12`; crypto_alt avg `0.1353` n `228`; crypto_major avg `-0.0638` n `8`; equity avg `0.1102` n `69`; fx avg `-0.0225` n `6`; index avg `0.0136` n `23`; metal avg `-0.1317` n `18`; unknown avg `-0.43` n `419`
- 4h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.5871` n `228`; crypto_major avg `-0.6921` n `8`; equity avg `0.1259` n `69`; fx avg `-0.0101` n `6`; index avg `0.0999` n `23`; metal avg `-0.2523` n `18`; unknown avg `-0.3232` n `419`
- 24h: commodity avg `-0.6809` n `12`; crypto_alt avg `0.3332` n `228`; crypto_major avg `0.8284` n `8`; equity avg `1.3035` n `69`; fx avg `0.1872` n `6`; index avg `0.1619` n `23`; metal avg `0.0411` n `18`; unknown avg `0.5785` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
