# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T05:37:33.740243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `13`; crypto_alt avg `0.1473` n `237`; crypto_major avg `0.0792` n `8`; equity avg `0.0054` n `151`; fx avg `-0.0008` n `6`; index avg `0.0069` n `26`; metal avg `0.025` n `20`; unknown avg `0.1456` n `1194`
- 1h: commodity avg `-0.0112` n `13`; crypto_alt avg `0.2088` n `237`; crypto_major avg `0.1199` n `8`; equity avg `-0.0551` n `151`; fx avg `-0.0367` n `6`; index avg `0.008` n `26`; metal avg `-0.0116` n `20`; unknown avg `1.1715` n `1190`
- 4h: commodity avg `-0.0699` n `13`; crypto_alt avg `-0.0861` n `237`; crypto_major avg `0.3314` n `8`; equity avg `0.4595` n `151`; fx avg `-0.0281` n `6`; index avg `0.0937` n `26`; metal avg `0.0922` n `20`; unknown avg `0.4422` n `1184`
- 24h: commodity avg `-0.4329` n `13`; crypto_alt avg `0.575` n `237`; crypto_major avg `1.1992` n `8`; equity avg `2.7193` n `151`; fx avg `-0.046` n `6`; index avg `0.524` n `26`; metal avg `0.3159` n `20`; unknown avg `3.6448` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1983`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.098`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
