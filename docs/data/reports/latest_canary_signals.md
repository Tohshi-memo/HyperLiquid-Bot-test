# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T12:52:35.944021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0803` n `13`; crypto_alt avg `-0.0262` n `239`; crypto_major avg `-0.014` n `8`; equity avg `0.1266` n `162`; fx avg `0.0005` n `6`; index avg `0.024` n `27`; metal avg `0.015` n `20`; unknown avg `0.204` n `1265`
- 1h: commodity avg `-0.113` n `13`; crypto_alt avg `-1.0038` n `239`; crypto_major avg `-0.9991` n `8`; equity avg `-0.6163` n `162`; fx avg `-0.0049` n `6`; index avg `-0.0532` n `27`; metal avg `-0.0756` n `20`; unknown avg `10.3183` n `1257`
- 4h: commodity avg `-0.223` n `13`; crypto_alt avg `-0.7937` n `239`; crypto_major avg `-0.7353` n `8`; equity avg `-1.1032` n `162`; fx avg `-0.0363` n `6`; index avg `-0.1186` n `27`; metal avg `0.0653` n `20`; unknown avg `16.9147` n `1253`
- 24h: commodity avg `-0.5913` n `13`; crypto_alt avg `-2.4338` n `239`; crypto_major avg `-2.1359` n `8`; equity avg `-1.6044` n `162`; fx avg `-0.052` n `6`; index avg `-0.1164` n `27`; metal avg `0.039` n `20`; unknown avg `24.6914` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
