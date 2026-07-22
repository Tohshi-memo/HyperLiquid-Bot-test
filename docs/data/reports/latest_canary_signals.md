# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T14:52:25.741238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.1344` n `230`; crypto_major avg `-0.0759` n `8`; equity avg `-0.1884` n `98`; fx avg `-0.0099` n `6`; index avg `-0.0269` n `25`; metal avg `-0.069` n `20`; unknown avg `0.2718` n `773`
- 1h: commodity avg `0.0275` n `12`; crypto_alt avg `-0.1697` n `230`; crypto_major avg `-0.1371` n `8`; equity avg `-0.125` n `98`; fx avg `-0.0313` n `6`; index avg `0.0126` n `25`; metal avg `-0.0792` n `20`; unknown avg `0.3992` n `773`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.0488` n `230`; crypto_major avg `-0.1736` n `8`; equity avg `0.4734` n `98`; fx avg `-0.0182` n `6`; index avg `0.0587` n `25`; metal avg `0.1024` n `20`; unknown avg `34.7931` n `773`
- 24h: commodity avg `0.5514` n `12`; crypto_alt avg `-0.4348` n `230`; crypto_major avg `-1.3006` n `8`; equity avg `0.2621` n `98`; fx avg `-0.038` n `6`; index avg `-0.0499` n `25`; metal avg `0.4359` n `20`; unknown avg `1.1228` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0711`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
