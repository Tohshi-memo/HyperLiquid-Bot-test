# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T01:07:27.278932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `-0.1542` n `238`; crypto_major avg `-0.0078` n `8`; equity avg `0.06` n `156`; fx avg `0.0057` n `6`; index avg `0.0055` n `27`; metal avg `-0.0033` n `20`; unknown avg `7.839` n `1256`
- 1h: commodity avg `-0.0509` n `13`; crypto_alt avg `0.0975` n `238`; crypto_major avg `0.1722` n `8`; equity avg `0.0619` n `156`; fx avg `0.0015` n `6`; index avg `0.0046` n `27`; metal avg `0.0115` n `20`; unknown avg `-0.215` n `1254`
- 4h: commodity avg `-0.0983` n `13`; crypto_alt avg `1.3659` n `238`; crypto_major avg `0.7884` n `8`; equity avg `0.2964` n `156`; fx avg `-0.0478` n `6`; index avg `0.0272` n `27`; metal avg `0.0504` n `20`; unknown avg `4.1636` n `1249`
- 24h: commodity avg `0.0291` n `13`; crypto_alt avg `4.5268` n `238`; crypto_major avg `1.3344` n `8`; equity avg `-1.5069` n `156`; fx avg `-0.1341` n `6`; index avg `-0.0701` n `27`; metal avg `-0.6401` n `20`; unknown avg `3.5749` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
