# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T01:22:28.111220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.1217` n `236`; crypto_major avg `-0.1542` n `8`; equity avg `0.0862` n `151`; fx avg `0.0018` n `6`; index avg `0.013` n `26`; metal avg `0.0262` n `20`; unknown avg `-0.0963` n `1136`
- 1h: commodity avg `-0.0128` n `13`; crypto_alt avg `0.1817` n `236`; crypto_major avg `-0.0191` n `8`; equity avg `0.8547` n `151`; fx avg `0.0713` n `6`; index avg `0.1376` n `26`; metal avg `0.0359` n `20`; unknown avg `0.6488` n `1134`
- 4h: commodity avg `-0.0333` n `13`; crypto_alt avg `-0.0001` n `236`; crypto_major avg `-0.3793` n `8`; equity avg `0.0414` n `151`; fx avg `0.0857` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0857` n `20`; unknown avg `0.1566` n `1096`
- 24h: commodity avg `-0.0007` n `13`; crypto_alt avg `1.4343` n `236`; crypto_major avg `0.6256` n `8`; equity avg `1.6784` n `151`; fx avg `0.0365` n `6`; index avg `0.2854` n `26`; metal avg `0.1538` n `20`; unknown avg `25.7316` n `910`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0878`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0675`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
