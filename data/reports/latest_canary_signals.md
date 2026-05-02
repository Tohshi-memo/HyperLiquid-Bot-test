# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T05:00:31.285077+00:00`
- Correlation status: `ready`
- Asset price records: `43`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `7`; crypto_alt avg `-0.1047` n `223`; crypto_major avg `-0.0544` n `7`; equity avg `-0.06` n `42`; fx avg `0.0119` n `4`; index avg `0.004` n `9`; metal avg `0.0008` n `7`; unknown avg `0.0379` n `311`
- 1h: commodity avg `-0.0133` n `7`; crypto_alt avg `-0.3923` n `223`; crypto_major avg `-0.1783` n `7`; equity avg `-0.132` n `42`; fx avg `-0.009` n `4`; index avg `-0.0267` n `9`; metal avg `-0.0244` n `7`; unknown avg `0.0246` n `311`
- 4h: commodity avg `-0.0536` n `7`; crypto_alt avg `-0.3855` n `223`; crypto_major avg `-0.0573` n `7`; equity avg `-0.0088` n `42`; fx avg `-0.0405` n `4`; index avg `0.0137` n `9`; metal avg `-0.0202` n `7`; unknown avg `0.2427` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6558`, n `39`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6325`, n `39`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5868`, n `35`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5712`, n `35`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5461`, n `39`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5357`, n `35`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5241`, n `35`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5168`, n `35`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5087`, n `39`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5071`, n `39`, strong_sample_signal
