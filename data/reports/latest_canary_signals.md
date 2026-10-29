# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T08:37:26.424353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `13`; crypto_alt avg `-0.0138` n `238`; crypto_major avg `-0.0231` n `8`; equity avg `-0.06` n `155`; fx avg `0.0003` n `6`; index avg `-0.026` n `27`; metal avg `0.0065` n `20`; unknown avg `5.9467` n `1238`
- 1h: commodity avg `-0.0715` n `13`; crypto_alt avg `0.2607` n `238`; crypto_major avg `0.3068` n `8`; equity avg `0.0429` n `155`; fx avg `-0.0104` n `6`; index avg `-0.0303` n `27`; metal avg `0.0044` n `20`; unknown avg `164.5008` n `1216`
- 4h: commodity avg `-0.0216` n `13`; crypto_alt avg `-0.2553` n `238`; crypto_major avg `0.0772` n `8`; equity avg `-0.1812` n `155`; fx avg `-0.0029` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0903` n `20`; unknown avg `-0.0625` n `1188`
- 24h: commodity avg `-0.1266` n `13`; crypto_alt avg `-2.8462` n `238`; crypto_major avg `-2.074` n `8`; equity avg `-1.5406` n `154`; fx avg `0.0301` n `6`; index avg `-0.0999` n `27`; metal avg `-0.3701` n `20`; unknown avg `31.306` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
