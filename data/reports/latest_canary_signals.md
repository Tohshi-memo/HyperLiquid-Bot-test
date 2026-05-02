# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T06:00:27.909881+00:00`
- Correlation status: `ready`
- Asset price records: `47`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `7`; crypto_alt avg `0.0054` n `223`; crypto_major avg `0.0097` n `7`; equity avg `0.0078` n `42`; fx avg `0.0128` n `4`; index avg `0.0038` n `9`; metal avg `-0.0014` n `7`; unknown avg `-0.0286` n `311`
- 1h: commodity avg `-0.0166` n `7`; crypto_alt avg `0.0256` n `223`; crypto_major avg `-0.0644` n `7`; equity avg `0.1503` n `42`; fx avg `-0.1046` n `4`; index avg `0.0119` n `9`; metal avg `-0.0015` n `7`; unknown avg `-0.077` n `311`
- 4h: commodity avg `-0.0108` n `7`; crypto_alt avg `-0.523` n `223`; crypto_major avg `-0.174` n `7`; equity avg `0.0591` n `42`; fx avg `-0.1441` n `4`; index avg `0.0117` n `9`; metal avg `-0.0336` n `7`; unknown avg `-0.0981` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6569`, n `43`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6338`, n `43`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.579`, n `39`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5779`, n `39`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5538`, n `43`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.518`, n `39`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.515`, n `43`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5146`, n `39`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5089`, n `43`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5067`, n `39`, strong_sample_signal
