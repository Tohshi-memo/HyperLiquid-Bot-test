# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T14:37:30.294362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7857` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0006` n `13`; crypto_alt avg `0.7678` n `239`; crypto_major avg `0.8389` n `8`; equity avg `1.1085` n `162`; fx avg `-0.0105` n `6`; index avg `0.1171` n `27`; metal avg `-0.0281` n `20`; unknown avg `2.1178` n `1261`
- 1h: commodity avg `-0.1429` n `13`; crypto_alt avg `0.1873` n `239`; crypto_major avg `-0.0555` n `8`; equity avg `0.238` n `162`; fx avg `-0.0133` n `6`; index avg `0.0821` n `27`; metal avg `-0.0162` n `20`; unknown avg `4.0312` n `1255`
- 4h: commodity avg `0.1705` n `13`; crypto_alt avg `-1.2347` n `239`; crypto_major avg `-1.816` n `8`; equity avg `-1.4587` n `162`; fx avg `-0.0084` n `6`; index avg `-0.0303` n `27`; metal avg `-0.3257` n `20`; unknown avg `20.8518` n `1247`
- 24h: commodity avg `-0.081` n `13`; crypto_alt avg `-3.037` n `239`; crypto_major avg `-2.4237` n `8`; equity avg `-1.7551` n `162`; fx avg `-0.0666` n `6`; index avg `-0.0112` n `27`; metal avg `-0.8776` n `20`; unknown avg `2.2255` n `1146`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
