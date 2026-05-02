# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T03:45:25.660437+00:00`
- Correlation status: `ready`
- Asset price records: `38`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `7`; crypto_alt avg `-0.1339` n `223`; crypto_major avg `-0.0366` n `7`; equity avg `0.0472` n `42`; fx avg `0.0077` n `4`; index avg `0.0082` n `9`; metal avg `-0.0034` n `7`; unknown avg `-0.0375` n `311`
- 1h: commodity avg `-0.008` n `7`; crypto_alt avg `-0.1503` n `223`; crypto_major avg `-0.0134` n `7`; equity avg `-0.0188` n `42`; fx avg `0.0042` n `4`; index avg `0.0126` n `9`; metal avg `0.0005` n `7`; unknown avg `-0.018` n `311`
- 4h: commodity avg `-0.043` n `7`; crypto_alt avg `0.0521` n `223`; crypto_major avg `0.235` n `7`; equity avg `0.0806` n `42`; fx avg `-0.0053` n `4`; index avg `0.0475` n `9`; metal avg `-0.0017` n `7`; unknown avg `0.047` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6572`, n `34`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6337`, n `34`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5577`, n `34`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.551`, n `30`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5384`, n `30`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5219`, n `34`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5155`, n `34`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.501`, n `30`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4926`, n `30`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4926`, n `30`, moderate_sample_signal
