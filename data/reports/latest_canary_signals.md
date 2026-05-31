# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T04:07:20.497121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `-0.0451` n `228`; crypto_major avg `-0.0998` n `8`; equity avg `0.0118` n `69`; fx avg `-0.001` n `6`; index avg `-0.0015` n `23`; metal avg `0.0145` n `18`; unknown avg `-0.0509` n `421`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.1333` n `228`; crypto_major avg `0.0804` n `8`; equity avg `0.0392` n `69`; fx avg `0.002` n `6`; index avg `-0.0183` n `23`; metal avg `0.0064` n `18`; unknown avg `-0.2899` n `421`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `0.6939` n `228`; crypto_major avg `0.6578` n `8`; equity avg `0.1758` n `69`; fx avg `0.0189` n `6`; index avg `-0.0168` n `23`; metal avg `-0.032` n `18`; unknown avg `-0.2231` n `419`
- 24h: commodity avg `-0.2004` n `12`; crypto_alt avg `0.5698` n `228`; crypto_major avg `2.4008` n `8`; equity avg `1.0546` n `69`; fx avg `0.0469` n `6`; index avg `0.0953` n `23`; metal avg `0.0156` n `18`; unknown avg `0.6944` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
