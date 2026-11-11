# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T23:59:40.725861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `13`; crypto_alt avg `0.1824` n `239`; crypto_major avg `0.061` n `8`; equity avg `0.1402` n `160`; fx avg `-0.0168` n `6`; index avg `0.0238` n `27`; metal avg `0.0294` n `20`; unknown avg `1.5302` n `1256`
- 1h: commodity avg `-0.0286` n `13`; crypto_alt avg `0.1859` n `239`; crypto_major avg `0.0545` n `8`; equity avg `0.5286` n `160`; fx avg `-0.0017` n `6`; index avg `0.0621` n `27`; metal avg `0.0592` n `20`; unknown avg `0.8564` n `1252`
- 4h: commodity avg `-0.0132` n `13`; crypto_alt avg `0.58` n `239`; crypto_major avg `0.2024` n `8`; equity avg `1.1393` n `160`; fx avg `-0.0005` n `6`; index avg `0.1029` n `27`; metal avg `0.0613` n `20`; unknown avg `1.6381` n `1222`
- 24h: commodity avg `0.0775` n `13`; crypto_alt avg `-0.5596` n `239`; crypto_major avg `-2.6914` n `8`; equity avg `-1.0311` n `160`; fx avg `-0.1244` n `6`; index avg `-0.1181` n `27`; metal avg `-0.588` n `20`; unknown avg `0.8566` n `1169`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2583`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
