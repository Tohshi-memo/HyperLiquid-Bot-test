# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T22:22:25.071281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.1302` n `236`; crypto_major avg `-0.0397` n `8`; equity avg `-0.5593` n `151`; fx avg `0.0029` n `6`; index avg `-0.0681` n `26`; metal avg `0.0413` n `20`; unknown avg `-0.2904` n `1136`
- 1h: commodity avg `0.0169` n `13`; crypto_alt avg `0.2581` n `236`; crypto_major avg `0.0787` n `8`; equity avg `-0.6464` n `151`; fx avg `-0.0169` n `6`; index avg `-0.103` n `26`; metal avg `0.0331` n `20`; unknown avg `-0.2303` n `1054`
- 4h: commodity avg `0.0416` n `13`; crypto_alt avg `0.355` n `236`; crypto_major avg `0.1511` n `8`; equity avg `-1.1585` n `151`; fx avg `-0.0079` n `6`; index avg `-0.1513` n `26`; metal avg `0.0204` n `20`; unknown avg `1.0048` n `998`
- 24h: commodity avg `-0.0973` n `13`; crypto_alt avg `-2.2433` n `236`; crypto_major avg `-2.1407` n `8`; equity avg `-5.182` n `151`; fx avg `-0.1595` n `6`; index avg `-0.6745` n `26`; metal avg `-0.8111` n `20`; unknown avg `1392.5049` n `890`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0537`, n `666`, weak_sample_signal
