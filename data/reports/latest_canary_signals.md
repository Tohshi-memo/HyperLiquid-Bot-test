# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T19:37:19.070531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0602` n `12`; crypto_alt avg `0.4793` n `228`; crypto_major avg `0.5078` n `8`; equity avg `0.1889` n `69`; fx avg `0.0077` n `6`; index avg `0.0989` n `23`; metal avg `-0.0451` n `18`; unknown avg `1.0721` n `419`
- 1h: commodity avg `0.1753` n `12`; crypto_alt avg `-0.5146` n `228`; crypto_major avg `-0.1811` n `8`; equity avg `-0.0793` n `69`; fx avg `0.0102` n `6`; index avg `0.0528` n `23`; metal avg `-0.0293` n `18`; unknown avg `0.7557` n `419`
- 4h: commodity avg `-0.0964` n `12`; crypto_alt avg `-0.9678` n `228`; crypto_major avg `-0.4601` n `8`; equity avg `0.0214` n `69`; fx avg `-0.0023` n `6`; index avg `0.1718` n `23`; metal avg `-0.1729` n `18`; unknown avg `-0.06` n `418`
- 24h: commodity avg `-0.4947` n `12`; crypto_alt avg `0.5092` n `228`; crypto_major avg `1.1686` n `8`; equity avg `1.1069` n `69`; fx avg `0.2252` n `6`; index avg `-0.0304` n `23`; metal avg `0.2098` n `18`; unknown avg `1.469` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
