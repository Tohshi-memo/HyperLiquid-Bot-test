# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T12:37:25.999722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.258` n `239`; crypto_major avg `-0.2142` n `8`; equity avg `-0.0223` n `162`; fx avg `-0.0093` n `6`; index avg `0.0309` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.7666` n `1265`
- 1h: commodity avg `-0.0942` n `13`; crypto_alt avg `-0.9038` n `239`; crypto_major avg `-1.0606` n `8`; equity avg `-0.8229` n `162`; fx avg `-0.0077` n `6`; index avg `-0.0861` n `27`; metal avg `-0.0655` n `20`; unknown avg `159.8737` n `1257`
- 4h: commodity avg `-0.2269` n `13`; crypto_alt avg `-0.6897` n `239`; crypto_major avg `-0.6936` n `8`; equity avg `-1.1539` n `162`; fx avg `-0.0054` n `6`; index avg `-0.1256` n `27`; metal avg `0.1071` n `20`; unknown avg `18.2093` n `1255`
- 24h: commodity avg `-0.5175` n `13`; crypto_alt avg `-2.2824` n `239`; crypto_major avg `-2.1434` n `8`; equity avg `-1.7174` n `162`; fx avg `-0.0668` n `6`; index avg `-0.1407` n `27`; metal avg `0.029` n `20`; unknown avg `23.3786` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
