# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T19:07:19.790967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0731` n `12`; crypto_alt avg `0.232` n `228`; crypto_major avg `0.1922` n `8`; equity avg `-0.048` n `69`; fx avg `0.0002` n `6`; index avg `0.0143` n `23`; metal avg `0.0981` n `18`; unknown avg `0.2593` n `419`
- 1h: commodity avg `0.0689` n `12`; crypto_alt avg `-0.8092` n `228`; crypto_major avg `-0.7196` n `8`; equity avg `-0.3413` n `69`; fx avg `0.0084` n `6`; index avg `-0.017` n `23`; metal avg `0.1066` n `18`; unknown avg `0.0692` n `419`
- 4h: commodity avg `0.1221` n `12`; crypto_alt avg `0.6673` n `228`; crypto_major avg `0.4049` n `8`; equity avg `0.1109` n `69`; fx avg `0.0115` n `6`; index avg `0.1081` n `23`; metal avg `-0.4964` n `18`; unknown avg `1.602` n `418`
- 24h: commodity avg `-0.8073` n `12`; crypto_alt avg `0.3903` n `228`; crypto_major avg `0.7346` n `8`; equity avg `0.9617` n `69`; fx avg `0.2004` n `6`; index avg `-0.1448` n `23`; metal avg `0.2379` n `18`; unknown avg `1.6791` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
