# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T12:52:27.317606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0712` n `13`; crypto_alt avg `0.0497` n `239`; crypto_major avg `0.1303` n `8`; equity avg `0.0158` n `162`; fx avg `0.0087` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0028` n `20`; unknown avg `0.2947` n `1261`
- 1h: commodity avg `-0.106` n `13`; crypto_alt avg `-0.058` n `239`; crypto_major avg `0.1712` n `8`; equity avg `-0.5829` n `162`; fx avg `-0.0175` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0505` n `20`; unknown avg `20.9458` n `1243`
- 4h: commodity avg `-0.2896` n `13`; crypto_alt avg `-0.8312` n `239`; crypto_major avg `-0.8859` n `8`; equity avg `-0.6261` n `162`; fx avg `-0.0269` n `6`; index avg `0.0032` n `27`; metal avg `-0.1509` n `20`; unknown avg `21.0975` n `1249`
- 24h: commodity avg `-0.2747` n `13`; crypto_alt avg `-2.8194` n `239`; crypto_major avg `-1.9735` n `8`; equity avg `-1.9868` n `162`; fx avg `-0.1364` n `6`; index avg `-0.1128` n `27`; metal avg `-0.9633` n `20`; unknown avg `0.8005` n `1140`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
