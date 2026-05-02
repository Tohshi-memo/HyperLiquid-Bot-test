# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T04:00:27.558657+00:00`
- Correlation status: `ready`
- Asset price records: `39`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `7`; crypto_alt avg `0.1044` n `223`; crypto_major avg `0.0567` n `7`; equity avg `-0.0606` n `42`; fx avg `-0.0042` n `4`; index avg `-0.0044` n `9`; metal avg `0.0008` n `7`; unknown avg `0.1997` n `311`
- 1h: commodity avg `-0.0013` n `7`; crypto_alt avg `0.0922` n `223`; crypto_major avg `0.0257` n `7`; equity avg `-0.0138` n `42`; fx avg `-0.0138` n `4`; index avg `0.0101` n `9`; metal avg `-0.0132` n `7`; unknown avg `0.0074` n `311`
- 4h: commodity avg `-0.0304` n `7`; crypto_alt avg `0.1849` n `223`; crypto_major avg `0.1683` n `7`; equity avg `0.1369` n `42`; fx avg `-0.0199` n `4`; index avg `0.0088` n `9`; metal avg `-0.0025` n `7`; unknown avg `0.0504` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6557`, n `35`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6322`, n `35`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5675`, n `35`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5505`, n `31`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5397`, n `31`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5345`, n `35`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5182`, n `35`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5019`, n `31`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4934`, n `31`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4905`, n `31`, moderate_sample_signal
