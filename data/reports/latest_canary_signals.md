# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T01:37:32.545803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0678` n `13`; crypto_alt avg `0.0111` n `239`; crypto_major avg `-0.1738` n `8`; equity avg `-0.3036` n `168`; fx avg `-0.0065` n `6`; index avg `-0.0356` n `27`; metal avg `-0.2335` n `20`; unknown avg `163.099` n `1265`
- 1h: commodity avg `-0.0037` n `13`; crypto_alt avg `0.1793` n `239`; crypto_major avg `-0.0092` n `8`; equity avg `-0.0926` n `168`; fx avg `-0.0203` n `6`; index avg `-0.0017` n `27`; metal avg `-0.1492` n `20`; unknown avg `161.7447` n `1261`
- 4h: commodity avg `0.0205` n `13`; crypto_alt avg `1.032` n `239`; crypto_major avg `0.1674` n `8`; equity avg `1.1981` n `168`; fx avg `-0.0454` n `6`; index avg `0.1008` n `27`; metal avg `-0.0205` n `20`; unknown avg `385.2133` n `1185`
- 24h: commodity avg `0.4287` n `13`; crypto_alt avg `3.7557` n `239`; crypto_major avg `2.3007` n `8`; equity avg `1.085` n `168`; fx avg `-0.0115` n `6`; index avg `0.0964` n `27`; metal avg `0.1123` n `20`; unknown avg `772.3016` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
