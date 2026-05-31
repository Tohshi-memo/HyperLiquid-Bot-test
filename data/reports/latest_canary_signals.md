# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T18:07:24.564827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `-0.143` n `8`; equity avg `-0.0103` n `69`; fx avg `0.0007` n `6`; index avg `-0.0343` n `23`; metal avg `-0.0004` n `18`; unknown avg `-0.0694` n `421`
- 1h: commodity avg `0.1295` n `12`; crypto_alt avg `0.5336` n `228`; crypto_major avg `0.2613` n `8`; equity avg `0.0937` n `69`; fx avg `0.0` n `6`; index avg `0.0865` n `23`; metal avg `-0.0428` n `18`; unknown avg `-0.0782` n `421`
- 4h: commodity avg `0.1958` n `12`; crypto_alt avg `-0.6931` n `228`; crypto_major avg `-0.6326` n `8`; equity avg `0.0299` n `69`; fx avg `-0.0095` n `6`; index avg `0.2915` n `23`; metal avg `-0.0647` n `18`; unknown avg `0.0533` n `421`
- 24h: commodity avg `0.7113` n `12`; crypto_alt avg `-1.2176` n `228`; crypto_major avg `-0.5949` n `8`; equity avg `0.9215` n `69`; fx avg `-0.0092` n `6`; index avg `0.1538` n `23`; metal avg `-0.1538` n `18`; unknown avg `0.3577` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
