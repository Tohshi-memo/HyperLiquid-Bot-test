# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T09:31:19.079281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `13`; crypto_alt avg `0.1935` n `239`; crypto_major avg `0.2404` n `8`; equity avg `0.1506` n `162`; fx avg `-0.0272` n `6`; index avg `0.0192` n `27`; metal avg `-0.0237` n `20`; unknown avg `0.1452` n `1263`
- 1h: commodity avg `-0.2551` n `13`; crypto_alt avg `0.1035` n `239`; crypto_major avg `-0.1673` n `8`; equity avg `-0.1568` n `162`; fx avg `-0.0086` n `6`; index avg `-0.0021` n `27`; metal avg `0.041` n `20`; unknown avg `9.26` n `1259`
- 4h: commodity avg `-0.2424` n `13`; crypto_alt avg `-0.2239` n `239`; crypto_major avg `-0.4013` n `8`; equity avg `-0.1055` n `162`; fx avg `-0.0211` n `6`; index avg `0.0495` n `27`; metal avg `-0.0698` n `20`; unknown avg `12.3394` n `1077`
- 24h: commodity avg `-0.5561` n `13`; crypto_alt avg `-0.93` n `239`; crypto_major avg `-1.0028` n `8`; equity avg `-0.7363` n `162`; fx avg `-0.0813` n `6`; index avg `-0.0231` n `27`; metal avg `-0.0116` n `20`; unknown avg `12.6495` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
