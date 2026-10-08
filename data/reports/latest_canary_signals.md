# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T12:22:29.680554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `13`; crypto_alt avg `0.1459` n `235`; crypto_major avg `0.0575` n `8`; equity avg `-0.0076` n `150`; fx avg `-0.0022` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0145` n `20`; unknown avg `-0.0128` n `1077`
- 1h: commodity avg `0.0589` n `13`; crypto_alt avg `-0.1492` n `235`; crypto_major avg `-0.2326` n `8`; equity avg `0.1168` n `150`; fx avg `0.0084` n `6`; index avg `0.0418` n `26`; metal avg `0.0269` n `20`; unknown avg `0.1103` n `1069`
- 4h: commodity avg `0.2047` n `13`; crypto_alt avg `-0.5235` n `235`; crypto_major avg `-1.0106` n `8`; equity avg `-0.3851` n `150`; fx avg `0.0351` n `6`; index avg `-0.0363` n `26`; metal avg `-0.1163` n `20`; unknown avg `2.5195` n `1069`
- 24h: commodity avg `0.8516` n `13`; crypto_alt avg `0.1306` n `235`; crypto_major avg `-2.1083` n `8`; equity avg `-1.206` n `150`; fx avg `0.0737` n `6`; index avg `-0.1697` n `26`; metal avg `-0.0572` n `20`; unknown avg `416.5781` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
