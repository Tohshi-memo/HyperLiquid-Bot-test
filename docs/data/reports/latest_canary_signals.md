# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T00:22:27.502095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0954` n `13`; crypto_alt avg `-0.3804` n `239`; crypto_major avg `-0.4155` n `8`; equity avg `-0.0965` n `162`; fx avg `-0.0253` n `6`; index avg `-0.0329` n `27`; metal avg `-0.033` n `20`; unknown avg `6.7398` n `1263`
- 1h: commodity avg `0.1203` n `13`; crypto_alt avg `-0.1719` n `239`; crypto_major avg `-0.2038` n `8`; equity avg `0.2219` n `162`; fx avg `-0.0122` n `6`; index avg `0.0067` n `27`; metal avg `0.0435` n `20`; unknown avg `2.0811` n `1257`
- 4h: commodity avg `-0.1902` n `13`; crypto_alt avg `0.334` n `239`; crypto_major avg `0.4544` n `8`; equity avg `1.0704` n `162`; fx avg `-0.0287` n `6`; index avg `0.1604` n `27`; metal avg `0.3318` n `20`; unknown avg `0.5454` n `1187`
- 24h: commodity avg `-0.2038` n `13`; crypto_alt avg `1.6995` n `239`; crypto_major avg `2.6804` n `8`; equity avg `1.9281` n `162`; fx avg `0.0031` n `6`; index avg `0.2303` n `27`; metal avg `0.5077` n `20`; unknown avg `2.158` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
