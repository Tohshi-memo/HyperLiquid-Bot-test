# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T07:15:19.548593+00:00`
- Correlation status: `ready`
- Asset price records: `52`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `7`; crypto_alt avg `0.0169` n `223`; crypto_major avg `-0.0637` n `7`; equity avg `0.0016` n `42`; fx avg `0.035` n `4`; index avg `-0.021` n `9`; metal avg `0.0059` n `7`; unknown avg `-0.0476` n `311`
- 1h: commodity avg `-0.0317` n `7`; crypto_alt avg `0.1521` n `223`; crypto_major avg `0.1519` n `7`; equity avg `0.1214` n `42`; fx avg `0.0013` n `4`; index avg `-0.0145` n `9`; metal avg `0.0297` n `7`; unknown avg `-0.0428` n `311`
- 4h: commodity avg `-0.0198` n `7`; crypto_alt avg `-0.0064` n `223`; crypto_major avg `0.1067` n `7`; equity avg `0.2333` n `42`; fx avg `-0.1156` n `4`; index avg `-0.0293` n `9`; metal avg `0.0117` n `7`; unknown avg `-0.0515` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6258`, n `48`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6039`, n `48`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.58`, n `44`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5689`, n `48`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.547`, n `44`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5374`, n `48`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4933`, n `48`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4683`, n `44`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4574`, n `44`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.4532`, n `44`, moderate_sample_signal
