# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T09:52:35.227025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1462` n `13`; crypto_alt avg `0.0342` n `239`; crypto_major avg `0.0368` n `8`; equity avg `0.0896` n `157`; fx avg `0.0004` n `6`; index avg `0.0306` n `27`; metal avg `0.0048` n `20`; unknown avg `1.0456` n `1264`
- 1h: commodity avg `-0.1512` n `13`; crypto_alt avg `0.4766` n `239`; crypto_major avg `0.5265` n `8`; equity avg `0.851` n `157`; fx avg `0.022` n `6`; index avg `0.0776` n `27`; metal avg `0.1206` n `20`; unknown avg `1.4072` n `1248`
- 4h: commodity avg `0.2559` n `13`; crypto_alt avg `0.2619` n `239`; crypto_major avg `0.447` n `8`; equity avg `0.8817` n `157`; fx avg `0.068` n `6`; index avg `0.0932` n `27`; metal avg `-0.1724` n `20`; unknown avg `1.6414` n `1210`
- 24h: commodity avg `-0.3578` n `13`; crypto_alt avg `-1.8513` n `238`; crypto_major avg `-1.1796` n `8`; equity avg `-3.6844` n `157`; fx avg `0.013` n `6`; index avg `-0.2392` n `27`; metal avg `-0.4475` n `20`; unknown avg `4.6239` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
