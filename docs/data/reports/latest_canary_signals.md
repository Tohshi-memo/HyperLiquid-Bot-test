# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T06:15:21.163582+00:00`
- Correlation status: `ready`
- Asset price records: `48`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `7`; crypto_alt avg `0.0825` n `223`; crypto_major avg `0.0312` n `7`; equity avg `0.0097` n `42`; fx avg `0.0048` n `4`; index avg `-0.0077` n `9`; metal avg `0.0195` n `7`; unknown avg `0.0254` n `311`
- 1h: commodity avg `0.016` n `7`; crypto_alt avg `0.2329` n `223`; crypto_major avg `0.1261` n `7`; equity avg `0.1234` n `42`; fx avg `-0.0738` n `4`; index avg `0.01` n `9`; metal avg `0.0256` n `7`; unknown avg `-0.0142` n `311`
- 4h: commodity avg `0.003` n `7`; crypto_alt avg `-0.3178` n `223`; crypto_major avg `-0.1461` n `7`; equity avg `0.0371` n `42`; fx avg `-0.1291` n `4`; index avg `-0.0112` n `9`; metal avg `-0.0139` n `7`; unknown avg `-0.064` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6502`, n `44`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6274`, n `44`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5768`, n `40`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5674`, n `40`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5567`, n `44`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.518`, n `44`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5085`, n `44`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5042`, n `40`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5005`, n `40`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4953`, n `40`, moderate_sample_signal
