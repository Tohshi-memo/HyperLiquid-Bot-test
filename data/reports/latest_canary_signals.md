# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T12:30:26.404930+00:00`
- Correlation status: `ready`
- Asset price records: `73`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `7`; crypto_alt avg `0.2406` n `223`; crypto_major avg `0.1761` n `7`; equity avg `-0.0146` n `42`; fx avg `-0.012` n `4`; index avg `0.028` n `9`; metal avg `-0.006` n `7`; unknown avg `0.1372` n `313`
- 1h: commodity avg `-0.0213` n `7`; crypto_alt avg `0.2951` n `223`; crypto_major avg `0.0365` n `7`; equity avg `-0.0292` n `42`; fx avg `-0.0008` n `4`; index avg `0.035` n `9`; metal avg `0.0027` n `7`; unknown avg `0.0254` n `313`
- 4h: commodity avg `-0.04` n `7`; crypto_alt avg `0.5129` n `223`; crypto_major avg `-0.0208` n `7`; equity avg `-0.0943` n `42`; fx avg `-0.0176` n `4`; index avg `0.0323` n `9`; metal avg `0.0232` n `7`; unknown avg `0.0762` n `313`
- 24h: crypto_alt avg `1.0661` n `223`; crypto_major avg `0.7001` n `7`; metal avg `0.7906` n `1`; unknown avg `1.4334` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5732`, n `69`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5535`, n `69`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5522`, n `65`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5423`, n `65`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4944`, n `69`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4791`, n `65`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4751`, n `65`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4661`, n `65`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4597`, n `69`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4548`, n `69`, moderate_sample_signal
