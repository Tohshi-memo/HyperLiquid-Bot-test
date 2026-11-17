# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T03:52:27.018604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0491` n `13`; crypto_alt avg `-0.2526` n `239`; crypto_major avg `-0.0523` n `8`; equity avg `-0.3675` n `162`; fx avg `-0.0064` n `6`; index avg `-0.0491` n `27`; metal avg `-0.0411` n `20`; unknown avg `0.1432` n `1266`
- 1h: commodity avg `-0.0547` n `13`; crypto_alt avg `0.7214` n `239`; crypto_major avg `0.9374` n `8`; equity avg `0.4044` n `162`; fx avg `-0.0026` n `6`; index avg `-0.0079` n `27`; metal avg `0.0163` n `20`; unknown avg `-0.1371` n `1260`
- 4h: commodity avg `-0.1941` n `13`; crypto_alt avg `0.5753` n `239`; crypto_major avg `0.568` n `8`; equity avg `0.754` n `162`; fx avg `0.0362` n `6`; index avg `0.0056` n `27`; metal avg `0.1421` n `20`; unknown avg `0.0201` n `1254`
- 24h: commodity avg `-1.0736` n `13`; crypto_alt avg `0.552` n `239`; crypto_major avg `1.0622` n `8`; equity avg `-2.332` n `162`; fx avg `-0.0526` n `6`; index avg `-0.2451` n `27`; metal avg `-0.1034` n `20`; unknown avg `556.4676` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
