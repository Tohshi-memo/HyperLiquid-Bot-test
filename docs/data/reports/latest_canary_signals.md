# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T18:37:41.348065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `0.1652` n `239`; crypto_major avg `0.1115` n `8`; equity avg `0.0866` n `162`; fx avg `-0.0066` n `6`; index avg `0.0094` n `27`; metal avg `0.0205` n `20`; unknown avg `0.1915` n `1261`
- 1h: commodity avg `0.1516` n `13`; crypto_alt avg `0.3206` n `239`; crypto_major avg `0.2919` n `8`; equity avg `0.0692` n `162`; fx avg `-0.0117` n `6`; index avg `-0.0073` n `27`; metal avg `0.0637` n `20`; unknown avg `0.2024` n `1253`
- 4h: commodity avg `0.4161` n `13`; crypto_alt avg `0.1989` n `239`; crypto_major avg `0.2485` n `8`; equity avg `1.0797` n `162`; fx avg `-0.0576` n `6`; index avg `0.0902` n `27`; metal avg `-0.0744` n `20`; unknown avg `57.4523` n `1229`
- 24h: commodity avg `0.5265` n `13`; crypto_alt avg `-3.0666` n `239`; crypto_major avg `-3.3051` n `8`; equity avg `-2.8244` n `162`; fx avg `-0.1663` n `6`; index avg `-0.1533` n `27`; metal avg `-0.7508` n `20`; unknown avg `17.3261` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
