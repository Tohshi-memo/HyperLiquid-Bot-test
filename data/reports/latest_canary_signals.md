# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T11:22:27.984888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1087` n `13`; crypto_alt avg `0.1045` n `237`; crypto_major avg `0.0319` n `8`; equity avg `-0.0471` n `152`; fx avg `-0.0084` n `6`; index avg `-0.0162` n `26`; metal avg `0.0083` n `20`; unknown avg `0.8652` n `1233`
- 1h: commodity avg `-0.1063` n `13`; crypto_alt avg `-0.3028` n `237`; crypto_major avg `-0.3593` n `8`; equity avg `-0.365` n `152`; fx avg `0.0041` n `6`; index avg `-0.0303` n `26`; metal avg `0.0701` n `20`; unknown avg `2.1936` n `1231`
- 4h: commodity avg `-0.0207` n `13`; crypto_alt avg `-0.3326` n `237`; crypto_major avg `-0.2697` n `8`; equity avg `-0.645` n `152`; fx avg `-0.0338` n `6`; index avg `-0.0929` n `26`; metal avg `0.1028` n `20`; unknown avg `1.9453` n `1151`
- 24h: commodity avg `0.2824` n `13`; crypto_alt avg `-0.1478` n `237`; crypto_major avg `-0.0402` n `8`; equity avg `-1.5535` n `152`; fx avg `0.017` n `6`; index avg `-0.1547` n `26`; metal avg `-0.2598` n `20`; unknown avg `49.4015` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
