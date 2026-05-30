# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T10:52:20.388626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.0417` n `228`; crypto_major avg `0.1026` n `8`; equity avg `0.0079` n `69`; fx avg `0.0002` n `6`; index avg `0.0073` n `23`; metal avg `-0.005` n `18`; unknown avg `-0.0009` n `421`
- 1h: commodity avg `0.0594` n `12`; crypto_alt avg `0.0812` n `228`; crypto_major avg `0.1393` n `8`; equity avg `0.0509` n `69`; fx avg `0.0018` n `6`; index avg `0.0155` n `23`; metal avg `0.0135` n `18`; unknown avg `0.0905` n `421`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `0.11` n `228`; crypto_major avg `0.3481` n `8`; equity avg `0.1235` n `69`; fx avg `0.0231` n `6`; index avg `-0.0483` n `23`; metal avg `0.0364` n `18`; unknown avg `-0.1713` n `421`
- 24h: commodity avg `-0.1797` n `12`; crypto_alt avg `1.6242` n `228`; crypto_major avg `2.0779` n `8`; equity avg `1.1793` n `69`; fx avg `0.1001` n `6`; index avg `0.0225` n `23`; metal avg `-0.1881` n `18`; unknown avg `0.5543` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
