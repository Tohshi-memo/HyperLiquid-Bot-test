# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T07:45:37.032720+00:00`
- Correlation status: `ready`
- Asset price records: `54`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `7`; crypto_alt avg `-0.0024` n `223`; crypto_major avg `-0.0139` n `7`; equity avg `-0.0318` n `42`; fx avg `0.0336` n `4`; index avg `-0.0383` n `9`; metal avg `0.016` n `7`; unknown avg `0.0192` n `311`
- 1h: commodity avg `-0.0069` n `7`; crypto_alt avg `0.2242` n `223`; crypto_major avg `0.1465` n `7`; equity avg `0.0328` n `42`; fx avg `0.04` n `4`; index avg `-0.0602` n `9`; metal avg `0.0273` n `7`; unknown avg `-0.0269` n `311`
- 4h: commodity avg `0.0013` n `7`; crypto_alt avg `0.031` n `223`; crypto_major avg `0.0042` n `7`; equity avg `0.0718` n `42`; fx avg `-0.101` n `4`; index avg `-0.0897` n `9`; metal avg `0.0402` n `7`; unknown avg `0.0683` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6032`, n `50`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5824`, n `46`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5822`, n `50`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5702`, n `50`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5425`, n `46`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5376`, n `50`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4965`, n `50`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4611`, n `46`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4452`, n `46`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.443`, n `46`, moderate_sample_signal
