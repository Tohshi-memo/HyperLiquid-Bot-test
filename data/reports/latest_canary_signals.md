# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T05:22:19.763957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1089` n `12`; crypto_alt avg `0.3462` n `228`; crypto_major avg `0.1312` n `8`; equity avg `0.1212` n `69`; fx avg `-0.004` n `6`; index avg `-0.0004` n `23`; metal avg `0.0596` n `18`; unknown avg `-0.2075` n `422`
- 1h: commodity avg `-0.1162` n `12`; crypto_alt avg `-0.2233` n `228`; crypto_major avg `-0.4121` n `8`; equity avg `0.3579` n `69`; fx avg `-0.0292` n `6`; index avg `0.1654` n `23`; metal avg `0.2835` n `18`; unknown avg `-0.714` n `422`
- 4h: commodity avg `-0.3263` n `12`; crypto_alt avg `0.0039` n `228`; crypto_major avg `-0.3512` n `8`; equity avg `0.8397` n `69`; fx avg `0.0455` n `6`; index avg `0.1018` n `23`; metal avg `0.3696` n `18`; unknown avg `-0.1441` n `422`
- 24h: commodity avg `-0.734` n `12`; crypto_alt avg `-0.6757` n `228`; crypto_major avg `-1.5068` n `8`; equity avg `-0.1426` n `69`; fx avg `0.0418` n `6`; index avg `-0.5384` n `23`; metal avg `0.2428` n `18`; unknown avg `2.1762` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
