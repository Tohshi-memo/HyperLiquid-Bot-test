# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T04:52:24.009951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `0.0119` n `235`; crypto_major avg `-0.056` n `8`; equity avg `0.0235` n `151`; fx avg `-0.0102` n `6`; index avg `0.0053` n `26`; metal avg `0.0251` n `20`; unknown avg `-0.108` n `1135`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `0.1397` n `235`; crypto_major avg `-0.0248` n `8`; equity avg `-0.0642` n `151`; fx avg `0.0014` n `6`; index avg `0.0118` n `26`; metal avg `0.0385` n `20`; unknown avg `-0.3166` n `1127`
- 4h: commodity avg `-0.1431` n `13`; crypto_alt avg `0.4147` n `235`; crypto_major avg `0.2751` n `8`; equity avg `-0.0575` n `151`; fx avg `-0.0279` n `6`; index avg `0.0479` n `26`; metal avg `0.1671` n `20`; unknown avg `-0.1856` n `1127`
- 24h: commodity avg `1.0571` n `13`; crypto_alt avg `0.0719` n `235`; crypto_major avg `0.1563` n `8`; equity avg `0.7624` n `151`; fx avg `0.0592` n `6`; index avg `0.2246` n `26`; metal avg `-0.284` n `20`; unknown avg `1.1872` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1534`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1362`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0865`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `666`, weak_sample_signal
