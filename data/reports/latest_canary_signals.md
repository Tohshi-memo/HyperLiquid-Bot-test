# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T07:00:26.340984+00:00`
- Correlation status: `ready`
- Asset price records: `51`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `7`; crypto_alt avg `0.1477` n `223`; crypto_major avg `0.2027` n `7`; equity avg `0.0517` n `42`; fx avg `-0.0056` n `4`; index avg `0.0092` n `9`; metal avg `0.0054` n `7`; unknown avg `0.0416` n `311`
- 1h: commodity avg `0.0173` n `7`; crypto_alt avg `0.2173` n `223`; crypto_major avg `0.247` n `7`; equity avg `0.1297` n `42`; fx avg `-0.0288` n `4`; index avg `-0.0012` n `9`; metal avg `0.0434` n `7`; unknown avg `0.032` n `311`
- 4h: commodity avg `-0.0139` n `7`; crypto_alt avg `-0.0604` n `223`; crypto_major avg `0.0294` n `7`; equity avg `0.1296` n `42`; fx avg `-0.1559` n `4`; index avg `-0.0059` n `9`; metal avg `0.0042` n `7`; unknown avg `-0.0257` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6329`, n `47`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6108`, n `47`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.578`, n `43`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5678`, n `47`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5498`, n `43`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5348`, n `47`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5008`, n `47`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4739`, n `43`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4699`, n `43`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4595`, n `43`, moderate_sample_signal
