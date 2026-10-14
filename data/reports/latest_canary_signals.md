# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T20:07:32.759248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `13`; crypto_alt avg `0.2233` n `236`; crypto_major avg `0.0495` n `8`; equity avg `-0.0862` n `151`; fx avg `0.0093` n `6`; index avg `-0.0276` n `26`; metal avg `-0.0143` n `20`; unknown avg `2.3573` n `1106`
- 1h: commodity avg `0.0841` n `13`; crypto_alt avg `0.3513` n `236`; crypto_major avg `0.4052` n `8`; equity avg `0.1422` n `151`; fx avg `0.034` n `6`; index avg `0.0225` n `26`; metal avg `0.0148` n `20`; unknown avg `14.5964` n `1090`
- 4h: commodity avg `0.0669` n `13`; crypto_alt avg `0.5575` n `236`; crypto_major avg `0.1595` n `8`; equity avg `-0.7858` n `151`; fx avg `0.0248` n `6`; index avg `-0.136` n `26`; metal avg `-0.0309` n `20`; unknown avg `0.2331` n `1088`
- 24h: commodity avg `-0.1505` n `13`; crypto_alt avg `-2.593` n `236`; crypto_major avg `-2.0003` n `8`; equity avg `-4.2101` n `151`; fx avg `-0.1188` n `6`; index avg `-0.5836` n `26`; metal avg `-0.8632` n `20`; unknown avg `1305.3776` n `948`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0598`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0577`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0565`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
