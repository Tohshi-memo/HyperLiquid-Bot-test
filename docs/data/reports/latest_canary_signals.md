# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T00:07:24.016601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.0762` n `230`; crypto_major avg `0.1629` n `8`; equity avg `0.2383` n `102`; fx avg `-0.019` n `6`; index avg `0.0449` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.1655` n `778`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1842` n `230`; crypto_major avg `0.2737` n `8`; equity avg `0.3321` n `102`; fx avg `-0.0465` n `6`; index avg `0.0352` n `25`; metal avg `-0.0669` n `20`; unknown avg `0.1143` n `778`
- 4h: commodity avg `-0.0828` n `12`; crypto_alt avg `0.7476` n `230`; crypto_major avg `0.8577` n `8`; equity avg `0.3939` n `102`; fx avg `-0.0072` n `6`; index avg `0.2414` n `25`; metal avg `0.284` n `20`; unknown avg `0.8994` n `778`
- 24h: commodity avg `0.6259` n `12`; crypto_alt avg `-2.353` n `230`; crypto_major avg `-0.4858` n `8`; equity avg `-4.1584` n `102`; fx avg `-0.0216` n `6`; index avg `-0.7104` n `25`; metal avg `0.326` n `20`; unknown avg `-0.6806` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
