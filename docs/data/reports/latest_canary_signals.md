# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:07:34.046976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.0762` n `230`; crypto_major avg `0.0624` n `8`; equity avg `0.0078` n `114`; fx avg `-0.0038` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.0008` n `791`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `0.1676` n `230`; crypto_major avg `0.1928` n `8`; equity avg `0.0177` n `114`; fx avg `0.0962` n `6`; index avg `0.0032` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.2466` n `791`
- 4h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.3401` n `230`; crypto_major avg `0.5039` n `8`; equity avg `0.0262` n `114`; fx avg `0.0633` n `6`; index avg `0.0002` n `25`; metal avg `0.021` n `20`; unknown avg `0.3588` n `791`
- 24h: commodity avg `0.1758` n `12`; crypto_alt avg `0.3523` n `230`; crypto_major avg `-0.2247` n `8`; equity avg `-0.0704` n `114`; fx avg `0.2088` n `6`; index avg `-0.0181` n `25`; metal avg `0.4143` n `20`; unknown avg `-0.0851` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
