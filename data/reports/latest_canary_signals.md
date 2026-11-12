# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T02:07:25.491452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0036` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0884` n `13`; crypto_alt avg `0.2563` n `239`; crypto_major avg `0.1958` n `8`; equity avg `0.0975` n `161`; fx avg `-0.0132` n `6`; index avg `0.0061` n `27`; metal avg `0.0519` n `20`; unknown avg `2.6321` n `1258`
- 1h: commodity avg `0.0347` n `13`; crypto_alt avg `0.0715` n `239`; crypto_major avg `-0.0343` n `8`; equity avg `0.7809` n `161`; fx avg `0.0005` n `6`; index avg `0.0658` n `27`; metal avg `-0.0575` n `20`; unknown avg `2.575` n `1256`
- 4h: commodity avg `-0.0554` n `13`; crypto_alt avg `-1.1342` n `239`; crypto_major avg `-1.0769` n `8`; equity avg `-0.8881` n `161`; fx avg `-0.0552` n `6`; index avg `-0.0733` n `27`; metal avg `0.0076` n `20`; unknown avg `59.7195` n `1250`
- 24h: commodity avg `0.1766` n `13`; crypto_alt avg `-1.2696` n `239`; crypto_major avg `-0.083` n `8`; equity avg `2.0709` n `161`; fx avg `-0.1488` n `6`; index avg `0.1978` n `27`; metal avg `-0.2922` n `20`; unknown avg `4.7999` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
