# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T13:37:28.245089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `-0.1313` n `239`; crypto_major avg `-0.0365` n `8`; equity avg `-0.0617` n `162`; fx avg `-0.0001` n `6`; index avg `-0.0019` n `27`; metal avg `0.0051` n `20`; unknown avg `0.1106` n `1262`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.5712` n `239`; crypto_major avg `-0.6785` n `8`; equity avg `-0.1798` n `162`; fx avg `0.0054` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0151` n `20`; unknown avg `158.6882` n `1260`
- 4h: commodity avg `-0.033` n `13`; crypto_alt avg `-0.8286` n `239`; crypto_major avg `-0.653` n `8`; equity avg `-0.2294` n `162`; fx avg `0.0135` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0182` n `20`; unknown avg `121.0632` n `1234`
- 24h: commodity avg `-0.1984` n `13`; crypto_alt avg `-4.9442` n `239`; crypto_major avg `-5.2449` n `8`; equity avg `-3.6846` n `162`; fx avg `-0.1524` n `6`; index avg `-0.317` n `27`; metal avg `-0.4743` n `20`; unknown avg `1.5198` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
